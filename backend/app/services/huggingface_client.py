import json
from transformers import pipeline
from app.core.config import settings

# Se o token estiver vazio ou None, não passa use_auth_token
token_arg = settings.HF_TOKEN if settings.HF_TOKEN else None

# Inicializa pipeline HF
classifier_pipeline = pipeline(
    "zero-shot-classification",
    model=settings.HF_MODEL,
    use_auth_token=token_arg
)

def classify_email_with_hf(email_text: str):
    """
    Classifica email usando Hugging Face zero-shot.
    Retorna dict com category, confidence e provider.
    """
    labels = ["Produtivo", "Improdutivo"]
    try:
        res = classifier_pipeline(email_text, candidate_labels=labels, multi_label=False)
        category = res["labels"][0]
        confidence = float(res["scores"][0])
        return {
            "category": category,
            "confidence": round(confidence, 3),
            "suggested_reply": "",
            "provider": "hf"
        }
    except Exception as e:
        print("Erro HF:", e)
        # fallback por regras
        return {
            "category": "Produtivo",
            "confidence": 0.6,
            "suggested_reply": "",
            "provider": "rules"
        }
