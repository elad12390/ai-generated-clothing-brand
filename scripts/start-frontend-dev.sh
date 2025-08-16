#!/bin/bash

# Script to start the frontend development server in the background

# Navigate to the frontend directory
cd /home/eladbenhaim/dev/ai-generated-clothing-brand/src/frontend

# Start the development server in the background
npm run dev &

# Save the process ID
echo $! > /tmp/frontend-server.pid

echo "Frontend development server started in the background"
echo "PID: $(cat /tmp/frontend-server.pid)"
echo "Visit http://localhost:5173 to view the application"
echo "To stop the server, run: kill $(cat /tmp/frontend-server.pid)"