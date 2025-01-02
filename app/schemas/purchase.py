from pydantic import BaseModel
from typing import List

class PurchaseItemSchema(BaseModel):
    product_id: int
    quantity: int
    price: float

class PurchaseCreate(BaseModel):
    user_id: int
    total: float
    shipping_address: str
    city: str
    state: str
    postal_code: str
    items: List[PurchaseItemSchema]
