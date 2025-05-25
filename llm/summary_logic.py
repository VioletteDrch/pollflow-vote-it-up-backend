from api.models.chat import Message
from llm.client import client
from llm.models import LLModels
from llm.utils import format_chat_history


def summary_logic(question: str, messages: list[Message]):
    
    full_convo = format_chat_history(messages)

    prompt = f"""You are an assistant summarizing a user's opinion on: "{question}".

        The user had a conversation with an AI to refine their thinking. The full conversation is shown below. It includes both the user's and the AI's messages.

        Your task is to write a **short, clear summary of the user's final opinion**, based **only on what the user explicitly said or agreed with**. You may use improved formulations introduced by the AI **only if the user clearly accepted or built on them**.

        Do **not** include:
        - Points the AI made that the user did not respond to or agree with
        - Ideas the user rejected or ignored
        - Speculations or interpretations beyond the user’s actual words

        Here is the conversation:
        {full_convo}
    """

    completion = client.chat.completions.create(
        model=LLModels.GPT_4o_MINI,
        messages=[
            {"role": "system", "content": "You summarize user opinions into constructive summaries."},
            {"role": "user", "content": prompt},
        ]
    )

    return completion.choices[0].message.content.strip()