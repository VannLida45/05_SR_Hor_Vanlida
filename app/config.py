EMBED_MODEL = "nomic-embed-text"
GEN_MODEL = "llama3.2:3b"

DATA_DIR = "./data/"
CHROMA_DB_DIR = "chroma_db"
COLLECTION_NAME = "my_collection"

CHUNKING_STRATEGY = "fixed"

CHUNK_SIZE = 700
CHUNK_OVERLAP = 100

TOP_K = 4


SYSTEM_PROMPT = (
    "You are a helpful AI assistant that answers questions using the provided context. "
    "The context comes from documents retrieved from a knowledge base. "
    "Use the provided context as the main source of information when answering the user's question. "
    "Answer clearly, accurately, and in simple language. "
    "If the answer is not available in the provided context, say that you do not have enough information "
    "to answer the question instead of making up or guessing an answer. "
    "Do not use information that is unrelated to the provided context. "
    "When possible, explain the answer with relevant details from the context. "
    "Keep the answer focused on the user's question."
)