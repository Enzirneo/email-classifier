import os
from pydantic import BaseModel

class Settings(BaseModel):
    MODEL_PROVIDER: str = os.getenv("MODEL_PROVIDER", "rules")  # rules | hf
    HF_MODEL: str = os.getenv("HF_MODEL", "facebook/bart-large-mnli")
    HF_TOKEN: str = os.getenv("HF_TOKEN", "")

settings = Settings()
