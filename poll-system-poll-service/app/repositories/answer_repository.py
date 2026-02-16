from sqlalchemy.orm import Session
from app.models.answer import Answer


class AnswerRepository:

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
    
    def count_answers_by_option(self, db: Session, poll_id: int):
        answers = self.get_answers_for_poll(db, poll_id)

        stats = {1: 0, 2: 0, 3: 0, 4: 0}

        for answer in answers:
            stats[answer.selected_option] += 1

        return stats

    def count_total_answers_for_poll(self, db: Session, poll_id: int):
        return len(self.get_answers_for_poll(db, poll_id))

    def count_total_answers_by_user(self, db: Session, user_id: int):
        return len(self.get_answers_by_user(db, user_id))
