from sqlalchemy import Column, Integer, String, Float
from ..database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sku = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    shippingCost = Column(Integer)
    image_url = Column(String, nullable=True)  # Campo para la URL de la imagen
