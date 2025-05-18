from llm import client


def chat_logic(question: str, message: str):
    # prompt = f"You are discussing the topic: {question}. The user said: {message}. Respond as an insightful assistant helping refine their opinion."
    # completion = client.chat.completions.create(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system", "content": "You are a thoughtful assistant helping users clarify and expand their opinions."},
    #         {"role": "user", "content": prompt},
    #     ]
    # )
    # return completion.choices[0].message.content.strip()
    return "Chat logic"