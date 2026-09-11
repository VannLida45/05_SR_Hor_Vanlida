import chromadb

from app.config import (
    CHROMA_DB_DIR,
    COLLECTION_NAME,
)
def get_collection():

    client = chromadb.PersistentClient(
        path=CHROMA_DB_DIR
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    return collection


def add_documents(
    ids,
    documents,
    embeddings,
    metadatas
):

    collection = get_collection()

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )


def search_documents(
    query_embedding,
    top_k
):

    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    return results