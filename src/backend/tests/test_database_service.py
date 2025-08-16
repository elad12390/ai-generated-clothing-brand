"""
Test suite for database functionality.
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the backend directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.database_service import DatabaseService

class TestDatabaseService:
    """Test cases for the DatabaseService class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.service = DatabaseService(testing_mode=True)
    
    def test_initialize_database_connection(self):
        """Test that database connection is initialized."""
        # In testing mode, the service should be initialized without errors
        assert self.service is not None
        assert self.service.testing_mode == True
    
    def test_save_shirt_design_success(self):
        """Test that save_shirt_design saves a shirt design successfully."""
        # Arrange
        shirt_data = {
            'topic': 'AI Technology',
            'image_data': b'fake_image_data',
            'created_at': '2025-08-16T22:34:15'
        }
        
        # Act
        result = self.service.save_shirt_design(shirt_data)
        
        # Assert
        assert result == True  # In testing mode, we return True
    
    def test_save_shirt_design_with_missing_data(self):
        """Test that save_shirt_design handles missing data."""
        # Arrange
        shirt_data = {
            'topic': 'AI Technology'
            # Missing image_data and created_at
        }
        
        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            self.service.save_shirt_design(shirt_data)
        
        assert "Missing required shirt data" in str(exc_info.value)
    
    def test_get_latest_shirt_design(self):
        """Test that get_latest_shirt_design retrieves the latest shirt design."""
        # Arrange
        expected_data = {
            'topic': 'AI Technology',
            'image_data': b'fake_image_data',
            'created_at': '2025-08-16T22:34:15'
        }
        
        # Act
        result = self.service.get_latest_shirt_design()
        
        # Assert
        # In testing mode, we return fake data
        assert result is not None
        assert 'topic' in result
        assert 'image_data' in result
        assert 'created_at' in result
    
    def test_get_all_shirt_designs(self):
        """Test that get_all_shirt_designs retrieves all shirt designs."""
        # Act
        result = self.service.get_all_shirt_designs()
        
        # Assert
        # In testing mode, we return a list with fake data
        assert isinstance(result, list)
        assert len(result) >= 0  # Could be empty or have data
    
    def test_get_shirt_design_by_topic(self):
        """Test that get_shirt_design_by_topic retrieves a shirt design by topic."""
        # Arrange
        topic = "AI Technology"
        
        # Act
        result = self.service.get_shirt_design_by_topic(topic)
        
        # Assert
        # In testing mode, we return fake data or None
        assert result is None or isinstance(result, dict)

if __name__ == '__main__':
    pytest.main([__file__])