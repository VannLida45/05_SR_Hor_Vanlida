from pathlib import Path

from app.chunking import (
    fixed_size_chunking,
    sentence_chunking,
)
from app.config import DATA_DIR

def read_txt(file_path):
    return file_path.read_text(encoding="utf-8")

def show_chunks(name, chunks):
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    print(f"Number of chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i + 1} ---")
        print(chunk)

def main():
    file_path = Path(DATA_DIR) / "002_Resetting_a_Forgotten_PIN.txt"

    text = read_txt(file_path)
    fixed_chunks = fixed_size_chunking(text)
    sentence_chunks = sentence_chunking(text)

    show_chunks(
        "FIXED-SIZE CHUNKING", fixed_chunks )
    show_chunks(
        "SENTENCE-BASED CHUNKING", sentence_chunks)

if __name__ == "__main__":
    main()