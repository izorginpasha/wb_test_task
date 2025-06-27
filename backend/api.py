from fastapi import APIRouter
from schemas import ProductResponse
from backend.db.db import db_dependency
api_router = APIRouter(prefix="/products", tags=['products'])

@api_router.get("/", response_model=list[ProductResponse])
async def get_products(db: db_dependency,products:ProductResponse ):
    return await get_products(db, products)