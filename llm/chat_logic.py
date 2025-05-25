from typing import List
from api.models.chat import Message
from llm.client import client
from llm.models import LLModels

def format_chat_history(chat_history: List[Message]):
    messages = [
        f"{m.sender.upper()} : {m.content}"
        for m in chat_history
    ]
    return "\n".join(messages)


def chat_logic(question: str, message: str, chat_history: List[Message]):
    history = format_chat_history(chat_history)
    print(history)

    prompt = f"""
        You are having a conversation with a user about the topic: "{question}".

        Your role is to help the user reflect and form a thoughtful, informed opinion on the topic. 
        Encourage them to express themselves freely, especially if they are unsure or hesitant.
        Make them feel legitimate in their perspective, and guide them with empathy.

        You can ask open-ended questions or gently challenge their thinking to help them explore deeper. 
        Your tone should be supportive, curious, and insightful — not argumentative or pushy.

        ---

        Here is the conversation so far:
        {history}

        The user just said:
        "{message}"

        Respond as a thoughtful assistant continuing the conversation.
        """

    completion = client.chat.completions.create(
        model=LLModels.GPT_4o_MINI,
        messages=[
            {"role": "system", "content": "You are a thoughtful assistant helping users clarify and expand their opinions."},
            {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message.content.strip()