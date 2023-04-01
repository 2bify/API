from pydantic import BaseModel, EmailStr
from pydantic.types import conint

class Video_data(BaseModel):
    video_id: str
    predicted_score: int
    #created_at: datetime
    class Config:
        orm_mode = True

class Video_Output(BaseModel):
    video_id: str
    predicted_score: int
    no_of_comments: int
    p_comments: int