import re

from app.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

def fixed_size_chunking(text):
    text = text.strip()
    if not text:
        return []

    chunks = []

    start = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunks.append(
            text[start:end]        )

        if end >= len(text):
            break

        start = end - CHUNK_OVERLAP

    return chunks

def sentence_chunking(text):

    text = text.strip()

    if not text:
        return []

    sentences = re.split(
        r'(?<=[.!?])\s+', text)

    chunks = []

    current_chunk = ""
    for sentence in sentences:

        if len(current_chunk) + len(sentence) <= CHUNK_SIZE:
            if current_chunk:
                current_chunk += " "

            current_chunk += sentence

        else:

            if current_chunk:
                chunks.append(
                    current_chunk
                )

            current_chunk = sentence

    if current_chunk:
        chunks.append(
            current_chunk
        )

    return chunks