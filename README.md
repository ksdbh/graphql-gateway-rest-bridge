# GraphQL Gateway over REST Microservices
[![CI](https://github.com/ksdbh/graphql-gateway-rest-bridge/actions/workflows/ci.yml/badge.svg)](https://github.com/ksdbh/graphql-gateway-rest-bridge/actions/workflows/ci.yml)

A small **GraphQL** gateway (FastAPI + Strawberry) that stitches data from REST services (JSONPlaceholder by default).
Includes JWT auth stub, correlation IDs, Dockerfile, CI, and Kubernetes manifests with health/readiness probes.

## Features
- GraphQL endpoint at `/graphql` with built-in schema docs
- REST adapters using `httpx`
- JWT auth middleware (stub) and request correlation IDs for traceability
- Health (`/health`) and readiness probes
- Dockerfile & GitHub Actions CI (lint/test/build)
- K8s manifests with probes and basic resource limits

## Quickstart (local)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# http://localhost:8000/health
# http://localhost:8000/graphql
```

### Example GraphQL Query
```graphql
query {
  post(id: 1) { id title author { id name } }
  posts(limit: 3) { id title }
}
```

## Configuration
Defaults live in `app/settings.py`. You can override via environment variables:
- `JWT_SECRET` — HMAC secret used by the JWT middleware (dev default: `change-me`)
- To point at a different REST backend, change `rest_base_url` in `app/settings.py`

## Docker
```bash
docker build -t gql-gateway:dev .
docker run -p 8000:8000 -e JWT_SECRET=dev gql-gateway:dev
```

## Kubernetes (kind/minikube)
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods -l app=gql-gateway
```

## Tests
```bash
pytest -q
```

## License
This project is licensed under the MIT License — see `LICENSE`.
