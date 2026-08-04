from fastapi import APIRouter
from fastapi import UploadFile
from app.services.pdf_service import save_pdf

router = APIRouter()

@router.post("/upload")
def upload(file: UploadFile):
    saved_path = save_pdf(file)
    return{
        "message": "PDF uploaded successfully",
        "path": str(saved_path)
    }