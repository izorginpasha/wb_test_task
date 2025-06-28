from fastapi import APIRouter, Query
from schemas import ProductResponse
from models import Product
from db.db import db_dependency
from crud_product import save_to_db
from parser import fetch_wb_products
from sqlalchemy import select, and_

api_router = APIRouter(prefix="/api/products", tags=['products'])

@api_router.get("/", response_model=list[ProductResponse])
async def get_products(
    db: db_dependency,
    name: str = Query("", description="Название товара"),
    min_price: float = Query(0, description="Минимальная цена"),
    max_price: float = Query(float("inf"), description="Максимальная цена"),
    min_rating: float = Query(0, description="Минимальный рейтинг"),
    min_feedbacks: int = Query(0, description="Минимум отзывов")
):
    # Поиск подходящих продуктов в БД
    query = select(Product).where(
        and_(
            Product.name.ilike(f"%{name}%"),
            Product.price >= min_price,
            Product.price <= max_price,
            Product.rating >= min_rating,
            Product.feedbacks >= min_feedbacks
        )
    )
    result = await db.execute(query)
    products = result.scalars().all()

    # Если подходящих товаров нет — загрузка с WB
    if not products:
        new_products = fetch_wb_products(
            query=name,
            min_price=min_price,
            max_price=max_price,
            min_rating=min_rating,
            min_feedbacks=min_feedbacks
        )
        for item in new_products:
            db.add(Product(**item))
        await db.commit()

        # Повторный запрос из БД после вставки
        result = await db.execute(query)
        products = result.scalars().all()

    return products