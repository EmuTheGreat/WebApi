from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./products.db"

# Создание асинхронного движка
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)

# Асинхронная сессия
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Базовый класс моделей
Base = declarative_base()

async def init_db(engine: AsyncEngine):
    """
    Инициализация базы данных: создание таблиц на основе моделей.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
