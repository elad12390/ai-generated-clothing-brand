#!/bin/bash
# Script to run the main application for the AI Generated Clothing Brand project.

# Navigate to project root
cd "$(dirname "$0")"

# Activate virtual environment and run the main application
source .venv/bin/activate
echo "Running AI Generated Clothing Brand application..."
python src/backend/main.py
deactivate