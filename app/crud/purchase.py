from sqlalchemy.orm import Session
from ..models.purchase import Purchase, PurchaseItem
from ..schemas.purchase import PurchaseCreate

def create_purchase(db: Session, purchase: PurchaseCreate):
    db_purchase = Purchase(
        user_id=purchase.user_id,
        total=purchase.total,
        shipping_address=purchase.shipping_address,
        city=purchase.city,
        state=purchase.state,
        postal_code=purchase.postal_code,
    )
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)

    for item in purchase.items:
        db_item = PurchaseItem(
            purchase_id=db_purchase.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price,
        )
        db.add(db_item)

    db.commit()
    return db_purchase
