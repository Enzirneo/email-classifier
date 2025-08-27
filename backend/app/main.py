from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router

app = FastAPI(title="Email Classifier API")

# Permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou o endereço do frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(api_router, prefix="/api")
