from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.answer_repository import AnswerRepository
from app.repositories.poll_repository import PollRepository


class AnswerService:

    def __init__(self):
        self.answer_repository = AnswerRepository()
        self.poll_repository = PollRepository()

    # ---------- CREATE ANSWER ----------
    def create_answer(
        self,
        db: Session,
        user_id: int,
        poll_id: int,
        selected_option: int
    ):
        return self.answer_repository.create_answer(
            db, user_id, poll_id, selected_option
        )

    # ---------- GET USER ANSWER FOR POLL ----------
    def get_user_answer_for_poll(
        self,
        db: Session,
        user_id: int,
        poll_id: int
    ):
        return self.answer_repository.get_user_answer_for_poll(
            db, user_id, poll_id
        )

    # ---------- ANSWER POLL (POST) ----------
    def answer_poll(
        self,
        db: Session,
        poll_id: int,
        user_id: int,
        selected_option: int
    ):
        existing_answer = self.get_user_answer_for_poll(
            db, user_id, poll_id
        )

        # if user already answered → update
        if existing_answer:
            return self.answer_repository.update_answer(
                db, existing_answer, selected_option
            )

        return self.create_answer(
            db, user_id, poll_id, selected_option
        )

    # ---------- UPDATE ANSWER (PUT) ----------
    def update_poll_answer(
        self,
        db: Session,
        poll_id: int,
        user_id: int,
        selected_option: int
    ):
        existing_answer = self.get_user_answer_for_poll(
            db, user_id, poll_id
        )

        if not existing_answer:
            raise HTTPException(
                status_code=404,
                detail="Answer not found"
            )

        return self.answer_repository.update_answer(
            db, existing_answer, selected_option
        )

    # ---------- POLL STATISTICS ----------
    def get_poll_statistics(self, db: Session, poll_id: int):

        poll = self.poll_repository.get_poll_by_id(db, poll_id)

        if not poll:
            raise HTTPException(status_code=404, detail="Poll not found")

        option_counts = self.answer_repository.count_answers_by_option(
            db, poll_id
        )

        total_answers = self.answer_repository.count_total_answers_for_poll(
            db, poll_id
        )

        return {
            "poll_id": poll_id,
            "total_answers": total_answers,
            "option_one": option_counts[1],
            "option_two": option_counts[2],
            "option_three": option_counts[3],
            "option_four": option_counts[4],
        }

    # ---------- USER ANSWERS ----------
    def get_user_answers(self, db: Session, user_id: int):

        answers = self.answer_repository.get_answers_by_user(
            db, user_id
        )

        return {
            "user_id": user_id,
            "total_answered": len(answers),
            "answers": [
                {
                    "poll_id": answer.poll_id,
                    "selected_option": answer.selected_option,
                }
                for answer in answers
            ],
        }

    # ---------- ALL POLLS WITH STATS ----------
    def get_all_polls_with_stats(self, db: Session):

        polls = self.poll_repository.get_all_polls(db)

        result = []

        for poll in polls:
            option_counts = self.answer_repository.count_answers_by_option(
                db, poll.id
            )

            result.append({
                "poll_id": poll.id,
                "title": poll.title,
                "option_one": poll.option_one,
                "option_two": poll.option_two,
                "option_three": poll.option_three,
                "option_four": poll.option_four,
                "stats": {
                    "option_one": option_counts[1],
                    "option_two": option_counts[2],
                    "option_three": option_counts[3],
                    "option_four": option_counts[4],
                }
            })

        return result