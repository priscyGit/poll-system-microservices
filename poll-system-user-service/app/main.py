from fastapi import FastAPI
from app.controllers.user_controller import router as user_router

app = FastAPI(title="User Service")

app.include_router(user_router)


@app.get("/health")
def health_check():
    return {"status": "User service is running"}
