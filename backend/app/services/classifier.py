from app.services.nlp import preprocess
from app.services.responder import generate_reply
from app.core.config import settings

# Palavras/expressões simples para baseline (regra)
PRODUCTIVE_KEYWORDS = {
    "pt": ["suporte", "erro", "falha", "atualização", "andamento", "protocolo", "ticket", "urgente", "prazo", "relatório", "acesso", "senha", "fatura", "boleto", "cancelamento", "reembolso", "bloqueio", "sistema", "api", "contrato", "chamado"],
    "en": ["support", "issue", "error", "bug", "update", "status", "ticket", "urgent", "deadline", "report", "access", "password", "invoice", "refund", "cancel", "blocked", "system", "api", "contract", "case"],
}
UNPRODUCTIVE_KEYWORDS = {
    "pt": ["feliz", "parabéns", "boas festas", "natal", "ano novo", "obrigado", "agradeço", "bom dia", "boa tarde", "boa noite"],
    "en": ["happy", "congrats", "congratulations", "merry", "christmas", "new year", "thanks", "thank you", "good morning", "good afternoon", "good evening"],
}

def _rules_classifier(text: str) -> tuple[str, float, str]:
    """
    Classificador baseline por regras. Retorna (categoria, confiança, provider)
    """
    prod_hits = sum(any(k in text for k in PRODUCTIVE_KEYWORDS[lang]) for lang in PRODUCTIVE_KEYWORDS)
    unprod_hits = sum(any(k in text for k in UNPRODUCTIVE_KEYWORDS[lang]) for lang in UNPRODUCTIVE_KEYWORDS)

    if prod_hits > unprod_hits and prod_hits > 0:
        return "Produtivo", 0.85, "rules"
    if unprod_hits > prod_hits and unprod_hits > 0:
        return "Improdutivo", 0.85, "rules"
    # fallback
    return "Produtivo", 0.60, "rules"

def _hf_classifier(text: str) -> tuple[str, float, str]:
    """
    Opcional: Hugging Face. Só roda se você instalar transformers/torch e configurar.
    """
    try:
        from transformers import pipeline
        # exemplo simples zero-shot; substitua pelo seu modelo se preferir
        classifier = pipeline("zero-shot-classification", model=settings.HF_MODEL)
        labels = ["Produtivo", "Improdutivo"]
        res = classifier(text, candidate_labels=labels, multi_label=False)
        label = res["labels"][0]
        score = float(res["scores"][0])
        return label, score, "hf"
    except Exception:
        # fallback se não instalado ou deu erro
        return _rules_classifier(text)

def _openai_classifier(text: str) -> tuple[str, float, str]:
    """
    Opcional: OpenAI. Só roda se você setar OPENAI_API_KEY.
    """
    import os
    api_key = settings.OPENAI_API_KEY or os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        return _rules_classifier(text)
    try:
        # usando SDK recente (pseudocódigo para não travar dependências)
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        prompt = (
            "Classifique o email como 'Produtivo' ou 'Improdutivo'. "
            "RESPOSTA EM JSON COM CAMPOS category e confidence (0-1). "
            f"Email:\n{text}"
        )
        resp = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[{"role":"user","content":prompt}],
            temperature=0.0,
        )
        content = resp.choices[0].message.content
        # tentativa simples de parse
        import json, re
        json_str = re.search(r"\{.*\}", content, re.S)
        if json_str:
            data = json.loads(json_str.group(0))
            cat = data.get("category", "Produtivo")
            conf = float(data.get("confidence", 0.8))
            return cat, conf, "openai"
    except Exception:
        pass
    return _rules_classifier(text)

def classify_email_text(subject: str, body: str):
    raw = f"{subject}\n{body}".strip()
    clean = preprocess(raw)

    provider = settings.MODEL_PROVIDER.lower()
    if provider == "hf":
        category, confidence, prov = _hf_classifier(clean)
    elif provider == "openai":
        category, confidence, prov = _openai_classifier(clean)
    else:
        category, confidence, prov = _rules_classifier(clean)

    reply = generate_reply(category=category, subject=subject, body=body)
    return {
        "category": category,
        "confidence": round(confidence, 3),
        "suggested_reply": reply,
        "provider": prov,
    }
