from pypdf import PdfReader
from pathlib import Path


def extract_text(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"file not found: {file_path}")
    if path.suffix.lower() != ".pdf":
        raise ValueError("expected a PDF file")
    reader = PdfReader(path)

    text = []
    for page  in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    return "\n".join(text)
