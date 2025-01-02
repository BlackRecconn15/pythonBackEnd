from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    sku: str
    description: str
    price: float
    stock: int
    shippingCost: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
