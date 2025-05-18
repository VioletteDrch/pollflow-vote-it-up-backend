from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.logging import setup_logging
from api.controllers import polls, chat


setup_logging()

app = FastAPI()

app.include_router(polls.router, tags=["polls"])
app.include_router(chat.router, tags=["chat"])


# Allow frontend dev server to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)