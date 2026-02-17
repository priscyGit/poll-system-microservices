from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship


class Poll(Base):
    __tablename__ = "polls"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    option_one = Column(String(255), nullable=False)
    option_two = Column(String(255), nullable=False)
    option_three = Column(String(255), nullable=False)
    option_four = Column(String(255), nullable=False)
    
    answers = relationship("Answer", backref = "poll", cascade = "all, delete", passive_deletes = True)

