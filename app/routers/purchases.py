from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.purchase import PurchaseCreate
from ..crud.purchase import create_purchase
from ..database import get_db

router = APIRouter()

@router.post("/")
def register_purchase(purchase: PurchaseCreate, db: Session = Depends(get_db)):
    try:
        new_purchase = create_purchase(db, purchase)
        return {"message": "Purchase registered successfully", "purchase": new_purchase}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error registering purchase: {e}")
