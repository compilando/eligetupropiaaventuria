#!/bin/bash

# Set the URL for the application
APP_URL="http://localhost:3000" # Or whatever port your app uses

# Check if Node.js and npm are installed
if ! command -v node &> /dev/null; then
  echo "Error: Node.js is not installed. Please install it and try again."
  exit 1
fi

if ! command -v npm &> /dev/null; then
  echo "Error: npm is not installed. Please ensure Node.js is installed correctly."
  exit 1
fi

# Change to the project directory
cd "$(dirname "$0")" || exit

# Install dependencies if they don't exist (or consider a separate script for this)
if [ ! -d "node_modules" ]; then
  echo "Installing project dependencies..."
  npm install
fi


# Run the development server
npm run dev &

# Wait a few seconds for the server to start (adjust as needed)
sleep 5

# Open the URL in the default browser
if command -v xdg-open &> /dev/null; then
  xdg-open "$APP_URL" &
elif command -v open &> /dev/null; then
  open "$APP_URL" &
elif command -v start &> /dev/null; then #for Windows
    start "$APP_URL"
else
  echo "Could not open a browser automatically. Please open $APP_URL manually."
fi


# Keep the script running until the server is terminated (Ctrl+C)
# Alternatively,  if you want the script to exit after opening the browser, remove this while loop.
while true; do sleep 1; done

