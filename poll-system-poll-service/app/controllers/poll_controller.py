from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.poll import PollCreate, PollResponse
from app.services.poll_service import PollService

router = APIRouter(prefix="/polls", tags=["Polls"])
poll_service = PollService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/",
    response_model=PollResponse,
    status_code=status.HTTP_201_CREATED
)
def create_poll(poll: PollCreate, db: Session = Depends(get_db)):
    return poll_service.create_poll(db, poll)


@router.get("/{poll_id}", response_model=PollResponse)
def get_poll(poll_id: int, db: Session = Depends(get_db)):
    poll = poll_service.get_poll(db, poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")
    return poll


@router.get("/", response_model=list[PollResponse])
def get_all_polls(db: Session = Depends(get_db)):
    return poll_service.get_all_polls(db)
