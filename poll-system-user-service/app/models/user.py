from sqlalchemy import Column, Integer, String, Boolean, Date
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)
    joining_date = Column(Date, nullable=False)
    is_registered = Column(Boolean, default=False)
