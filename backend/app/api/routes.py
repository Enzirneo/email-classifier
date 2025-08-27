from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EmailRequest(BaseModel):
    email_text: str

@router.post("/classify")
async def classify_email(request: EmailRequest):
    text = request.email_text.lower()
    # Classificação simples
    if "feliz" in text or "obrigado" in text:
        category = "Improdutivo"
        suggested_reply = "Sem ação necessária."
    else:
        category = "Produtivo"
        suggested_reply = "Responder solicitando detalhes adicionais."

    return {"category": category, "suggested_reply": suggested_reply}
