from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.email import EmailRequest, ClassificationResponse
from app.services.classifier import classify_email_text
from app.utils.helpers import read_txt_file, read_pdf_file

router = APIRouter(tags=["Classifier"])

@router.post("/classify", response_model=ClassificationResponse)
async def classify(req: EmailRequest):
    result = classify_email_text(subject=req.subject, body=req.body)
    return result

@router.post("/classify-file", response_model=ClassificationResponse)
async def classify_file(file: UploadFile = File(...)):
    filename = (file.filename or "").lower()
    if filename.endswith(".txt"):
        text = await read_txt_file(file)
    elif filename.endswith(".pdf"):
        text = await read_pdf_file(file)
    else:
        raise HTTPException(status_code=400, detail="Formato não suportado. Envie .txt ou .pdf")
    result = classify_email_text(subject="", body=text)
    return result
