
from pathlib import Path

from app.vector_store import add_documents
from app.embedding import embed
from app.chunking import fixed_size_chunking,sentence_chunking;

from app.config import (
    DATA_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    CHUNKING_STRATEGY
)


def read_txt(file_path):
    return file_path.read_text(encoding="utf-8")

def load_documents():
    documents = []

    data_path = Path(DATA_DIR)

    for file_path in data_path.glob("*.txt"):
        text = read_txt(file_path)

        documents.append({
            "text": text,
            "source": file_path.name,
        })

    return documents


def chunk_text(text):

    text = text.strip()

    if not text:
        return []

    if CHUNKING_STRATEGY == "fixed":
        return fixed_size_chunking(text)

    if CHUNKING_STRATEGY == "sentence":
        return sentence_chunking(text)



def build_index():

    documents = load_documents()

    print(f"Loaded {len(documents)} documents")

    if not documents:
        print("No .txt files found in the data folder.")
        return

    ids, texts, metadatas = [], [], []

    for document in documents:

        filename = document["source"]
        full_text = document["text"]

        print(f"\nProcessing: {filename}")

        for i, chunk in enumerate(
            chunk_text(full_text)
        ):

            ids.append(
                f"{filename}::{i}"
            )

            texts.append(chunk)

            metadatas.append({
                "source": filename,
                "chunk_index": i
            })

    print(f"\nTotal chunks: {len(texts)}")

    print("Creating embeddings...")

    embeddings = embed(texts)

    print("Saving chunks to ChromaDB...")

    add_documents(
        ids,
        texts,
        embeddings,
        metadatas
    )

    print("\nIngestion completed!")


if __name__ == "__main__":
    build_index()

