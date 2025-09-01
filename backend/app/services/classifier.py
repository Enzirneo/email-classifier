from app.services.nlp import preprocess
from app.services.responder import generate_ai_reply
from app.core.config import settings
from app.services.huggingface_client import classify_email_with_hf

PRODUCTIVE_KEYWORDS = {
    "pt": ["suporte", "erro", "falha", "atualização", "andamento", "protocolo",
           "ticket", "urgente", "prazo", "relatório", "acesso", "senha",
           "fatura", "boleto", "cancelamento", "reembolso", "bloqueio",
           "sistema", "api", "contrato", "chamado"],
    "en": ["support", "issue", "error", "bug", "update", "status",
           "ticket", "urgent", "deadline", "report", "access", "password",
           "invoice", "refund", "cancel", "blocked", "system", "api",
           "contract", "case"],
}

UNPRODUCTIVE_KEYWORDS = {
    "pt": ["feliz", "parabéns", "boas festas", "natal", "ano novo",
           "obrigado", "agradeço", "bom dia", "boa tarde", "boa noite"],
    "en": ["happy", "congrats", "congratulations", "merry", "christmas",
           "new year", "thanks", "thank you", "good morning",
           "good afternoon", "good evening"],
}

def _rules_classifier(text: str):
    """Classificador baseline por regras."""
    prod_hits = sum(any(k in text for k in PRODUCTIVE_KEYWORDS[lang]) for lang in PRODUCTIVE_KEYWORDS)
    unprod_hits = sum(any(k in text for k in UNPRODUCTIVE_KEYWORDS[lang]) for lang in UNPRODUCTIVE_KEYWORDS)

    if prod_hits > unprod_hits and prod_hits > 0:
        return "Produtivo", 0.85, "rules"
    if unprod_hits > prod_hits and unprod_hits > 0:
        return "Improdutivo", 0.85, "rules"
    return "Produtivo", 0.60, "rules"

def classify_email_text(subject: str, body: str):
    """Classifica o email e gera resposta sugerida."""
    raw = f"{subject}\n{body}".strip()
    clean = preprocess(raw)

    provider = settings.MODEL_PROVIDER.lower()
    if provider == "hf":
        result = classify_email_with_hf(clean)
        category = result["category"]
        confidence = result["confidence"]
        prov = result["provider"]
    else:
        category, confidence, prov = _rules_classifier(clean)

    # Gera resposta natural usando HF ou fallback
    reply = generate_ai_reply(category=category, subject=subject, body=body)

    return {
        "category": category,
        "confidence": round(confidence, 3),
        "suggested_reply": reply,
        "provider": prov,
    }