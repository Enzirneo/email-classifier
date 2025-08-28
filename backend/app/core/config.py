import os
from pydantic import BaseModel

class Settings(BaseModel):
    MODEL_PROVIDER: str = os.getenv("MODEL_PROVIDER", "rules")  # rules | hf | openai
    HF_MODEL: str = os.getenv("HF_MODEL", "distilbert-base-uncased")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    # limiares / tunáveis
    RULES_CONFIDENCE: float = 0.70

settings = Settings()
