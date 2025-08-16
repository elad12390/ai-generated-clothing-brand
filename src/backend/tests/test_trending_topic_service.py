"""
Test suite for trending topic analysis functionality.
"""

import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the backend directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.trending_topic_service import TrendingTopicService

class TestTrendingTopicService:
    """Test cases for the TrendingTopicService class."""
    
    def test_get_trending_topics_returns_list(self):
        """Test that get_trending_topics returns a list of topics."""
        # Arrange
        service = TrendingTopicService()
        
        # Act
        with patch('services.trending_topic_service.requests.get') as mock_get:
            # Mock response data
            mock_response = MagicMock()
            mock_response.json.return_value = {
                'data': [
                    {'title': 'AI Technology', 'score': 95},
                    {'title': 'Machine Learning', 'score': 87},
                    {'title': 'Python Programming', 'score': 82}
                ]
            }
            mock_get.return_value = mock_response
            
            topics = service.get_trending_topics()
        
        # Assert
        assert isinstance(topics, list)
        assert len(topics) > 0
        assert all(isinstance(topic, dict) for topic in topics)
    
    def test_select_best_topic_returns_single_topic(self):
        """Test that select_best_topic returns exactly one topic."""
        # Arrange
        service = TrendingTopicService()
        topics = [
            {'title': 'AI Technology', 'score': 95},
            {'title': 'Machine Learning', 'score': 87},
            {'title': 'Python Programming', 'score': 82}
        ]
        
        # Act
        best_topic = service.select_best_topic(topics)
        
        # Assert
        assert isinstance(best_topic, dict)
        assert 'title' in best_topic
        assert 'score' in best_topic
        assert best_topic['title'] == 'AI Technology'  # Highest score should be selected
    
    def test_filter_topics_removes_inappropriate_content(self):
        """Test that filter_topics removes inappropriate content."""
        # Arrange
        service = TrendingTopicService()
        topics = [
            {'title': 'AI Technology', 'score': 95},
            {'title': 'Inappropriate Content', 'score': 90},
            {'title': 'Machine Learning', 'score': 87},
            {'title': 'Violent Topic', 'score': 80}
        ]
        
        # Mock the content filter
        with patch.object(service, '_is_appropriate_content', side_effect=[True, False, True, False]) as mock_filter:
            # Act
            filtered_topics = service.filter_topics(topics)
        
        # Assert
        assert len(filtered_topics) == 2
        assert filtered_topics[0]['title'] == 'AI Technology'
        assert filtered_topics[1]['title'] == 'Machine Learning'
    
    @pytest.mark.integration
    def test_get_trending_topics_integration(self):
        """Integration test for get_trending_topics (skipped in regular test runs)."""
        # This test would actually call the real API in an integration test
        # For now, we'll skip it in regular test runs
        pytest.skip("Integration test - requires real API access")

if __name__ == '__main__':
    pytest.main([__file__])