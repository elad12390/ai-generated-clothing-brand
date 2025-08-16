"""
Test suite for content filter functionality.
"""

import pytest
import sys
import os

# Add the backend directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.content_filter import ContentFilter

class TestContentFilter:
    """Test cases for the ContentFilter class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.filter = ContentFilter()
    
    def test_is_appropriate_with_appropriate_content(self):
        """Test that appropriate content is marked as appropriate."""
        # Arrange
        appropriate_texts = [
            "AI Technology",
            "Machine Learning",
            "Python Programming",
            "Data Science",
            "Web Development"
        ]
        
        # Act & Assert
        for text in appropriate_texts:
            assert self.filter.is_appropriate(text) == True, f"Text '{text}' should be appropriate"
    
    def test_is_appropriate_with_inappropriate_content(self):
        """Test that inappropriate content is marked as inappropriate."""
        # Arrange
        inappropriate_texts = [
            "Violent Content",
            "Offensive Language",
            "Inappropriate Material",
            "NSFW Topics"
        ]
        
        # Act & Assert
        for text in inappropriate_texts:
            assert self.filter.is_appropriate(text) == False, f"Text '{text}' should be inappropriate"
    
    def test_is_appropriate_with_empty_content(self):
        """Test that empty content is considered appropriate."""
        # Act
        result = self.filter.is_appropriate("")
        
        # Assert
        assert result == True
    
    def test_is_appropriate_with_none_content(self):
        """Test that None content is considered appropriate."""
        # Act
        result = self.filter.is_appropriate(None)
        
        # Assert
        assert result == True
    
    def test_filter_text_with_appropriate_content(self):
        """Test that appropriate content is not filtered."""
        # Arrange
        text = "AI Technology"
        
        # Act
        filtered_text = self.filter.filter_text(text)
        
        # Assert
        assert filtered_text == text
    
    def test_filter_text_with_inappropriate_content(self):
        """Test that inappropriate content is filtered."""
        # Arrange
        text = "Violent Content"
        
        # Act
        filtered_text = self.filter.filter_text(text)
        
        # Assert
        assert filtered_text == "[FILTERED]"

if __name__ == '__main__':
    pytest.main([__file__])