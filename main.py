
from app.pipeline import run_pipeline


def main():

    print("Type 'exit' to quit.")

    while True:
        question = input("\nEnter the question: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        results, answer = run_pipeline(question)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        print("\nRetrieved chunks:")

        for i, document in enumerate(documents):
            print(
                f"\n--- Chunk {i + 1} ---"
            )
            print(
                f"Source: "
                f"{metadatas[i]['source']}"
            )
            print(
                f"Distance: "
                f"{distances[i]}"
            )

            print(document)

        print("\nAnswer: ")
        print(answer)


if __name__ == "__main__":
    main()

