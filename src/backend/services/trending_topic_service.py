"""
Trending Topic Service for AI Generated Clothing Brand.
Handles fetching, filtering, and selecting trending topics for shirt designs.
"""

import requests
import logging
from typing import List, Dict, Optional
from utils.content_filter import ContentFilter

class TrendingTopicService:
    """Service for handling trending topic analysis."""
    
    def __init__(self):
        """Initialize the TrendingTopicService."""
        self.logger = logging.getLogger(__name__)
        self.content_filter = ContentFilter()
        # TODO: Load API keys from environment variables
        self.api_key = None
        self.api_endpoint = None
    
    def get_trending_topics(self) -> List[Dict]:
        """
        Fetch trending topics from external API.
        
        Returns:
            List[Dict]: List of trending topics with title and score
        """
        self.logger.info("Fetching trending topics...")
        
        # TODO: Implement actual API call to trending topics service
        # For now, return mock data for testing
        mock_topics = [
            {'title': 'AI Technology', 'score': 95},
            {'title': 'Machine Learning', 'score': 87},
            {'title': 'Python Programming', 'score': 82},
            {'title': 'Data Science', 'score': 78}
        ]
        
        return mock_topics
    
    def filter_topics(self, topics: List[Dict]) -> List[Dict]:
        """
        Filter out inappropriate topics for shirt designs.
        
        Args:
            topics (List[Dict]): List of topics to filter
            
        Returns:
            List[Dict]: Filtered list of appropriate topics
        """
        self.logger.info(f"Filtering {len(topics)} topics...")
        
        filtered_topics = []
        for topic in topics:
            if self._is_appropriate_content(topic['title']):
                filtered_topics.append(topic)
        
        self.logger.info(f"Filtered topics: {len(topics)} -> {len(filtered_topics)}")
        return filtered_topics
    
    def select_best_topic(self, topics: List[Dict]) -> Dict:
        """
        Select the best topic based on score.
        
        Args:
            topics (List[Dict]): List of topics to select from
            
        Returns:
            Dict: The highest scoring topic
        """
        if not topics:
            raise ValueError("No topics provided for selection")
        
        # Sort by score (descending) and return the top topic
        best_topic = sorted(topics, key=lambda x: x['score'], reverse=True)[0]
        self.logger.info(f"Selected best topic: {best_topic['title']} (score: {best_topic['score']})")
        
        return best_topic
    
    def _is_appropriate_content(self, content: str) -> bool:
        """
        Check if content is appropriate for shirt designs.
        
        Args:
            content (str): Content to check
            
        Returns:
            bool: True if content is appropriate, False otherwise
        """
        # For now, use a simple check
        # In reality, this would use a more sophisticated content filtering system
        inappropriate_keywords = ['inappropriate', 'violent', 'offensive']
        content_lower = content.lower()
        
        for keyword in inappropriate_keywords:
            if keyword in content_lower:
                return False
        
        return True