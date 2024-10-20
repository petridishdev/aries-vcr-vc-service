from fastapi import FastAPI

from config import settings

from routers.credential import router as credential
from routers.credential_type import router as credential_type
from services.verifier import cache_issuer_registry
        
cache_issuer_registry()

app = FastAPI(title=settings.project_title)
app.include_router(credential)
app.include_router(credential_type)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
