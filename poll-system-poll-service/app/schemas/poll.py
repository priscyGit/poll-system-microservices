from pydantic import BaseModel


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
