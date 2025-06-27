import asyncio
import logging
from config import uvicorn_options
from api import api_router
from fastapi import FastAPI, Request
import uvicorn





app = FastAPI(
    docs_url="/api/openapi"
)

app.include_router(api_router)

if __name__ == '__main__':
    print(uvicorn_options)
    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=True)
