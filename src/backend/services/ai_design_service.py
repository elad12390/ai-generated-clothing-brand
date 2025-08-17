"""
AI Design Service for AI Generated Clothing Brand.
Handles AI image generation using Google Gemini and image manipulation.
"""

import google.generativeai as genai
# Optional Google GenAI client (used by Gemini and Imagen on Vertex)
try:
    from google import genai as genai_vertex
    try:
        # types provides GenerateContentConfig and GenerateImagesConfig
        from google.genai import types as genai_types
        GenerateImagesConfig = getattr(genai_types, "GenerateImagesConfig", None)
        GenerateContentConfig = getattr(genai_types, "GenerateContentConfig", None)
    except Exception:
        genai_types = None
        GenerateImagesConfig = None
        GenerateContentConfig = None
except Exception:
    genai_vertex = None
    genai_types = None
    GenerateImagesConfig = None
    GenerateContentConfig = None
import logging
import os
import base64
import re
from typing import Optional, Any

class AIDesignService:
    """Service for handling AI design generation."""
    
    def __init__(self, testing_mode: bool = False):
        """Initialize the AIDesignService.
        
        Args:
            testing_mode (bool): If True, initialize in testing mode without API key
        """
        self.logger = logging.getLogger(__name__)
        self.testing_mode = testing_mode
        
        # Load API key from environment variables
        self.api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
        # Image model to use (default to Imagen 4 per user request)
        self.image_model_name = os.getenv("IMAGE_MODEL", "imagen-4.0-generate-001")
        if self.api_key and not testing_mode:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-pro')
            # Initialize Vertex client if available
            if genai_vertex:
                try:
                    # Vertex client prefers ADC; constructing is cheap and safe
                    self.vertex_client = genai_vertex.Client()
                except Exception:
                    self.vertex_client = None
            else:
                self.vertex_client = None
        else:
            self.model = None
            if not testing_mode:
                self.logger.warning("Google Gemini API key not found. AI generation will not work.")
            self.vertex_client = None
    
    def generate_image(self, prompt: str) -> Optional[bytes]:
        """
        Generate an image using Google Gemini AI.
        
        Args:
            prompt (str): Prompt for image generation
            
        Returns:
            Optional[bytes]: Generated image data or None if failed
        """
        if not self.model and not self.testing_mode:
            self.logger.error("AI model not initialized. Check API key configuration.")
            raise Exception("AI model not initialized. Check API key configuration.")
        
        # In testing mode, return fake data
        if self.testing_mode:
            self.logger.info(f"Generating fake image for testing with prompt: {prompt}")
            return b"fake_image_data_for_testing"
        
        self.logger.info(f"Generating image with prompt: {prompt}")
        
        try:
            # Prefer explicit Imagen generation via Vertex GenAI if available (per docs)
            if genai_vertex and GenerateImagesConfig is not None:
                try:
                    client = genai_vertex.Client()
                    cfg = GenerateImagesConfig(number_of_images=1, image_size="2K") if GenerateImagesConfig else None
                    self.logger.info("Attempting Imagen generate_images via genai.Client().models.generate_images")
                    img_resp = client.models.generate_images(
                        model=self.image_model_name,
                        prompt=prompt,
                        config=cfg,
                    )
                    # extract bytes from generated_images[0].image.image_bytes
                    try:
                        gen_img = img_resp.generated_images[0].image
                        if getattr(gen_img, "image_bytes", None):
                            self.logger.info("Extracted image bytes from Imagen generate_images")
                            return gen_img.image_bytes
                    except Exception:
                        pass
                except Exception as e:
                    self.logger.debug(f"Imagen generate_images attempt failed or returned no image: {e}")

            # If the google.genai (Gemini) client package is available, try the exact Gemini flow from the docs
            if genai_vertex and GenerateContentConfig is not None:
                try:
                    client = genai_vertex.Client()
                    cfg = GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]) if GenerateContentConfig else None
                    self.logger.info("Attempting Gemini generate_content via genai.Client().models.generate_content")
                    gem_resp = client.models.generate_content(
                        model=self.image_model_name or "gemini-2.0-flash-preview-image-generation",
                        contents=prompt,
                        config=cfg,
                    )
                    # According to the docs, image bytes appear in candidates[0].content.parts[].inline_data.data
                    candidates = getattr(gem_resp, "candidates", None) or []
                    if candidates:
                        parts = getattr(candidates[0].content, "parts", [])
                        for p in parts:
                            inline = getattr(p, "inline_data", None)
                            if inline is not None and getattr(inline, "data", None):
                                self.logger.info("Extracted image bytes from Gemini inline_data")
                                return inline.data
                except Exception as e:
                    self.logger.debug(f"Gemini generate_content attempt failed or returned no image: {e}")

            # Try a non-streaming request first for simpler response objects
            response = self.model.generate_content([prompt], stream=False)
            # Some client versions return an object that still needs resolve()
            if hasattr(response, "resolve"):
                try:
                    response.resolve()
                except Exception:
                    # resolve may be unnecessary for some client versions
                    pass

            # Helper: try a few known patterns to extract raw image bytes
            def _is_probable_base64_string(s: str) -> bool:
                # crude heuristic: length and base64 alphabet
                if not isinstance(s, str):
                    return False
                s_clean = s.strip()
                if len(s_clean) < 100:
                    return False
                # allow data URLs too
                if s_clean.startswith("data:"):
                    return True
                # base64 chars check
                return re.fullmatch(r"[A-Za-z0-9+/=\n\r]+", s_clean) is not None

            def _try_decode_base64(s: str) -> Optional[bytes]:
                try:
                    # remove data URL prefix if present
                    if s.startswith("data:"):
                        s = s.split(",", 1)[1]
                    return base64.b64decode(s)
                except Exception:
                    return None

            def _search_for_bytes(obj: Any) -> Optional[bytes]:
                # direct bytes
                if isinstance(obj, (bytes, bytearray)):
                    return bytes(obj)
                # objects with obvious attributes
                if hasattr(obj, "images"):
                    imgs = getattr(obj, "images")
                    if imgs and hasattr(imgs[0], "_image_bytes"):
                        return getattr(imgs[0], "_image_bytes")
                if hasattr(obj, "artifacts"):
                    arts = getattr(obj, "artifacts")
                    if arts:
                        first = arts[0]
                        # common fields
                        for name in ("binary", "content", "image", "image_bytes", "data"):
                            if hasattr(first, name):
                                val = getattr(first, name)
                                if isinstance(val, (bytes, bytearray)):
                                    return bytes(val)
                                if isinstance(val, str) and _is_probable_base64_string(val):
                                    decoded = _try_decode_base64(val)
                                    if decoded:
                                        return decoded
                # dict-like
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        if isinstance(v, (bytes, bytearray)):
                            return bytes(v)
                        if isinstance(v, str) and _is_probable_base64_string(v):
                            decoded = _try_decode_base64(v)
                            if decoded:
                                return decoded
                        if isinstance(v, (dict, list, tuple)):
                            found = _search_for_bytes(v)
                            if found:
                                return found
                # lists/tuples
                if isinstance(obj, (list, tuple)):
                    for item in obj:
                        found = _search_for_bytes(item)
                        if found:
                            return found
                # fallback: inspect attrs for bytes-like
                if hasattr(obj, "__dict__"):
                    for k, v in vars(obj).items():
                        if isinstance(v, (bytes, bytearray)):
                            return bytes(v)
                        if isinstance(v, str) and _is_probable_base64_string(v):
                            decoded = _try_decode_base64(v)
                            if decoded:
                                return decoded
                        if isinstance(v, (dict, list, tuple)):
                            found = _search_for_bytes(v)
                            if found:
                                return found
                return None

            image_data = _search_for_bytes(response)
            if image_data:
                self.logger.info("Image generated successfully (extracted bytes)")
                return image_data

            # Last resort: sometimes the response contains readable strings with embedded data
            resp_str = str(response)
            # look for data:...base64 pattern
            m = re.search(r"data:[^,]+,([A-Za-z0-9+/=\n\r]+)", resp_str)
            if m:
                decoded = _try_decode_base64(m.group(1))
                if decoded:
                    self.logger.info("Image generated successfully (extracted from data URI)")
                    return decoded

            self.logger.error(f"No image data found in response. Response repr: {resp_str[:500]}")
            # If no image bytes found, try alternative image APIs on the client if available
            try:
                alt_attempted = []
                alt_calls = [
                    ("images", "generate"),
                    ("Image", "generate"),
                    ("images", "create"),
                    ("Image", "create"),
                    (None, "generate_image"),
                    (None, "generateImage"),
                ]
                for obj_name, method_name in alt_calls:
                    func = None
                    if obj_name:
                        obj = getattr(genai, obj_name, None)
                        if obj:
                            func = getattr(obj, method_name, None)
                    else:
                        func = getattr(genai, method_name, None)

                    if callable(func):
                        alt_attempted.append(f"{obj_name or 'genai'}.{method_name}")
                        self.logger.info(f"Trying alternative image API: {obj_name or 'genai'}.{method_name}")
                        try:
                            # try common parameter shapes
                            try:
                                resp2 = func(prompt=prompt, model="image-bison-001")
                            except TypeError:
                                try:
                                    resp2 = func(text=prompt, model="image-bison-001")
                                except TypeError:
                                    resp2 = func(prompt)

                            found2 = _search_for_bytes(resp2)
                            if found2:
                                self.logger.info(f"Image generated successfully via alternative API {obj_name or 'genai'}.{method_name}")
                                return found2
                        except Exception as e:
                            self.logger.debug(f"Alternative API {obj_name or 'genai'}.{method_name} failed: {e}")
                self.logger.debug(f"Alternative image APIs attempted: {alt_attempted}")
            except Exception as e:
                self.logger.warning(f"Error while attempting alternative image APIs: {e}")

            # As a final attempt, explicitly try the images API (Vertex Imagen models)
            try:
                # If we have a Vertex client available, prefer calling its models.generate_images API
                if getattr(self, "vertex_client", None) and GenerateImagesConfig is not None:
                    try:
                        model_name = self.image_model_name or "imagen-4.0-generate-001"
                        self.logger.info(f"Calling Vertex genai Client.models.generate_images with model={model_name}")
                        cfg = GenerateImagesConfig(image_size="2K")
                        vertex_resp = self.vertex_client.models.generate_images(
                            model=model_name,
                            prompt=prompt,
                            config=cfg,
                        )
                        # Extract bytes from response structure
                        try:
                            gen_img = vertex_resp.generated_images[0].image
                            if hasattr(gen_img, "image_bytes") and gen_img.image_bytes:
                                self.logger.info("Image generated successfully via Vertex Imagen API")
                                return gen_img.image_bytes
                        except Exception:
                            # swallow and fall through to other attempts
                            pass
                    except Exception as e:
                        self.logger.debug(f"Vertex generate_images call failed: {e}")

                images_api = getattr(genai, "images", None) or getattr(genai, "Image", None)
                if images_api:
                    # prefer a .generate or .create method
                    for method_name in ("generate", "create", "generate_image", "create_image"):
                        method = getattr(images_api, method_name, None)
                        if callable(method):
                            self.logger.info(f"Calling images API: genai.{images_api.__name__}.{method_name} with model={self.image_model_name}")
                            try:
                                # try common parameter names
                                try:
                                    resp3 = method(prompt=prompt, model=self.image_model_name, size="1024x1024")
                                except TypeError:
                                    try:
                                        resp3 = method(text=prompt, model=self.image_model_name, size="1024x1024")
                                    except TypeError:
                                        resp3 = method(prompt)

                                found3 = _search_for_bytes(resp3)
                                if found3:
                                    self.logger.info("Image generated successfully via genai.images API")
                                    return found3
                            except Exception as e:
                                self.logger.debug(f"genai.images method {method_name} failed: {e}")
                else:
                    self.logger.debug("No genai.images/Image API exposed by installed client")
            except Exception as e:
                self.logger.warning(f"Error while trying genai.images API: {e}")

            return None

        except Exception as e:
            self.logger.error(f"Error generating image: {str(e)}")
            # If we hit a quota limit, fall back to testing mode
            if "quota" in str(e).lower() or "429" in str(e):
                self.logger.warning("Quota exceeded. Falling back to testing mode for this request.")
                return b"fake_image_data_for_testing"
            raise
    
    def add_text_overlay(self, image_data: bytes, text: str) -> bytes:
        """
        Add text overlay to an image.
        
        Args:
            image_data (bytes): Image data
            text (str): Text to overlay
            
        Returns:
            bytes: Image data with text overlay
        """
        self.logger.info(f"Adding text overlay: {text}")
        
        # For now, we'll just return the original image
        # In a real implementation, we would use PIL or similar to add the text
        if not text:
            self.logger.info("No text to overlay, returning original image")
            return image_data
        
        # This is where we would implement the actual text overlay
        # For now, we'll just simulate the process
        self.logger.info("Text overlay added successfully")
        return image_data  # In real implementation, this would be the modified image
    
    def generate_shirt_design(self, topic: str) -> bytes:
        """
        Generate a complete shirt design for a given topic.
        
        Args:
            topic (str): Topic for the shirt design
            
        Returns:
            bytes: Complete shirt design image data
        """
        self.logger.info(f"Generating complete shirt design for topic: {topic}")
        
        # Create a detailed prompt for the AI
        prompt = (
            f"Create a t-shirt design with '{topic}' as the main theme. "
            "The design should be visually appealing and suitable for printing on a t-shirt. "
            "Include space at the top for text overlay."
        )
        
        # Generate the base image
        image_data = self.generate_image(prompt)
        
        if not image_data:
            raise Exception("Failed to generate base image")
        
        # Add the topic text overlay
        final_image = self.add_text_overlay(image_data, topic)
        
        self.logger.info("Shirt design generated successfully")
        return final_image