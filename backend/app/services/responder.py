def generate_reply(category: str, subject: str, body: str) -> str:
    """
    Gera resposta automática simples baseada na categoria.
    Pode ser substituída por GPT/HF para respostas mais naturais.
    """
    category = (category or "").lower()
    if category == "produtivo":
        return (
            "Olá! Obrigado pelo contato. Recebemos sua mensagem e vamos analisar "
            "o caso. Se possível, responda este email com:\n"
            "- Número do protocolo (se houver)\n"
            "- Prints/telas do erro\n"
            "- Data/Hora aproximada do ocorrido\n\n"
            "Em breve retornaremos com uma atualização."
        )
    elif category == "improdutivo":
        return "Olá! Agradecemos sua mensagem. Não há ação necessária no momento. Tenha um ótimo dia!"
    # fallback
    return "Olá! Recebemos sua mensagem e encaminhamos para análise. Em breve retornaremos."
