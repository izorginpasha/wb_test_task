async def save_to_db(products ,db):
    for item in products:
        product = Product(
            name=item["name"],
            price=item["price"],
            sale_price=item["sale_price"],
            rating=item["rating"],
            feedbacks=item["feedbacks"]
        )
        db.add(product)
        await db.commit()
        await db.refresh(product)
    print(f"Сохранено {len(products)} товаров в базу данных")