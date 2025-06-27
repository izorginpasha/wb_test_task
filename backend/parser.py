import requests
import time
from models import Product



import requests
import time

def fetch_wb_products(query, max_pages=None):
    headers = {"User-Agent": "Mozilla/5.0"}
    all_products = []
    page = 1

    while True:
        params = {
            "curr": "rub",
            "query": query,
            "resultset": "catalog",


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

            if not products:
                print(f"Страницы закончились на {page - 1}")
                break

            for p in products:
                item = {
                    "name": p.get("name"),
                    "price": p.get("priceU", 0) / 100,
                    "sale_price": p.get("salePriceU", 0) / 100,
                    "rating": p.get("reviewRating", 0.0),
                    "feedbacks": p.get("feedbacks", 0)
                }
                all_products.append(item)

            print(f"Загружена страница {page}, всего товаров: {len(all_products)}")
            page += 1

            if max_pages and page > max_pages:
                break

        except Exception as e:
            print("Ошибка запроса:", e)
            break

    return all_products
