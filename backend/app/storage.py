# app/storage.py

# Lista global para armazenar os emails
emails_history = []

def add_email(email_data: dict):
    """Adiciona um email à lista global"""
    emails_history.append(email_data)

def get_all_emails():
    """Retorna todos os emails armazenados"""
    return emails_history
