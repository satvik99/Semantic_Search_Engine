from app.services.embedding_service import generate_embeddings
from app.services.faiss_service import load_index, search_index
from app.services.chunk_store import load_chunks


def test_list_copy_retrieval():

    query = "why can not I copy a list like list2=list1"

    query_embedding = generate_embeddings([query])[0]

    index = load_index()

    distances, indices = search_index(
        index,
        query_embedding,
        k=5
    )

    chunks = load_chunks()

    retrieved_chunks = [chunks[i] for i in indices]

    retrieved_text = " ".join(" ".join(retrieved_chunks).split())

    assert "list2 = list1" in retrieved_text