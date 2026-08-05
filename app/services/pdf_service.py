# UploadFile is the object received from FastAPI.
from fastapi import UploadFile

# Path provides filesystem operations in an object-oriented way.
from pathlib import Path

# PdfReader is responsible for reading PDF documents.
from pypdf import PdfReader


def save_pdf(file: UploadFile):

    # Represents the uploads/ folder.
    upload_dir = Path("uploads")

    # Create the folder if it doesn't already exist.
    upload_dir.mkdir(exist_ok=True)

    # Create the complete path:
    # uploads/report.pdf
    file_path = upload_dir / file.filename

    # Open the destination file in Binary Write mode.
    # "with" automatically closes the file after writing.
    with open(file_path, "wb") as buffer:

        # Read bytes from the uploaded file
        # and write them to disk.
        buffer.write(file.file.read())

    # Return where the file was saved.
    return file_path


def extract_text(path: Path):

    # Create an object capable of reading the PDF.
    reader = PdfReader(path)

    # This will hold text from all pages.
    text_from_pdf = ""

    # Visit every page inside the PDF.
    for page in reader.pages:

        # Extract text from the current page.
        page_text = page.extract_text()

        # Some pages may return None (e.g., scanned images).
        if page_text:

            # Append page text and preserve page separation.
            text_from_pdf += page_text + "\n"

    # Return one large string containing the entire document.
    return text_from_pdf