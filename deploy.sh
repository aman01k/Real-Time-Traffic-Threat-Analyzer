#!/bin/bash

# Configuration
APP_NAME="net-analyzer"
REGION="us-central1" # You can change this to your preferred region

echo "🚀 Deploying $APP_NAME to Google Cloud Run..."

# Submit the build to Cloud Build
gcloud builds submit --tag gcr.io/$(gcloud config get-value project)/$APP_NAME

# Deploy to Cloud Run
gcloud run deploy $APP_NAME \
  --image gcr.io/$(gcloud config get-value project)/$APP_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated

echo "✅ Deployment complete!"
