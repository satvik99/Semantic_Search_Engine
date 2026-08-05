# Import Router (used to group endpoints),
# HTTPException (used to return HTTP errors),
# UploadFile (FastAPI object representing an uploaded file)
from fastapi import APIRouter, HTTPException, UploadFile

# Import business logic from the service layer.
# The route only orchestrates; it doesn't implement the logic itself.
from app.services.pdf_service import save_pdf, extract_text
from app.services.chunk_service import chunk_text
from app.services.embedding_service import generate_embeddings


# Create a router object.
# Every endpoint in this file belongs to this router.
router = APIRouter()


# POST endpoint that accepts a PDF upload.
@router.post("/upload")
def upload(file: UploadFile):

    # Validate the uploaded file before processing.
    # Reject anything that doesn't have a .pdf extension.
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    # Save the uploaded PDF to disk.
    # Returns the location where it was saved.
    saved_path = save_pdf(file)

    # Read the saved PDF and extract all text.
    # Returns one large string.
    text = extract_text(saved_path)

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    # Return a response to the client.
    # We return only the first 500 characters for debugging.
    return {
        "message": "Document processed successfully",
        #"path": str(saved_path),     # Convert Path object to string for JSON
        #"preview": text[:500]        # Show only a preview instead of the entire PDF
        "chunks": len(chunks),
        "embeddings": len(embeddings),
        "embedding_dimension": len(embeddings[0])
    }