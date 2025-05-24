from fastapi import APIRouter, HTTPException, logger
from api.models.polls import Poll, PollOption, PollAnswer, QuestionType
from typing import List
from uuid import uuid4
from datetime import datetime, UTC
import logging
from db.storage import polls
from llm import analysis_logic
from llm.summary_logic import summary_logic

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/polls")


# Endpoints
@router.get("/", response_model=List[Poll])
def get_polls():
    return list(polls.values())

@router.get("/{poll_id}", response_model=Poll)
def get_poll(poll_id: str):
    logger.info(f"polls available: {polls}")
    if poll_id not in polls:
        raise HTTPException(status_code=404, detail="Poll not found")
    return polls[poll_id]

@router.post("/", response_model=Poll)
def create_poll(data: dict):
    poll_id = str(uuid4())
    new_poll = Poll(
        id=poll_id,
        question=data["question"],
        questionType=QuestionType.THOUGHT,
        options=[PollOption(id=str(uuid4()), text=opt) for opt in data["options"]],
        isTextBased=data.get("isTextBased", False),
        createdAt=datetime.now(UTC)
    )
    logger.info(f"Creating new poll with ID: {poll_id}")
    polls[poll_id] = new_poll
    return new_poll

@router.put("/{poll_id}/vote", response_model=Poll)
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

@router.post("/{poll_id}/answer", response_model=Poll)
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

@router.post("/{poll_id}/analyze", response_model=dict)
def analyze_poll_opinions(poll_id: str):
    poll = polls.get(poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")
    
    if not poll.answers:
        raise HTTPException(status_code=400, detail="No answers found for this poll")
    
    # Extract answer texts for analysis
    answer_texts = [answer.text for answer in poll.answers]
    
    # Generate analysis using the summary logic
    analysis = analysis_logic(poll.question, answer_texts) 
    
    return {"analysis": analysis}