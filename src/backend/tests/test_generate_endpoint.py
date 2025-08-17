import os
import re
import pathlib
import src.backend.app as appmod


def test_generate_endpoint_creates_image_and_returns_record():
    # Call the endpoint function directly to avoid TestClient/httpx issues
    inp = appmod.GenerateIn(prompt='Unit test prompt')
    result = appmod.generate(inp)
    # result is a ShirtOut Pydantic model
    assert hasattr(result, 'imageUrl')
    image_url = result.imageUrl

    # Ensure the image file exists on disk
    m = re.search(r'/static/(.+)$', image_url)
    assert m, 'imageUrl should reference a path under /static'
    rel_path = m.group(1)
    abs_path = pathlib.Path(appmod.IMAGES_DIR.parent) / rel_path
    assert abs_path.exists(), f'Expected generated image at {abs_path}'

    # Cleanup
    try:
        os.remove(abs_path)
    except Exception:
        pass
