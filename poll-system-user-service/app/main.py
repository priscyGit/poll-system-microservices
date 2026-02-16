from fastapi import FastAPI
from app.controllers.user_controller import router as user_router


from app.database import Base, engine
from app.models import user 

app = FastAPI(title="User Service")

app.include_router(user_router)


@app.get("/health")
def health_check():
    return {"status": "User service is running"}



@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)
