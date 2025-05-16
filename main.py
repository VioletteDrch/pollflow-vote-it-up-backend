from fastapi import FastAPI, HTTPException
from typing import List, Optional
from uuid import uuid4
from datetime import datetime, UTC
from fastapi.middleware.cors import CORSMiddleware
from models import Poll, PollOption, PollAnswer
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # or DEBUG for more detail
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Allow frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory DB
polls = {}


# Endpoints
@app.get("/api/polls", response_model=List[Poll])
def get_polls():
    return list(polls.values())

@app.get("/api/polls/{poll_id}", response_model=Poll)
def get_poll(poll_id: str):
    if poll_id not in polls:
        raise HTTPException(status_code=404, detail="Poll not found")
    print(polls[poll_id])
    return polls[poll_id]

@app.post("/api/polls", response_model=Poll)
def create_poll(data: dict):
    poll_id = str(uuid4())
    new_poll = Poll(
        id=poll_id,
        question=data["question"],
        options=[PollOption(id=str(uuid4()), text=opt) for opt in data["options"]],
        isTextBased=data.get("isTextBased", False),
        createdAt=datetime.now(UTC)
    )
    logger.info(f"Creating new poll with ID: {poll_id}")
    polls[poll_id] = new_poll
    return new_poll

@app.put("/api/polls/{poll_id}/vote", response_model=Poll)
def vote_poll(poll_id: str, vote_data: dict):
    option_id = vote_data["optionId"]
    poll = polls.get(poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")
    for option in poll.options:
        if option.id == option_id:
            option.votes += 1
            return poll
    raise HTTPException(status_code=404, detail="Option not found")

@app.post("/api/polls/{poll_id}/answer", response_model=Poll)
def submit_answer(poll_id: str, answer_data: dict):
    poll = polls.get(poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")
    new_answer = PollAnswer(
        id=str(uuid4()),
        text=answer_data["text"],
        createdAt=datetime.now(UTC)
    )
    poll.answers.append(new_answer)
    return poll
