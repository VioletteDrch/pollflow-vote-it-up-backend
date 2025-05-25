from llm.client import client
from llm.models import LLModels


def analysis_logic(question: str, messages: list[str]):
    full_convo = " ** ".join(messages)
    prompt = f"""You are an assistant helping summarize opinions on: "{question}". Here are all the opinions on the subject :
{full_convo}. Each opinion is separated from the following with this sign ' ** '. Please write a short, clear summary on the diverse opinions regarding the question. Every idea should be conveyed in the final result.
Please write a short, clear summary of the user’s perspective based on this discussion."""
    
    completion = client.chat.completions.create(
        model=LLModels.GPT_4o_MINI,
        messages=[
            {"role": "system", "content": "You summarize diverse opinions into constructive summaries."},
            {"role": "user", "content": prompt},
        ]
    )

    return completion.choices[0].message.content.strip()