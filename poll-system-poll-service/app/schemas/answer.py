from pydantic import BaseModel, Field


class AnswerCreate(BaseModel):
    user_id: int
    selected_option: int = Field(..., ge=1, le=4)


class AnswerResponse(BaseModel):
    id: int
    user_id: int
    poll_id: int
    selected_option: int

    class Config:
        orm_mode = True
