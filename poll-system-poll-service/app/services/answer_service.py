from sqlalchemy.orm import Session
from app.models.answer import Answer


class AnswerService:

    def create_answer(self, db: Session, user_id: int, poll_id: int, selected_option: int):
        new_answer = Answer(
            user_id=user_id,
            poll_id=poll_id,
            selected_option=selected_option
        )
        db.add(new_answer)
        db.commit()
        db.refresh(new_answer)
        return new_answer

    def get_user_answer_for_poll(self, db: Session, user_id: int, poll_id: int):
        return db.query(Answer).filter(
            Answer.user_id == user_id,
            Answer.poll_id == poll_id
        ).first()

    def update_answer(self, db: Session, answer: Answer, selected_option: int):
        answer.selected_option = selected_option
        db.commit()
        db.refresh(answer)
        return answer

    def get_answers_for_poll(self, db: Session, poll_id: int):
        return db.query(Answer).filter(Answer.poll_id == poll_id).all()

    def get_answers_by_user(self, db: Session, user_id: int):
        return db.query(Answer).filter(Answer.user_id == user_id).all()
    def get_poll_statistics(self, db: Session, poll_id: int):
        poll = self.poll_repository.get_poll_by_id(db, poll_id)
        if not poll:
            raise HTTPException(status_code=404, detail="Poll not found")

        option_counts = self.answer_repository.count_answers_by_option(db, poll_id)
        total_answers = self.answer_repository.count_total_answers_for_poll(db, poll_id)

        return {
            "poll_id": poll_id,
            "total_answers": total_answers,
            "option_one": option_counts[1],
            "option_two": option_counts[2],
            "option_three": option_counts[3],
            "option_four": option_counts[4],
        }

    def get_user_answers(self, db: Session, user_id: int):
        answers = self.answer_repository.get_answers_by_user(db, user_id)

        return {
            "user_id": user_id,
            "total_answered": len(answers),
            "answers": [
                {
                    "poll_id": answer.poll_id,
                    "selected_option": answer.selected_option
                }
                for answer in answers
            ]
        }

    def get_all_polls_with_stats(self, db: Session):
        polls = self.poll_repository.get_all_polls(db)

        result = []

        for poll in polls:
            option_counts = self.answer_repository.count_answers_by_option(db, poll.id)

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
