from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Product
from schemas import ProductCreate

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Product).offset(skip).limit(limit))
    return result.scalars().all()

async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(select(Product).filter(Product.id == product_id))
    return result.scalars().first()

async def create_product(db: AsyncSession, product: ProductCreate):
    db_product = Product(title=product.title, price=product.price)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def delete_product(db: AsyncSession, product_id: int):
    db_product = await get_product(db, product_id)
    if db_product is None:
        return False
    await db.delete(db_product)
    await db.commit()
    return True

from parser import parse_products_async

async def async_parse_products(db: AsyncSession):
    products = await parse_products_async()
    for product in products:
        db_product = Product(title=product["Название"], price=product["Цена"])
        db.add(db_product)
    await db.commit()

