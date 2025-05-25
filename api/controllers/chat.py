from fastapi import APIRouter
from llm.chat_logic import chat_logic
from llm.summary_logic import summary_logic
from api.models.chat import ChatRequest, ChatResponse, SummaryRequest, SummaryResponse


router = APIRouter(prefix="/api/chat")


@router.post("/respond", response_model=ChatResponse)
async def chat_respond(req: ChatRequest):
    response = chat_logic(req.question, req.message, req.past_messages)
    return ChatResponse(response=response)


@router.post("/summary", response_model=SummaryResponse)
async def chat_summary(req: SummaryRequest):
    summary = summary_logic(req.question, [m.content for m in req.messages])
    return SummaryResponse(summary=summary)