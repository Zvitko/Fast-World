# Fast-World

A small FastAPI app running on a self-hosted Kubernetes cluster.

---

## Endpoints

```
GET /         → {"application": "Fast World"}
GET /fast     → message from inside the container
GET /health   → health check
```

---

## What's running under the hood

- **FastAPI** on Python 3.12
- **Docker** image stored in a local registry
- **Kubernetes** via kubeadm on bare metal (1 control plane, 2 workers)
- **Envoy Gateway** for HTTP routing
- **Prometheus + Grafana** for cluster monitoring
- **MetalLB** for load balancing on-prem

---

## Project structure

```
Fast-World/
├── app.py
├── Dockerfile
├── requirements.txt
└── k8s/
    ├── apps/
    │   └── fast-api/         # deployment, service, gateway, httproute
    └── platform/
        ├── gateway/          # gatewayclass
        └── monitoring/       # prometheus + grafana helm values
```

---
