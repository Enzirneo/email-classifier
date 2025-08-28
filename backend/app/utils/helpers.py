from fastapi import UploadFile
from io import BytesIO
from pdfminer.high_level import extract_text

async def read_txt_file(file: UploadFile) -> str:
    content = await file.read()
    try:
        return content.decode("utf-8")
    except Exception:
        return content.decode("latin-1", errors="ignore")

async def read_pdf_file(file: UploadFile) -> str:
    raw = await file.read()
    bio = BytesIO(raw)
    # pdfminer extrai texto diretamente
    text = extract_text(bio) or ""
    return text
