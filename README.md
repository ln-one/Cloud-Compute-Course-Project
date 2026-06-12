# Cloud Computing Course Project

Student: 2023112573 张春冉

Team: 张春冉, 邓苏鑫

This repository contains the course project scaffold for:

- Part 1: Flask + Redis + Nginx on Huawei Cloud CCE
- Part 2: MPI numerical integration on Kubernetes

## Local Check

```bash
docker compose up --build
curl http://localhost:8080/api/ping
python3 -m unittest discover -s backend/tests
```

## Cloud Deploy

Replace image placeholders if needed, then:

```bash
kubectl apply -f k8s/
kubectl get pods -o wide
kubectl get svc
```

