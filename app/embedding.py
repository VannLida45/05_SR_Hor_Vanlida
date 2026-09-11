from typing import List

import ollama
from app.config  import EMBED_MODEL

def embed(texts: List[str]) -> List[List[float]]:
    """Embed a list of strings into a list of lists of floats."""
    if not texts:
        return []

    response = ollama.embed(
        model=EMBED_MODEL,
        input=texts
    )

    return list(response.embeddings)

def embed_query(text: str) -> List[float]:
    """Embed a single query into a vector."""
    return embed([text])[0]