from fastapi import APIRouter
from app.models.search_request import SearchRequest
from app.services.embedding_service import generate_embeddings
from app.services.faiss_service import load_index, search_index
from app.services.chunk_store import load_chunks
from app.services.llm_service import generate_answer

router = APIRouter()


@router.post("/ask")
def ask_question(request: SearchRequest):

    # 1. Embed the question
    query_embedding = generate_embeddings(request.query)[0]

    # 2. Load FAISS index
    index = load_index()

    # 3. Search FAISS
    distance, indices = search_index(index, query_embedding, k=5)

    # 4. Load stored chunks
    chunks = load_chunks()

    # 5. Get the actual text for retrieved indices
    retrieved_chunks = [chunks[i] for i in indices]

    # 6. Combine chunks into context
    context = "\n\n".join(retrieved_chunks)

    # 7. Ask the LLM
    answer = generate_answer(
        context=context,
        question=request.query
    )

    return {
        "query": request.query,
        "answer": answer
    }