from openai import OpenAI

client = OpenAI()


def generate_answer(context: str, question: str):
    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text