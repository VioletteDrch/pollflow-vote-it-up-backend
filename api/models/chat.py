from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class Message(BaseModel):
    id: str
    content: str
    sender: Literal["user", "ai"]
    timestamp: datetime

class ChatRequest(BaseModel):
    question: str
    message: str

class ChatResponse(BaseModel):
    response: str

class SummaryRequest(BaseModel):
    question: str
    messages: list[Message]

class SummaryResponse(BaseModel):
    summary: str