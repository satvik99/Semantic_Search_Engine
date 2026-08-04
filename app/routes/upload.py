from fastapi import APIRouter, HTTPException, UploadFile
from app.services.pdf_service import save_pdf, extract_text

router = APIRouter()

@router.post("/upload")
def upload(file: UploadFile):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )
    saved_path = save_pdf(file)
    text = extract_text(saved_path)
    return{
        "message": "PDF uploaded successfully",
        "path": str(saved_path),
        "preview": text[:500]
    }

