from sqlalchemy.orm import Session
from app.repositories.poll_repository import PollRepository
from app.schemas.poll import PollCreate


class PollService:

    def __init__(self):
        self.poll_repository = PollRepository()

    def create_poll(self, db: Session, poll: PollCreate):
        return self.poll_repository.create_poll(db, poll)

    def get_poll(self, db: Session, poll_id: int):
        return self.poll_repository.get_poll_by_id(db, poll_id)

    def get_all_polls(self, db: Session):
        return self.poll_repository.get_all_polls(db)
