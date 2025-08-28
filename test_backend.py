import requests

# URL do backend rodando localmente
BASE_URL = "http://127.0.0.1:8000/api"

# Teste 1: email produtivo
email_produtivo = {
    "subject": "Erro no sistema",
    "body": "Olá, estou enfrentando uma falha no sistema e preciso de suporte urgente. Protocolo #12345."
}

# Teste 2: email improdutivo
email_improdutivo = {
    "subject": "Feliz ano novo!",
    "body": "Desejo a todos um ótimo ano novo e muita felicidade!"
}

def testar_email(email):
    try:
        response = requests.post(f"{BASE_URL}/classify", json=email)
        if response.status_code == 200:
            print("Input:", email)
            print("Resposta do backend:", response.json())
        else:
            print("Erro na requisição:", response.status_code, response.text)
    except Exception as e:
        print("Falha ao conectar com backend:", e)

if __name__ == "__main__":
    print("=== Testando email produtivo ===")
    testar_email(email_produtivo)
    
    print("\n=== Testando email improdutivo ===")
    testar_email(email_improdutivo)
