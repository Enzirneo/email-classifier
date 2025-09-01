from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.email import EmailRequest, ClassificationResponse
from app.services.classifier import classify_email_text
from app.utils.helpers import read_txt_file, read_pdf_file
from app.storage import add_email, get_all_emails  # <-- import storage

router = APIRouter(tags=["Classifier"])

@router.post("/classify", response_model=ClassificationResponse)
async def classify(req: EmailRequest):
    result = classify_email_text(subject=req.subject, body=req.body)

    # Adiciona o email e resultado ao histórico
    add_email({
        "subject": req.subject,
        "body": req.body,
        "category": result["category"],
        "confidence": result["confidence"],
        "suggested_reply": result["suggested_reply"],
        "provider": result["provider"],
        "responded": False  # Pode ajustar se quiser controlar respostas
    })

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

    # Armazena no histórico
    add_email({
        "subject": "",
        "body": text,
        "category": result["category"],
        "confidence": result["confidence"],
        "suggested_reply": result["suggested_reply"],
        "provider": result["provider"],
        "responded": False
    })

    return result

# Nova rota para retornar o histórico completo
@router.get("/emails-history")
def emails_history():
    return {"emails": get_all_emails()}
