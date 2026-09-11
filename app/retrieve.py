
from app.config import TOP_K
from app.embedding import embed_query
from app.vector_store import search_documents

def retrieve(query):
    query_embedding = embed_query(query)
    results = search_documents(
        query_embedding,
        TOP_K
    )

    return results

def main():

    query = input("Enter your question: ")

    results = retrieve(query)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    print("\nRetrieved chunks:\n")

    for i, document in enumerate(documents):

        print(f"--- Chunk {i + 1} ---")

        print(
            f"Source: "
            f"{metadatas[i]['source']}"
        )

        print(
            f"Distance: "
            f"{distances[i]}"
        )
        print(document)
        print()

if __name__ == "__main__":
    main()

