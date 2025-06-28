import requests
import time
from models import Product



import requests
import time

def fetch_wb_products(query, min_price=0, max_price=float("inf"), min_rating=0, min_feedbacks=0, max_pages=None):
    headers = {"User-Agent": "Mozilla/5.0"}
    all_products = []
    page = 1

    while True:
        params = {
            "ab_testing": "false",
            "appType": 1,
            "curr": "rub",
            "dest": -1257786,  #  регион, напр. Москва
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
                time.sleep(1)
                continue

            if response.status_code != 200:
                break

            data = response.json()
            products = data.get("data", {}).get("products", [])

            if not products:
                break

            for p in products:
                price = p.get("priceU", 0) / 100
                sale_price = p.get("salePriceU", 0) / 100
                rating = p.get("reviewRating", 0.0)
                feedbacks = p.get("feedbacks", 0)

                # ⬇️ Применяем фильтры вручную
                if not (min_price <= price <= max_price and rating >= min_rating and feedbacks >= min_feedbacks):
                    continue

                item = {
                    "name": p.get("name"),
                    "price": price,
                    "sale_price": sale_price,
                    "rating": rating,
                    "feedbacks": feedbacks
                }
                all_products.append(item)

            page += 1
            if max_pages and page > max_pages:
                break

        except Exception as e:
            print("Ошибка запроса:", e)
            break

    return all_products

