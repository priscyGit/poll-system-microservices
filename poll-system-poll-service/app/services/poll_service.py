from sqlalchemy.orm import Session
from app.repositories.poll_repository import PollRepository
from app.schemas.poll import PollCreate
from fastapi import HTTPException, status




class PollService:

    def __init__(self):
        self.poll_repository = PollRepository()

    def create_poll(self, db: Session, poll: PollCreate):
        return self.poll_repository.create_poll(db, poll)

    def get_poll(self, db: Session, poll_id: int):
        return self.poll_repository.get_poll_by_id(db, poll_id)

    def get_all_polls(self, db: Session):
        return self.poll_repository.get_all_polls(db)

    def delete_poll(self, db: Session, poll_id: int):
        poll = self.poll_repository.get_poll_by_id(db, poll_id)

        if not poll:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Poll not found"
            )

        self.poll_repository.delete_poll(db, poll_id)

        return {"message": "Poll deleted successfully"}

    from fastapi import HTTPException, status

    def update_poll(self, db: Session, poll_id: int, poll_update):
        poll = self.poll_repository.get_poll_by_id(db, poll_id)

        if not poll:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Poll not found"
            )

        # Update only provided fields
        if poll_update.title is not None:
            poll.title = poll_update.title
        if poll_update.option_one is not None:
            poll.option_one = poll_update.option_one
        if poll_update.option_two is not None:
            poll.option_two = poll_update.option_two
        if poll_update.option_three is not None:
            poll.option_three = poll_update.option_three
        if poll_update.option_four is not None:
            poll.option_four = poll_update.option_four

        db.commit()
        db.refresh(poll)

        return poll
