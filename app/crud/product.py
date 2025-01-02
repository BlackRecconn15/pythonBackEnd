from sqlalchemy.orm import Session
from ..models.product import Product
from ..schemas.product import ProductCreate


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name = product.name,
        sku = product.sku,
        description = product.description,
        price = product.price,
        stock = product.stock,
        shippingCost = product.shippingCost,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
