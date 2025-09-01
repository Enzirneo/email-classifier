# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.services.nlp import ensure_nlp_resources

# Cria a aplicação FastAPI
app = FastAPI(title="Email Classifier API", version="1.0.0")

# Configuração de CORS (ajuste o allow_origins em produção)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["https://seu-frontend.com"] em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Evento startup: garante que recursos de NLP estão baixados
@app.on_event("startup")
def _startup():
    ensure_nlp_resources()

# Inclui as rotas do API router
app.include_router(api_router, prefix="/api")

# Rota simples de health check
@app.get("/health")
def health():
    return {"status": "ok"}
