Building this RAG application helped me understand how the different components of a Retrieval-Augmented
Generation system work together. One thing that worked well was the complete pipeline from document
ingestion to answer generation. The application successfully loaded my text documents, divided them into
smaller chunks, created embeddings using the local nomic-embed-text model, stored them in ChromaDB, and
retrieved relevant chunks when I asked questions. Using the local llama3.2:3b model also allowed the application
to generate answers without depending on an external API.

One thing that was harder than I expected was making the different components work together correctly.
In particular, handling document chunks, embedding them, storing them with unique IDs, and
retrieving the correct results required careful debugging. I also learned that simply retrieving chunks
does not always guarantee that every retrieved chunk is perfectly relevant to the question.

In the future, I would improve the application by adding a re-ranking stage and the speed of model
answering is not fast yet. And instead of directly sending the top retrieved chunks to the language
model, I could retrieve more candidate chunks first and then use a re-ranking model to select the most
relevant ones. This could improve retrieval quality and help the LLM receive more focused context.
I could also experiment with different chunk sizes and overlap values to see how they affect the quality
of the answers.