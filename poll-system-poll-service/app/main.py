from fastapi import FastAPI
from app.controllers.poll_controller import router as poll_router
from app.controllers.answer_controller import router as answer_router
from app.models import poll, answer
from app.database import Base,engine

app = FastAPI(title="Poll Service")


app.include_router(poll_router)
app.include_router(answer_router)


@app.get("/health")
def health_check():
    return {"status": "Poll service is running"}

@app.on_event("startup")
def create_tables():
    from app.database import Base
    Base.metadata.create_all(bind=engine)
