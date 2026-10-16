from fastapi import FastAPI

app = FastAPI(
    title="TechApp API",
    description="API criada para o laboratório de DevOps e CI/CD",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {
        "application": "TechApp API",
        "message": "API funcionando",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
