"""
Test suite for Printful integration functionality.
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the backend directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.printful_service import PrintfulService

class TestPrintfulService:
    """Test cases for the PrintfulService class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.service = PrintfulService(testing_mode=True)
    
    def test_initialize_printful_service(self):
        """Test that Printful service is initialized."""
        # In testing mode, the service should be initialized without errors
        assert self.service is not None
        assert self.service.testing_mode == True
    
    def test_create_product_success(self):
        """Test that create_product creates a product successfully."""
        # Arrange
        product_data = {
            'name': 'AI Technology Shirt',
            'description': 'A shirt featuring AI Technology design',
            'image_url': 'https://example.com/design.png',
            'topic': 'AI Technology'
        }
        
        # Act
        result = self.service.create_product(product_data)
        
        # Assert
        assert result is not None
        assert isinstance(result, dict)
        # In testing mode, we return fake data with a product ID
        assert 'product_id' in result
        assert 'status' in result
        
    def test_create_product_with_missing_data(self):
        """Test that create_product handles missing data."""
        # Arrange
        product_data = {
            'name': 'AI Technology Shirt'
            # Missing description, image_url, and topic
        }
        
        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            self.service.create_product(product_data)
        
        assert "Missing required product data" in str(exc_info.value)
    
    def test_upload_design_success(self):
        """Test that upload_design uploads a design successfully."""
        # Arrange
        design_data = b"fake_image_data"
        product_id = "test_product_123"
        
        # Act
        result = self.service.upload_design(design_data, product_id)
        
        # Assert
        assert result == True  # In testing mode, we return True
    
    def test_upload_design_with_empty_data(self):
        """Test that upload_design handles empty data."""
        # Arrange
        design_data = b""
        product_id = "test_product_123"
        
        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            self.service.upload_design(design_data, product_id)
        
        assert "Design data cannot be empty" in str(exc_info.value)
    
    def test_get_product_status(self):
        """Test that get_product_status retrieves product status."""
        # Arrange
        product_id = "test_product_123"
        
        # Act
        result = self.service.get_product_status(product_id)
        
        # Assert
        # In testing mode, we return fake status data
        assert result is not None
        assert isinstance(result, dict)
        assert 'status' in result
        assert 'product_id' in result
    
    def test_handle_api_error(self):
        """Test that handle_api_error processes API errors."""
        # Arrange
        error_response = {
            'error': 'API limit exceeded',
            'code': 429
        }
        
        # Act
        result = self.service.handle_api_error(error_response)
        
        # Assert
        # In testing mode, we just log the error and return False
        assert result == False
    
    def test_rate_limiting(self):
        """Test that rate limiting is implemented."""
        # Arrange
        # This would test that we respect rate limits
        # For now, we'll just check that the service has rate limiting attributes
        assert hasattr(self.service, '_last_request_time')
        assert hasattr(self.service, '_min_request_interval')

if __name__ == '__main__':
    pytest.main([__file__])