#!/usr/bin/env bash
set -euo pipefail

REGION="${REGION:-cn-north-4}"
ORG="${ORG:-cloud-compute-2026}"
REGISTRY="swr.${REGION}.myhuaweicloud.com/${ORG}"

docker build -t backend:v1 backend
docker build -t frontend:v1 frontend
docker tag backend:v1 "${REGISTRY}/backend:v1"
docker tag frontend:v1 "${REGISTRY}/frontend:v1"
docker push "${REGISTRY}/backend:v1"
docker push "${REGISTRY}/frontend:v1"

