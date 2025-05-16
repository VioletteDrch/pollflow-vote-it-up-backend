
from pydantic import BaseModel
from typing import List
from datetime import datetime

# Models
class PollOption(BaseModel):
    id: str
    text: str
    votes: int = 0

class PollAnswer(BaseModel):
    id: str
    text: str
    createdAt: datetime

class Poll(BaseModel):
    id: str
    question: str
    options: List[PollOption]
    answers: List[PollAnswer] = []
    isTextBased: bool = False
    createdAt: datetime