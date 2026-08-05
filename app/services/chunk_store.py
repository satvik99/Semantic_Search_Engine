import json
from pathlib import Path

CHUNK_PATH = Path("uploads/chunks.json")


def save_chunks(chunks: list[str]):
    CHUNK_PATH.parent.mkdir(exist_ok=True)

    with open(CHUNK_PATH, "w", encoding="utf-8") as file:
        json.dump(chunks, file, ensure_ascii=False, indent=4)


def load_chunks() -> list[str]:
    with open(CHUNK_PATH, "r", encoding="utf-8") as file:
        return json.load(file)