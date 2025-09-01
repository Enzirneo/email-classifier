from app.services.huggingface_client import classify_email_with_hf

if __name__ == "__main__":
    test_text = "Olá, preciso de ajuda com o meu ticket de suporte urgente."
    result = classify_email_with_hf(test_text)
    print("Resultado do teste HF:", result)
