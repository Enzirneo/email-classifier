from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.email import EmailRequest, ClassificationResponse
from app.services.classifier import classify_email_text
from app.utils.helpers import read_txt_file, read_pdf_file
from app.storage import add_email, get_all_emails
from datetime import datetime

router = APIRouter(tags=["Classifier"])

@router.post("/classify", response_model=ClassificationResponse)
async def classify(req: EmailRequest):
    result = classify_email_text(req.subject, req.body)
    timestamp = datetime.utcnow().isoformat()

    add_email({
        "subject": req.subject,
        "body": req.body,
        "category": result["category"],
        "confidence": result["confidence"],
        "suggested_reply": result["suggested_reply"],
        "provider": result["provider"],
        "responded": False,
        "timestamp": timestamp,
        "fileName": None
    })

    return {
        "subject": req.subject,
        "body": req.body,
        "category": result["category"],
        "confidence": result["confidence"],
        "suggested_reply": result["suggested_reply"],
        "provider": result["provider"],
        "fileName": None,
        "timestamp": timestamp
    }

@router.post("/classify-file", response_model=ClassificationResponse)
async def classify_file(file: UploadFile = File(...)):
    filename = (file.filename or "").lower()
    if filename.endswith(".txt"):
        text = await read_txt_file(file)
    elif filename.endswith(".pdf"):
        text = await read_pdf_file(file)
    else:
        raise HTTPException(status_code=400, detail="Formato não suportado. Envie .txt ou .pdf")

    result = classify_email_text("", text)
    timestamp = datetime.utcnow().isoformat()

    add_email({
        "subject": "",
        "body": text,
        "category": result["category"],
        "confidence": result["confidence"],
        "suggested_reply": result["suggested_reply"],
        "provider": result["provider"],
        "responded": False,
        "timestamp": timestamp,
        "fileName": file.filename
    })

    # Retorna todos os dados para o frontend
    return {
        "subject": "",
        "body": text,
        "category": result["category"],
        "confidence": result["confidence"],
        "suggested_reply": result["suggested_reply"],
        "provider": result["provider"],
        "fileName": file.filename,
        "timestamp": timestamp
    }

@router.get("/emails-history")
def emails_history():
    return {"emails": get_all_emails()}
