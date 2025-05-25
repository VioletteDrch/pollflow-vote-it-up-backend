'''
- Theme clustering.
- 2D or 3D visualisation. 
- Statistics.
- Community Detection. 
- Graph.

'''

from llm.client import client
from llm.models import LLModels

def format_opinions(opinions: list[str]):
    formatted_opinions = [
        f"OPINION : {opinion}"
        for opinion in opinions
    ]
    return "\n".join(formatted_opinions)


def analysis_logic(question: str, opinions: list[str]):
    opinions_list = format_opinions(opinions)

    prompt = f"""
        You are an assistant tasked with summarizing the key points of view shared by users regarding the question: "{question}".

        Below is a collection of user-written opinions, expressed in their own words:
        {opinions_list}

        Please write a concise and well-structured report that includes:
        1. The main perspectives and arguments users shared.
        2. How users agree or disagree with each other, if applicable.
        3. A diversity of viewpoints, avoiding repetition.
        4. A tone that feels natural and human (avoid generic or robotic phrasing).

        The goal is to provide a short, readable document that captures what people think about the question, without sounding too analytical or too vague.

        Begin your report directly. Do not introduce yourself or explain what you're doing.
    """

    
    completion = client.chat.completions.create(
        model=LLModels.GPT_4o_MINI,
        messages=[
            {"role": "system", "content": "You summarize diverse opinions into constructive summaries."},
            {"role": "user", "content": prompt},
        ]
    )

    return completion.choices[0].message.content.strip()