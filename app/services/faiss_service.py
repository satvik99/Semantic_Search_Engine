import faiss
import numpy as np
from pathlib import Path

INDEX_PATH = Path("uploads/faiss_index.bin")


def create_index(embeddings: list[list[float]]):
    embeddings_array = np.array(
        embeddings,
        dtype=np.float32
    )

    dimension = embeddings_array.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings_array)

    return index


def search_index(index, query_embedding: list[float], k: int = 5):
    query_vector = np.array(
        [query_embedding],
        dtype=np.float32
    )

    distances, indices = index.search(query_vector, k)

    return distances[0], indices[0]


def save_index(index):
    INDEX_PATH.parent.mkdir(exist_ok=True)
    faiss.write_index(index, str(INDEX_PATH))


def load_index():
    return faiss.read_index(str(INDEX_PATH))


def index_exists():
    return INDEX_PATH.exists()