import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_URL = (
    f"postgresql+asyncpg://{os.getenv('FSTR_DB_LOGIN')}:{os.getenv('FSTR_DB_PASS')}"
    f"@{os.getenv('FSTR_DB_HOST')}:{os.getenv('FSTR_DB_PORT')}/{os.getenv('FSTR_DB_NAME')}"
)

print("Подключение к БД:", DB_URL)

# Асинхронный движок
engine = create_async_engine(DB_URL, echo=True)

# Асинхронная сессия
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Базовая модель
Base = declarative_base()
