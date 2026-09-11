# Offline RAG Chat 

## Overview

This project is a local Naive Retrieval-Augmented Generation (RAG) application. It reads text documents, splits them into chunks, creates embeddings, stores the vectors in ChromaDB, retrieves relevant chunks for a user question, and uses a local LLM to generate a grounded answer.

## Technologies

* Python
* Ollama
* `nomic-embed-text` for embeddings
* `llama3.2:3b` for text generation
* ChromaDB for vector storage


## Project Pipeline


Documents
    ↓
Ingestion
    ↓
Chunking
    ↓
Embedding
    ↓
ChromaDB
    ↓
Retrieval
    ↓
Local LLM
    ↓
Answer

## Chunking Strategy

I used fixed-size chunking with a chunk size of 700 characters and an overlap of 100 characters.

I chose this strategy because it is simple, predictable, and suitable for a baseline RAG application. The overlap helps preserve information when related text is split between two chunks.

The project also includes a sentence-based chunking strategy for comparison.

## Embedding Model

The application uses the local Ollama model: nomic-embed-text

The model converts each document chunk and user query into numerical vectors. These vectors allow ChromaDB to search for chunks with similar meaning.

## Vector Database

I used ChromaDB in persistent mode.

The database is stored locally in: chroma_db/


## Generation Model

The application uses the local Ollama model: llama3.2:3b

The model receives the user's question together with the retrieved document chunks and generates an answer based on that context.

## How to Run

### 1. Start Ollama

Make sure Ollama is running.

### 2. Pull the models

ollama pull llama3.2
ollama pull nomic-embed-text

### 3. Install dependencies

poetry install

### 4. Add documents

Place `.txt` documents inside:  data/


### 5. Build the vector database

python3 -m app.ingest

### 6. Run the chat application

python3 main.py

### 7. Exit

Type: exit


## Example


Enter question: What is Python?

Answer:
Python is a high-level programming language...


## RAG Components

* `ingest.py` loads documents.
* `chunking.py` splits documents into chunks.
* `embedding.py` creates embeddings.
* `vector_store.py` stores and searches vectors using ChromaDB.
* `retrieve.py` retrieves relevant chunks.
* `generator.py` generates an answer using the local LLM.
* `pipeline.py` connects retrieval and generation.
* `main.py` provides the terminal chat interface.
