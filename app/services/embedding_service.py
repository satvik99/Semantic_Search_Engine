from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def generate_embeddings(chunks: list[str]):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunks
    )
    print(response.data[0].embedding)
    return [item.embedding for item in response.data]

