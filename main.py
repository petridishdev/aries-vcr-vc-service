from fastapi import FastAPI

from routers.credential import router as credential
from routers.credential_type import router as credential_type

app = FastAPI()
app.include_router(credential)
app.include_router(credential_type)
