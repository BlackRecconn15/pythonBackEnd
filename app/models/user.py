from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String, index=True)  # Nombre Comercial
    phone = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    official_id_url = Column(Text, nullable=True)  # URL para el archivo de identificación oficial
    cfs_url = Column(Text, nullable=True)         # URL para el archivo CFS
    street = Column(String)
    ext_number = Column(String)
    int_number = Column(String, nullable=True)
    colony = Column(String)
    postal_code = Column(String)

    # Relación con Purchase
    purchases = relationship("Purchase", back_populates="user")
