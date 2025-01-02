from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate
import bcrypt

def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    
    db_user = User(
        email=user.email,
        password=hashed_password.decode('utf-8'),  
        business_name=user.business_name,
        phone=user.phone,
        street=user.street,
        ext_number=user.ext_number,
        int_number=user.int_number,
        colony=user.colony,
        postal_code=user.postal_code,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    # Compara la contraseña encriptada
    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return None
    return user

