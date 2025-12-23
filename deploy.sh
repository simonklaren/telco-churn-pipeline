#!/usr/bin/env bash
set -euo pipefail

# Absolute pad naar directory van dit script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$SCRIPT_DIR"

echo "Deploying from: $REPO_DIR"

cd "$REPO_DIR"

git pull origin main

cd ml_service

docker build -t churn-api:latest .

docker stop churn-api 2>/dev/null || true
docker rm churn-api 2>/dev/null || true

docker run -d \
  --name churn-api \
  --restart unless-stopped \
  -p 8000:8000 \
  churn-api:latest
