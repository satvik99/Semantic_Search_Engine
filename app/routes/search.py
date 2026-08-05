from fastapi import APIRouter
from app.models.search_request import SearchRequest
from app.services.embedding_service import generate_embeddings
from app.services.faiss_service import load_index, search_index
from app.services.chunk_store import load_chunks





router = APIRouter()
@router.post("/search")
def search(request: SearchRequest):
    index = load_index()
    chunks = load_chunks()
    query_embedding = generate_embeddings(
        [request.query]
    )[0]
    distances, indices = search_index(
        index,
        query_embedding
    )

    results = [
        chunks[i]
        for i in indices[0]
    ]

    return{
        "query": request.query,
        "results_found": len(results),
        "results": results
    }