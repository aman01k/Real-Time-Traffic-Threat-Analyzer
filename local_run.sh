#!/bin/bash

echo "🔨 Building Docker image..."
docker build -t net-analyzer .

echo "🏃 Running container on port 8080..."
echo "Open http://localhost:8080 in your browser"
docker run -p 8080:8080 net-analyzer
