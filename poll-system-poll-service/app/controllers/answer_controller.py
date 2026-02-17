from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.answer import AnswerCreate, AnswerResponse
from app.services.answer_service import AnswerService

router = APIRouter(prefix="/polls", tags=["Answers"])
answer_service = AnswerService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/polls/{poll_id}/answers")
async def answer_poll(
    poll_id: int,
    answer: AnswerCreate,
    db: Session = Depends(get_db)
):
    return await answer_service.answer_poll(
        db,
        poll_id,
        answer.user_id,
        answer.selected_option
    )

def answer_poll(poll_id: int, answer: AnswerCreate, db: Session = Depends(get_db)):
    return answer_service.answer_poll(
        db,
        poll_id,
        answer.user_id,
        answer.selected_option
    )


@router.put("/{poll_id}/answers", response_model=AnswerResponse)
def update_answer(poll_id: int, answer: AnswerCreate, db: Session = Depends(get_db)):
    return answer_service.update_poll_answer(
        db,
        poll_id,
        answer.user_id,
        answer.selected_option
    )
@router.get("/{poll_id}/statistics")
def get_poll_statistics(poll_id: int, db: Session = Depends(get_db)):
    return answer_service.get_poll_statistics(db, poll_id)


@router.get("/users/{user_id}/answers")
def get_user_answers(user_id: int, db: Session = Depends(get_db)):
    return answer_service.get_user_answers(db, user_id)

@router.get("/statistics/all")
def get_all_polls_statistics(db: Session = Depends(get_db)):
    return answer_service.get_all_polls_with_stats(db)

@router.delete("/answers/user/{user_id}")
def delete_answers_by_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return answer_service.delete_by_user(db, user_id)