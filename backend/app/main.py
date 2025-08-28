from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.services.nlp import ensure_nlp_resources

app = FastAPI(title="Email Classifier API", version="1.0.0")

# CORS (ajuste a origem do seu frontend em produção)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ex.: ["https://seu-frontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Baixa/garante recursos NLP (stopwords/lemmatizer) no startup
@app.on_event("startup")
def _startup():
    ensure_nlp_resources()

# Rotas principais
app.include_router(api_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}
