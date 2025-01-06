from pydantic import BaseModel
from typing import List

# Esquema para ítems de la compra
class PurchaseItemSchema(BaseModel):
    product_id: int
    quantity: int
    price: float

    class Config:
        orm_mode = True

# Esquema para crear una compra
class PurchaseCreate(BaseModel):
    user_id: int
    total: float
    shipping_address: str
    city: str
    state: str
    postal_code: str
    items: List[PurchaseItemSchema]

# Esquema para responder una compra completa
class PurchaseResponse(BaseModel):
    id: int
    user_id: int
    total: float
    shipping_address: str
    city: str
    state: str
    postal_code: str
    items: List[PurchaseItemSchema]

    class Config:
        orm_mode = True
