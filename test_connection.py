import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

async def test_connection():
    DB_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/wb_parser"

    engine = create_async_engine(
        DB_URL,
        echo=True,
        connect_args={"ssl": False}  # важно для Windows
    )

    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            print("✅ Успешное подключение:", result.scalar())
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(test_connection())
