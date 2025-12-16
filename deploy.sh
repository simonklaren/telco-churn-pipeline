#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$HOME/telco-churn-pipeline"

cd "$REPO_DIR"
git pull origin main

cd ml_service
docker build -t churn-api:latest .

docker stop churn-api 2>/dev/null || true
docker rm churn-api 2>/dev/null || true

docker run -d --restart=always -p 8000:8000 --name churn-api churn-api:latest
