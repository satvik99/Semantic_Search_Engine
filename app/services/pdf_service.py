from fastapi import UploadFile
from pathlib import Path
from pypdf import PdfReader

def save_pdf(file:UploadFile):
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)
    file_path = upload_dir / file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path

def extract_text(path:Path):
    reader = PdfReader(path)
    text_from_pdf = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_from_pdf += page_text + "\n"
    return text_from_pdf

