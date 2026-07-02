from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {
        "message": "This message comes from inside your container using FastAPI"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }
