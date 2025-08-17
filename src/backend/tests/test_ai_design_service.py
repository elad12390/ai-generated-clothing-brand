import pytest
from services.ai_design_service import AIDesignService


def test_generate_image_testing_mode_returns_fake_bytes():
    svc = AIDesignService(testing_mode=True)
    img = svc.generate_image("anything")
    assert isinstance(img, (bytes, bytearray))
    assert b"fake_image_data" in img


def test_generate_shirt_design_and_overlay():
    svc = AIDesignService(testing_mode=True)
    result = svc.generate_shirt_design("Test Topic")
    assert isinstance(result, (bytes, bytearray))

    # Current add_text_overlay returns the original image data in testing mode
    over = svc.add_text_overlay(result, "Hello")
    assert over == result
"""
Test suite for AI design generation functionality.
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the backend directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.ai_design_service import AIDesignService

class TestAIDesignService:
    """Test cases for the AIDesignService class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.service = AIDesignService(testing_mode=True)
    
    def test_generate_image_with_valid_prompt(self):
        """Test that generate_image creates an image with a valid prompt."""
        # Arrange
        prompt = "AI Technology"
        
        # Act
        result = self.service.generate_image(prompt)
        
        # Assert
        assert result is not None
        assert isinstance(result, bytes)
        assert result == b"fake_image_data_for_testing"
    
    def test_generate_image_handles_api_errors(self):
        """Test that generate_image handles API errors gracefully."""
        # Arrange
        # Create a service without testing mode to test error handling
        service_with_errors = AIDesignService(testing_mode=False)
        
        # Mock the model to be None to simulate missing API key
        service_with_errors.model = None
        prompt = "AI Technology"
        
        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            service_with_errors.generate_image(prompt)
        
        assert str(exc_info.value) == "AI model not initialized. Check API key configuration."
    
    def test_add_text_overlay_with_valid_inputs(self):
        """Test that add_text_overlay adds text to an image."""
        # Arrange
        image_data = b"fake_image_data"
        text = "AI Technology"
        
        # Act
        result = self.service.add_text_overlay(image_data, text)
        
        # Assert
        # For now, we just return the original image
        # In a real implementation, this would be the modified image
        assert result == image_data
    
    def test_add_text_overlay_with_empty_text(self):
        """Test that add_text_overlay handles empty text."""
        # Arrange
        image_data = b"fake_image_data"
        text = ""
        
        # Act
        result = self.service.add_text_overlay(image_data, text)
        
        # Assert
        # With empty text, we should return the original image
        assert result == image_data
    
    def test_generate_shirt_design_creates_complete_design(self):
        """Test that generate_shirt_design creates a complete shirt design."""
        # Arrange
        topic = "AI Technology"
        
        with patch.object(self.service, 'generate_image') as mock_generate, \
             patch.object(self.service, 'add_text_overlay') as mock_overlay:
            
            mock_generate.return_value = b"generated_image_data"
            mock_overlay.return_value = b"final_image_with_text"
            
            # Act
            result = self.service.generate_shirt_design(topic)
            
            # Assert
            assert result == b"final_image_with_text"
            mock_generate.assert_called_once_with(
                f"Create a t-shirt design with '{topic}' as the main theme. "
                "The design should be visually appealing and suitable for printing on a t-shirt. "
                "Include space at the top for text overlay."
            )
            mock_overlay.assert_called_once_with(b"generated_image_data", topic)
    
    @pytest.mark.integration
    def test_generate_image_integration(self):
        """Integration test for generate_image (skipped in regular test runs)."""
        # This test would actually call the real Google Gemini API in an integration test
        # For now, we'll skip it in regular test runs
        pytest.skip("Integration test - requires real Google Gemini API access")

if __name__ == '__main__':
    pytest.main([__file__])