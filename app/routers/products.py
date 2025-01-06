from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..crud.product import get_products
from ..schemas.product import Product
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=list[Product])
def read_products(
    skip: int = 0, 
    limit: int = 10, 
    search: str = Query(None),
    db: Session = Depends(get_db)
):
    return get_products(db, skip=skip, limit=limit, search=search)