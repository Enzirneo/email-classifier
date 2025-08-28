from pydantic import BaseModel, Field

class EmailRequest(BaseModel):
    subject: str = Field("", description="Assunto do email")
    body: str = Field(..., description="Corpo do email")

class ClassificationResponse(BaseModel):
    category: str
    confidence: float
    suggested_reply: str
    provider: str
    tokens: int | None = None
