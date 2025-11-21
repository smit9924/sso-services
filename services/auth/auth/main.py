from fastapi import FastAPI
import logging
from auth.api.routes.main import api_router
from auth.core.config import settings

app = FastAPI()

print('SQLALCHEMY_DATABASE_URI: ', settings.SQLALCHEMY_DATABASE_URI)
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(api_router, prefix="/api")


