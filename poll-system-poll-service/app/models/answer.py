from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from app.database import Base


class Answer(Base):
    __tablename__ = "answers"

    __table_args__ = (
        UniqueConstraint("user_id", "poll_id", name="unique_user_poll"),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    poll_id = Column(Integer, ForeignKey("polls.id", ondelete="CASCADE"), nullable=False)
    selected_option = Column(Integer, nullable=False)
    
