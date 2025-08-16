"""
pytest configuration file.
"""

import sys
import os

# Add the backend directory to the path so we can import our modules
backend_path = os.path.join(os.path.dirname(__file__), 'src', 'backend')
sys.path.insert(0, backend_path)

# Add a marker for integration tests
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )