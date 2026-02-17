from pydantic import BaseModel
from typing import Optional



class PollCreate(BaseModel):
    title: str
    option_one: str
    option_two: str
    option_three: str
    option_four: str


class PollResponse(BaseModel):
    id: int
    title: str
    option_one: str
    option_two: str
    option_three: str
    option_four: str

    class Config:
        orm_mode = True


class PollUpdate(BaseModel):
    title: Optional[str] = None
    option_one: Optional[str] = None
    option_two: Optional[str] = None
    option_three: Optional[str] = None
    option_four: Optional[str] = None