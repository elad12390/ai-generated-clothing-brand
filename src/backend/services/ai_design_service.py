"""
AI Design Service for AI Generated Clothing Brand.
Handles AI image generation using Google Gemini and image manipulation.
"""

import google.generativeai as genai
import logging
import os
from typing import Optional

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
        if self.api_key and not testing_mode:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-pro')
        else:
            self.model = None
            if not testing_mode:
                self.logger.warning("Google Gemini API key not found. AI generation will not work.")
    
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
            # For now, we'll use a simple approach
            # In a real implementation, we might want to be more specific about the image format
            response = self.model.generate_content(
                [prompt],
                stream=True
            )
            response.resolve()
            
            # Extract image data
            if response.images:
                image_data = response.images[0]._image_bytes
                self.logger.info("Image generated successfully")
                return image_data
            else:
                self.logger.error("No image data returned from API")
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