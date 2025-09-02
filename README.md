# 📨 Email Classifier AI

[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)](https://fastapi.tiangolo.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-orange)](https://huggingface.co/transformers/)

Sistema de **classificação de e-mails** que identifica se um e-mail é **produtivo** ou **improdutivo** e gera **respostas automáticas naturais e estilizadas** usando IA.

---

## 🚀 Funcionalidades

- Classificação de e-mails via **texto** ou **arquivo** (`.txt` / `.pdf`).  
- Baseado em **regras** ou **modelo HuggingFace** (zero-shot / T5).  
- Geração de respostas **educadas e personalizadas** em português ou inglês.  
- Suporte para múltiplos idiomas (PT/EN).  

---

## 🛠 Tecnologias

- **Backend:** FastAPI, Python 3.11+  
- **IA:** HuggingFace Transformers (`Text2TextGeneration`, `Zero-Shot`)  
- **Processamento de arquivos:** PyPDF2 / Python padrão  
- **Frontend:** React (opcional)  
- **Configuração:** `.env` para tokens e modelos  

---

## ⚡ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/enzirneo/email-classifier.git
cd email-classifier/backend
Crie e ative um ambiente virtual:

bash
Copiar código
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Crie um arquivo .env com as variáveis:

ini
Copiar código
MODEL_PROVIDER=hf
HF_MODEL=facebook/bart-large-mnli
HF_TOKEN=SEU_HF_TOKEN
▶ Como Rodar
bash
Copiar código
uvicorn app.main:app --reload
Acesse o backend em: http://127.0.0.1:8000.

📌 Endpoints da API
Método	Endpoint	Descrição
POST	/api/classify	Classifica e gera resposta de texto
POST	/api/classify-file	Classifica e gera resposta de arquivo
GET	/api/emails-history	Retorna histórico de e-mails classificados

Exemplo de requisição com arquivo (JS)
js
Copiar código
const formData = new FormData();
formData.append("file", arquivo);

const response = await fetch("http://127.0.0.1:8000/api/classify-file", {
  method: "POST",
  body: formData,
});
const data = await response.json();
console.log(data);
📂 Estrutura do Projeto
bash
Copiar código
backend/
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   ├── classifier.py
│   │   └── responder.py
│   ├── storage.py
│   └── core/config.py
├── venv/
├── requirements.txt
└── .env
⚠ Observações
Garanta que o token HuggingFace no .env está correto para usar modelos privados ou T5 em português.

Se a IA falhar, um fallback simples será usado.

Suporte para múltiplos idiomas (PT/EN).

🎯 Próximos passos
Adicionar histórico completo de e-mails classificados com filtros.

Melhorar a personalização das respostas da IA.

Criar interface web interativa com React.