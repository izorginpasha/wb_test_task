import asyncio
from parser import fetch_wb_products, save_to_db
from models import Product
from database import Base, engine
from fastapi import FastAPI, Request


app = FastAPI(
    docs_url="/api/openapi"
)

async def main():
    # Создаем таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    query =  'кроссовки'
    items = fetch_wb_products(query, max_pages=1)

    if items:
        await save_to_db(items)
    else:
        print("Не удалось получить товары.")

if __name__ == "__main__":
    asyncio.run(main())
