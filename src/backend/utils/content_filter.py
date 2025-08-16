"""
Content Filter utility for AI Generated Clothing Brand.
Handles filtering of inappropriate content for shirt designs.
"""

import re
import logging

class ContentFilter:
    """Utility class for filtering inappropriate content."""
    
    def __init__(self):
        """Initialize the ContentFilter."""
        self.logger = logging.getLogger(__name__)
        # Define inappropriate keywords (this would be more comprehensive in reality)
        self.inappropriate_keywords = {
            'violent', 'offensive', 'inappropriate', 'nsfw', 'explicit',
            'hate', 'discriminatory', 'profanity', 'obscene'
        }
        
        # Compile regex patterns for better performance
        self.keyword_pattern = re.compile(
            r'\b(' + '|'.join(self.inappropriate_keywords) + r')\b',
            re.IGNORECASE
        )
    
    def is_appropriate(self, text: str) -> bool:
        """
        Check if text is appropriate for shirt designs.
        
        Args:
            text (str): Text to check
            
        Returns:
            bool: True if content is appropriate, False otherwise
        """
        if not text:
            return True
            
        # Check for inappropriate keywords
        if self.keyword_pattern.search(text):
            self.logger.warning(f"Inappropriate content detected: {text}")
            return False
            
        # Additional checks could be added here
        # For example, checking for excessive special characters, etc.
        
        return True
    
    def filter_text(self, text: str) -> str:
        """
        Filter inappropriate content from text.
        
        Args:
            text (str): Text to filter
            
        Returns:
            str: Filtered text with inappropriate content removed or replaced
        """
        if not text:
            return text
            
        # For now, we'll just return the original text if it's appropriate
        # In a more sophisticated implementation, we might replace inappropriate
        # content with placeholders or remove it entirely
        if self.is_appropriate(text):
            return text
        else:
            # In a real implementation, we might want to handle this differently
            # For now, we'll just log and return a placeholder
            self.logger.warning(f"Filtering inappropriate text: {text}")
            return "[FILTERED]"