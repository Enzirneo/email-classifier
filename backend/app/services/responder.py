from transformers import pipeline
from app.core.config import settings

# Pipeline HF para geração de texto com token de autenticação
hf_text_pipeline = pipeline(
    "text2text-generation",
    model=settings.HF_MODEL,
    tokenizer=settings.HF_MODEL,
    device=-1,  # -1 = CPU, 0 = GPU se disponível
    use_auth_token=settings.HF_TOKEN
)

def fallback_reply(category: str):
    """Fallback simples caso HF falhe"""
    category = category.lower()
    if category == "produtivo":
        return "Olá! Recebemos sua mensagem e vamos analisar. Em breve retornaremos."
    else:
        return "Olá! Obrigado pelo contato. Não há ação necessária no momento."

def generate_ai_reply(category: str, subject: str, body: str) -> str:
    """
    Gera uma resposta natural usando HF Text2Text.
    Se der erro, usa fallback.
    """
    prompt = (
        f"Você é um assistente de email. Baseado na categoria '{category}', "
        f"responda o seguinte email de forma educada, curta e natural, apenas com a resposta:\n\n"
        f"Assunto: {subject}\n"
        f"Corpo: {body}\n\n"
        f"Resposta:"
    )
    try:
        # Aqui apenas parâmetros de geração, token não é necessário
        result = hf_text_pipeline(prompt, max_new_tokens=200)
        return result[0]["generated_text"].strip()
    except Exception as e:
        print("Erro ao gerar resposta com HF:", e)
        return fallback_reply(category)
