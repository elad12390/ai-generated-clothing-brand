#!/bin/bash
# Script to run tests for the AI Generated Clothing Brand project.

# Navigate to project root
cd "$(dirname "$0")"/..

# Activate virtual environment and run tests
source .venv/bin/activate
echo "Running tests..."
python -m pytest src/backend/tests/ -v
deactivate