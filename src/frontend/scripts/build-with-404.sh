#!/bin/bash

# Build script for The Daily Drip frontend
# This script builds the frontend and ensures the 404 page is properly copied

echo "Building The Daily Drip frontend..."

# Run the Vite build
npm run build

# Copy the 404 page to the dist folder
cp public/404.html dist/404.html

# Copy the 404 page to dist/index.html for SPA fallback
cp public/404.html dist/index.html

echo "Build completed successfully!"
echo "The 404 page has been copied to the dist folder for proper SPA routing."