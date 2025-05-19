from llm.client import client


def summary_logic(question: str, messages: list[str]):
    full_convo = "\n".join(messages)
    prompt = f"""You are an assistant helping summarize a user's opinion on: "{question}". Here is the conversation:
{full_convo}
Please write a short, clear summary of the user’s perspective based on this discussion."""
    
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You summarize user opinions into constructive summaries."},
            {"role": "user", "content": prompt},
        ]
    )

    return completion.choices[0].message.content.strip()