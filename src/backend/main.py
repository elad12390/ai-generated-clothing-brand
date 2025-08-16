#!/usr/bin/env python3
"""
Main script for AI Generated Clothing Brand.
Automatically generates one trending shirt per day.
"""

import os
import sys
import logging
from dotenv import load_dotenv
from datetime import datetime

# Add the backend directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(__file__))

from services.trending_topic_service import TrendingTopicService
from services.ai_design_service import AIDesignService
from services.database_service import DatabaseService
from services.printful_service import PrintfulService

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_trending_topic():
    """Fetch trending topic from API."""
    logging.info("Fetching trending topic...")
    
    # Use our new TrendingTopicService
    service = TrendingTopicService()
    
    # Get trending topics
    topics = service.get_trending_topics()
    
    # Filter inappropriate topics
    filtered_topics = service.filter_topics(topics)
    
    # Select the best topic
    if filtered_topics:
        best_topic = service.select_best_topic(filtered_topics)
        logging.info(f"Selected topic: {best_topic['title']}")
        return best_topic['title']
    else:
        logging.warning("No appropriate topics found, using default")
        return "AI Generated Clothing"

def generate_shirt_design(topic):
    """Generate shirt design using AI."""
    logging.info(f"Generating shirt design for topic: {topic}")
    
    # Use our new AIDesignService
    service = AIDesignService()  # Remove testing_mode=True to use real API
    
    try:
        # Generate the shirt design
        design_data = service.generate_shirt_design(topic)
        
        # Save the design data to database
        db_service = DatabaseService()  # Remove testing_mode=True to use real database
        shirt_data = {
            'topic': topic,
            'image_data': design_data,
            'created_at': datetime.now().isoformat()
        }
        db_service.save_shirt_design(shirt_data)
        
        # For now, we'll just return a placeholder path
        # In a real implementation, we would save the image to a file
        logging.info("Shirt design generated and saved successfully")
        return "design.png"  # Placeholder - in real implementation this would be the actual file path
    except Exception as e:
        logging.error(f"Error generating shirt design: {str(e)}")
        raise

def upload_to_printful(design_path, topic):
    """Upload design to Printful."""
    logging.info(f"Uploading design {design_path} for topic: {topic}")
    
    # Use our new PrintfulService
    service = PrintfulService()
    
    try:
        # Create a product in Printful
        product_data = {
            'name': f"{topic} Shirt",
            'description': f"Exclusive {topic} design shirt",
            'image_url': f"https://example.com/{design_path}",  # Placeholder URL
            'topic': topic
        }
        product_info = service.create_product(product_data)
        
        # Upload the design to the product
        # In a real implementation, we would read the actual image file
        design_data = b"fake_image_data"  # Placeholder
        success = service.upload_design(design_data, product_info['product_id'])
        
        if success:
            logging.info(f"Design uploaded successfully to product {product_info['product_id']}")
            return True
        else:
            logging.error("Failed to upload design to Printful")
            return False
            
    except Exception as e:
        logging.error(f"Error uploading to Printful: {str(e)}")
        return False

def main():
    """Main execution function."""
    try:
        logging.info("Starting daily shirt generation...")
        
        # Get trending topic
        topic = get_trending_topic()
        
        # Generate shirt design
        design_path = generate_shirt_design(topic)
        
        # Upload to Printful
        success = upload_to_printful(design_path, topic)
        
        if success:
            logging.info("Daily shirt generation completed successfully!")
        else:
            logging.error("Failed to upload design to Printful")
            
    except Exception as e:
        logging.error(f"Error in daily shirt generation: {str(e)}")
        raise

if __name__ == "__main__":
    main()