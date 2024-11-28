from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from database import engine, Base
from models import Product
from schemas import ProductCreate, Product
from crud import (
    get_products,
    get_product,
    create_product,
    delete_product,
    async_parse_products,
)

# Инициализация базы данных
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(on_startup=[init_db])

# Создание зависимостей для асинхронной сессии
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with SessionLocal() as session:
        yield session


@app.get("/products/", response_model=list[Product])
async def read_products(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_products(db, skip=skip, limit=limit)


@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product = await get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.post("/products/", response_model=Product)
async def create_new_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    return await create_product(db, product=product)


@app.delete("/products/{product_id}")
async def delete_product_endpoint(product_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_product(db, product_id=product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}


@app.post("/parse/")
async def start_parsing(db: AsyncSession = Depends(get_db)):
    await async_parse_products(db)
    return {"message": "Parsing complete"}

