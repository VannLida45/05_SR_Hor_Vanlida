from app.embedding import embed_query
from app.vector_store import get_collection



def main():

    question = "How to reset a Jammed Printer?"

    print(f"Question: {question}")

    query_embedding = embed_query(question)

    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
    )

    print("\nTop results:\n")

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for i in range(len(documents)):

        print(f"--- Result {i + 1} ---")

        print(
            f"Source: "
            f"{metadatas[i]['source']}"
        )

        print(
            f"Chunk: "
            f"{metadatas[i]['chunk_index']}"
        )

        print(
            f"Distance: "
            f"{distances[i]}"
        )

        print(
            f"Text:\n"
            f"{documents[i]}"
        )

        print()

if __name__ == "__main__":
    main()