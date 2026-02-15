from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    poll_id = Column(Integer, ForeignKey("polls.id"), nullable=False)
    selected_option = Column(Integer, nullable=False)
