from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from app.routers import credential, credential_type
from config import settings

app = FastAPI(title=settings.PROJECT_TITLE)


api_router = APIRouter()
app.include_router(credential.router)
app.include_router(credential_type.router)


@app.get("/health", include_in_schema=False)
async def health_check():
    return JSONResponse(status_code=200, content={"status": "ok"})


app.include_router(api_router)
