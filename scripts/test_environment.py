#!/usr/bin/env python3
"""
Test script to verify the development environment setup.
"""

import sys
import google.generativeai as genai
import requests
from dotenv import load_dotenv
import os

def test_environment():
    """Test that all required packages are available and working."""
    print("Testing development environment setup...")
    
    # Test Google Generative AI
    try:
        print("✓ Google Generative AI package imported successfully")
    except Exception as e:
        print(f"✗ Failed to import Google Generative AI: {e}")
        return False
    
    # Test requests
    try:
        response = requests.get("https://httpbin.org/get", timeout=5)
        if response.status_code == 200:
            print("✓ Requests package working correctly")
        else:
            print(f"✗ Requests package returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Failed to make HTTP request: {e}")
        return False
    
    # Test dotenv
    try:
        load_dotenv()
        print("✓ Python-dotenv package working correctly")
    except Exception as e:
        print(f"✗ Failed to load dotenv: {e}")
        return False
    
    print("\nAll tests passed! Development environment is ready.")
    return True

if __name__ == "__main__":
    if test_environment():
        print("\nYou're ready to start implementing the AI Generated Clothing Brand project!")
        sys.exit(0)
    else:
        print("\nThere were issues with the environment setup. Please check the errors above.")
        sys.exit(1)