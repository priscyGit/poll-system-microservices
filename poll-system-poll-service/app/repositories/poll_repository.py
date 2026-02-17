from sqlalchemy.orm import Session
from app.models.poll import Poll
from app.schemas.poll import PollCreate


class PollRepository:

    def create_poll(self, db: Session, poll: PollCreate):
        new_poll = Poll(
            title=poll.title,
            option_one=poll.option_one,
            option_two=poll.option_two,
            option_three=poll.option_three,
            option_four=poll.option_four
        )
        db.add(new_poll)
        db.commit()
        db.refresh(new_poll)
        return new_poll

    def get_poll_by_id(self, db: Session, poll_id: int):
        return db.query(Poll).filter(Poll.id == poll_id).first()

    def get_all_polls(self, db: Session):
        return db.query(Poll).all()

    def delete_poll(self, db: Session, poll_id: int):
        db.query(Poll).filter(Poll.id == poll_id).delete()
        db.commit()
