from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    sku: str
    description: str
    originalPrice: int
    finalprice: int | None
    stock: int
    shippingCost: int
    image_url: str | None  # Campo opcional
    rating: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
