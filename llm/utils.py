from typing import List

from api.models.chat import Message


def format_chat_history(chat_history: List[Message]):
    '''
    Renders an AI - user discussion as "AI : message \n USER : message \n ..."
    '''
    messages = [
        f"{m.sender.upper()} : {m.content}"
        for m in chat_history
    ]
    return "\n".join(messages)