from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from app.models import *  # Importa todos los modelos desde models/__init__.py

# Cargar variables de entorno
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # URL de conexión desde el archivo .env

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()
Base.metadata.create_all(bind=engine)

# Dependencia para las sesiones de la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
