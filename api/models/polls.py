from enum import Enum
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

class QuestionType(str, Enum):
    THOUGHT = "thought" # open-ended, user describes their thoughts on a topic
    STANCE = "stance" # close-ended, user takes a side on a topic

class Poll(BaseModel):
    id: str
    question: str
    questionType: QuestionType
    options: List[PollOption]
    answers: List[PollAnswer] = []
    isTextBased: bool = False
    createdAt: datetime
