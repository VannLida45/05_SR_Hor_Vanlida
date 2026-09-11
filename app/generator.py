
import ollama

from app.config import (
    GEN_MODEL,
    SYSTEM_PROMPT,
)

def generate_answer(query, context):

    prompt = f"""
                Context: {context}
                Question: {query}
            """

    response = ollama.chat(
        model=GEN_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return response["message"]["content"]
