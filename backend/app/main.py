from fastapi import FastAPI

app = FastAPI(
    title="VulnOps AI",
    description="AI-powered vulnerability operations and security scanning platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "VulnOps AI",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
