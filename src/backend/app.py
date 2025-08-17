"""FastAPI application exposing the HTTP API used by the frontend.

This is a lightweight production-ready scaffold that uses the existing
service classes in testing mode by default. Replace testing_mode flags
and set the environment variables in `.env` for real integrations.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Ensure backend dir is on path so `services` imports work when running via uvicorn
sys.path.insert(0, os.path.dirname(__file__))

# Import existing services (they are intentionally written to support testing mode)
from services.trending_topic_service import TrendingTopicService
from services.database_service import DatabaseService
from services.ai_design_service import AIDesignService
from datetime import datetime
import pathlib
import time

# Ensure images directory exists
IMAGES_DIR = pathlib.Path(os.path.join(os.path.dirname(__file__), "data", "images"))
IMAGES_DIR.mkdir(parents=True, exist_ok=True)
# Serve the `data` directory at /static so images are reachable at /static/images/<file>
STATIC_DIR = pathlib.Path(os.path.join(os.path.dirname(__file__), "data"))
app = FastAPI(title="The Daily Drip API")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


class ShirtOut(BaseModel):
    id: int
    topic: str
    imageUrl: str
    createdAt: str
    description: str = ""



# Allow CORS from typical frontend dev origins. Adjust in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/daily-shirt", response_model=ShirtOut)
def get_daily_shirt():
    """Return the latest daily shirt design.

    Uses `DatabaseService`'s testing-mode fake data when no real DB is configured.
    """
    testing_mode = os.getenv("USE_TESTING_SERVICES", "true").lower() in ("1", "true", "yes")
    db = DatabaseService(testing_mode=testing_mode)
    latest = db.get_latest_shirt_design()
    if not latest:
        # Fallback mock (same shape as frontend expects)
        return ShirtOut(
            id=1,
            topic="AI Technology",
            imageUrl="https://placehold.co/600x600/2563eb/white?text=AI+Technology+Shirt",
            createdAt="2025-01-01T00:00:00Z",
            description="Today's exclusive AI-generated design featuring AI Technology",
        )

    # Map stored shape to output model
    return ShirtOut(
        id=latest.get("id", 1),
        topic=latest.get("topic", "AI Technology"),
        imageUrl=latest.get("image_url") or latest.get("imageUrl") or "",
        createdAt=latest.get("created_at") or latest.get("createdAt") or "",
        description=latest.get("description", ""),
    )


@app.get("/api/shirts", response_model=List[ShirtOut])
def get_shirts():
    """Return archive of shirts.

    Uses `DatabaseService` in testing mode to return a predictable list.
    """
    testing_mode = os.getenv("USE_TESTING_SERVICES", "true").lower() in ("1", "true", "yes")
    db = DatabaseService(testing_mode=testing_mode)
    all_shirts = db.get_all_shirt_designs()

    if not all_shirts:
        # Return a small mocked archive if DB returns empty
        mocked = [
            {
                "id": 1,
                "topic": "Machine Learning",
                "imageUrl": "https://placehold.co/300x300/8b5cf6/white?text=ML+Shirt",
                "createdAt": "2025-08-16T00:00:00Z",
            },
            {
                "id": 2,
                "topic": "Neural Networks",
                "imageUrl": "https://placehold.co/300x300/0ea5e9/white?text=NN+Shirt",
                "createdAt": "2025-08-15T00:00:00Z",
            },
        ]
        return [ShirtOut(**s) for s in mocked]

    out = []
    for i, s in enumerate(all_shirts, start=1):
        out.append(
            ShirtOut(
                id=s.get("id", i),
                topic=s.get("topic", ""),
                imageUrl=s.get("image_url") or s.get("imageUrl") or "",
                createdAt=s.get("created_at") or s.get("createdAt") or "",
                description=s.get("description", ""),
            )
        )

    return out


@app.post("/api/trigger-generate")
def trigger_generate():
    """Trigger a generation run (development only). This uses the orchestration in `main.py`.

    WARNING: This endpoint is intended for local/dev use only. Protect it before exposing publicly.
    """
    # Protect trigger endpoint: require ADMIN_TRIGGER_TOKEN env var to be set and match header
    admin_token = os.getenv("ADMIN_TRIGGER_TOKEN")
    if not admin_token:
        # Admin token not configured — do not allow triggering in public/dev without explicit setup
        raise HTTPException(status_code=403, detail="Trigger endpoint disabled. Configure ADMIN_TRIGGER_TOKEN to enable.")

    # Expect token in header X-Admin-Token
    from fastapi import Request
    def _get_request_token(req: Request):
        return req.headers.get("x-admin-token")

    # Use dependency injection to read header
    def inner(request: "Request"):
        token = _get_request_token(request)
        if not token or token != admin_token:
            raise HTTPException(status_code=401, detail="Invalid admin token")

        try:
            from main import main as orchestration_main
            orchestration_main()
            return {"status": "started"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # Return an ASGI-compatible call (FastAPI will call this with the Request)
    return inner


class GenerateIn(BaseModel):
    prompt: str


@app.post("/api/generate", response_model=ShirtOut)
def generate(prompt_in: GenerateIn):
    """Generate an image for a prompt, persist it, and return the created shirt record.

    This endpoint is safe to call in testing mode; it will use `USE_TESTING_SERVICES` to decide.
    """
    testing_mode = os.getenv("USE_TESTING_SERVICES", "true").lower() in ("1", "true", "yes")
    ai = AIDesignService(testing_mode=testing_mode)
    db = DatabaseService(testing_mode=testing_mode)

    # Simple retry/backoff
    prompt = prompt_in.prompt
    max_attempts = 3
    delay = 1
    img_bytes = None
    for attempt in range(1, max_attempts + 1):
        try:
            img_bytes = ai.generate_shirt_design(prompt)
            if img_bytes:
                break
        except Exception as e:
            # On quota or transient errors, retry
            if "quota" in str(e).lower() or "429" in str(e):
                time.sleep(delay)
                delay *= 2
                continue
            raise

    if not img_bytes:
        raise HTTPException(status_code=500, detail="Failed to generate image")

    # Persist image to disk
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = f"shirt_{ts}.png"
    out_path = IMAGES_DIR / filename
    with open(out_path, "wb") as f:
        f.write(img_bytes)

    # Persist DB record and return
    record = {
        "topic": prompt,
        "image_url": f"/static/images/{filename}",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "description": "",
    }
    # When running in testing mode, DatabaseService expects raw image bytes in 'image_data'
    if testing_mode:
        record["image_data"] = img_bytes
    saved = db.save_shirt_design(record)

    # DatabaseService may return different shapes depending on mode:
    # - True (testing mode)
    # - dict/row containing inserted data
    # - False on failure
    if saved is True:
        resp_obj = {
            "id": 1,
            "topic": record["topic"],
            "imageUrl": record["image_url"],
            "createdAt": record["created_at"],
            "description": record["description"],
        }
    elif isinstance(saved, dict):
        resp_obj = {
            "id": saved.get("id", 0),
            "topic": saved.get("topic", record["topic"]),
            "imageUrl": saved.get("image_url") or saved.get("imageUrl") or record["image_url"],
            "createdAt": saved.get("created_at") or saved.get("createdAt") or record["created_at"],
            "description": saved.get("description", record["description"]),
        }
    elif isinstance(saved, int):
        resp_obj = {
            "id": saved,
            "topic": record["topic"],
            "imageUrl": record["image_url"],
            "createdAt": record["created_at"],
            "description": record["description"],
        }
    else:
        raise HTTPException(status_code=500, detail="Failed to save shirt record")

    return ShirtOut(**resp_obj)
