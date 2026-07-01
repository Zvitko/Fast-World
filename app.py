from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"application": "Fast World"}

@app.get("/fast")
def fast():
    return {
        "message": "This message comes from inside your container using FastAPI"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
