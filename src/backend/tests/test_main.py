"""
Test suite for main application functionality.
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the backend directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import main

class TestMainApplication:
    """Test cases for the main application."""
    
    @patch('main.get_trending_topic')
    @patch('main.generate_shirt_design')
    @patch('main.upload_to_printful')
    def test_main_success(self, mock_upload, mock_generate, mock_get_topic):
        """Test that main function completes successfully when all steps succeed."""
        # Arrange
        mock_get_topic.return_value = "AI Technology"
        mock_generate.return_value = "design.png"
        mock_upload.return_value = True
        
        # Act & Assert
        # This should not raise an exception
        main.main()
        
        # Verify that all functions were called
        mock_get_topic.assert_called_once()
        mock_generate.assert_called_once_with("AI Technology")
        mock_upload.assert_called_once_with("design.png", "AI Technology")
    
    @patch('main.get_trending_topic')
    def test_main_with_exception(self, mock_get_topic):
        """Test that main function handles exceptions properly."""
        # Arrange
        mock_get_topic.side_effect = Exception("API Error")
        
        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            main.main()
        
        assert str(exc_info.value) == "API Error"
    
    def test_get_trending_topic_with_appropriate_content(self):
        """Test get_trending_topic with appropriate content."""
        # This test actually uses our real service
        with patch('main.TrendingTopicService') as mock_service_class:
            mock_service = MagicMock()
            mock_service.get_trending_topics.return_value = [
                {'title': 'AI Technology', 'score': 95},
                {'title': 'Machine Learning', 'score': 87}
            ]
            mock_service.filter_topics.return_value = [
                {'title': 'AI Technology', 'score': 95},
                {'title': 'Machine Learning', 'score': 87}
            ]
            mock_service.select_best_topic.return_value = {'title': 'AI Technology', 'score': 95}
            mock_service_class.return_value = mock_service
            
            # Act
            result = main.get_trending_topic()
            
            # Assert
            assert result == "AI Technology"
    
    def test_get_trending_topic_with_no_appropriate_content(self):
        """Test get_trending_topic when no appropriate content is found."""
        # This test actually uses our real service
        with patch('main.TrendingTopicService') as mock_service_class:
            mock_service = MagicMock()
            mock_service.get_trending_topics.return_value = [
                {'title': 'Inappropriate Content', 'score': 95}
            ]
            mock_service.filter_topics.return_value = []  # All filtered out
            mock_service_class.return_value = mock_service
            
            # Act
            result = main.get_trending_topic()
            
            # Assert
            assert result == "AI Generated Clothing"  # Default fallback

if __name__ == '__main__':
    pytest.main([__file__])