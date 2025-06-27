import requests
import time
from models import Product

from database import AsyncSessionLocal

def fetch_wb_products(query, max_pages=1):
    headers = {"User-Agent": "Mozilla/5.0"}
    all_products = []

    for page in range(max_pages):
        params = {
            "ab_testing": "false",
            "appType": 1,
            "curr": "rub",
            "dest": -1257786,
            "query": query,
            "resultset": "catalog",
            "sort": "popular",
            "spp": 30,
            "page": page + 1
        }

        try:
            response = requests.get(
                "https://search.wb.ru/exactmatch/ru/common/v4/search",
                headers=headers,
                params=params,
                timeout=10
            )

            if response.status_code == 429:
                print("429 — ждём 1s")
                time.sleep(1)
                continue

            if response.status_code != 200:
                print(f"Ошибка: {response.status_code}")
                break

            data = response.json()
            products = data.get("data", {}).get("products", [])

            for p in products:
                item = {
                    "name": p.get("name"),
                    "price": p.get("priceU", 0) / 100,
                    "sale_price": p.get("salePriceU", 0) / 100,
                    "rating": p.get("reviewRating", 0.0),
                    "feedbacks": p.get("feedbacks", 0)
                }
                all_products.append(item)

        except Exception as e:
            print("Ошибка запроса:", e)
            continue

    return all_products

async def save_to_db(products):
    async with AsyncSessionLocal() as session:
        async with session.begin():
            for item in products:
                product = Product(
                    name=item["name"],
                    price=item["price"],
                    sale_price=item["sale_price"],
                    rating=item["rating"],
                    feedbacks=item["feedbacks"]
                )
                session.add(product)
        await session.commit()
    print(f"Сохранено {len(products)} товаров в базу данных")

