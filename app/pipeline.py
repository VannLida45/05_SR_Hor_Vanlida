
from app.retrieve import retrieve
from app.generator import generate_answer


def build_context(results):

    documents = results["documents"][0]
    context = "\n\n".join(documents)

    return context

def run_pipeline(query):

    results = retrieve(query)
    context = build_context(results)
    answer = generate_answer(
        query,
        context
    )

    return results, answer
