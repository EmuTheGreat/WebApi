from pydantic import BaseModel

class ProductBase(BaseModel):
    title: str
    price: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    title: str
    price: str
