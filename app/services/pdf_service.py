from fastapi import UploadFile
from pathlib import Path

def save_pdf(file:UploadFile):
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)
    file_path = upload_dir / file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path
