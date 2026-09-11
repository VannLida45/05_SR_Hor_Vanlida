
## Chunking Strategy Comparison

For this experiment, I compared fixed-size chunking and sentence-based chunking using the same document,
`002_Resetting_a_Forgotten_PIN.txt`.

### 1. Fixed-Size Chunking

Fixed-size chunking divides the document into chunks based on a fixed size. This makes the chunks more 
consistent in length and gives better control over how much text is stored and retrieved.

However, fixed-size chunking does not understand the meaning of the text. It can split a sentence or an 
instruction in the middle, which may cause important information to be separated between two chunks.

### 2. Sentence-Based Chunking

Sentence-based chunking divides the document according to sentence boundaries. This usually keeps complete 
sentences together and preserves their meaning.

The main disadvantage is that the chunks can have different lengths because sentences are not all the same size.
Very long sentences can create larger chunks, while short sentences can create very small chunks.

### 3. Comparison

Fixed-size chunking provides more predictable chunk sizes, while sentence-based chunking generally provides better
semantic coherence.

For documents such as instructions or help articles, sentence-based chunking can be useful because individual 
sentences often contain complete pieces of information. However, fixed-size chunking may be more useful when 
consistent chunk sizes are important for controlling the amount of text sent to the embedding model or language 
model.

### 4. Conclusion

I chose fixed-size chunking for my main RAG application because it provides consistent chunk sizes and is simple 
to control. I used sentence-based chunking separately for the bonus comparison to understand how different 
splitting strategies affect the resulting chunks.

