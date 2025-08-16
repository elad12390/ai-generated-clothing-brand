#!/bin/bash
# Setup script for AI Generated Clothing Brand cron job

echo "Setting up daily cron job for AI Generated Clothing Brand..."

# Get current directory
PROJECT_DIR=$(pwd)

# Create logs directory if it doesn't exist
mkdir -p logs

# Add cron job to run daily at 9 AM
(crontab -l 2>/dev/null; echo "0 9 * * * cd $PROJECT_DIR && /usr/bin/python3 src/main.py") | crontab -

echo "Cron job set up successfully!"
echo "The script will run daily at 9 AM."
echo "Check logs/app.log for execution details."