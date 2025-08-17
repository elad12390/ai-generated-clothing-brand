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
    # Google Generative AI import should raise if missing
    print("✓ Google Generative AI package imported successfully")
    
    # Test requests
    # Verify requests can perform a simple GET
    response = requests.get("https://httpbin.org/get", timeout=5)
    assert response.status_code == 200, f"Requests returned {response.status_code}"
    print("✓ Requests package working correctly")
    
    # Test dotenv
    load_dotenv()
    print("✓ Python-dotenv package working correctly")
    
    print("\nAll tests passed! Development environment is ready.")

if __name__ == "__main__":
    if test_environment():
        print("\nYou're ready to start implementing the AI Generated Clothing Brand project!")
        sys.exit(0)
    else:
        print("\nThere were issues with the environment setup. Please check the errors above.")
        sys.exit(1)