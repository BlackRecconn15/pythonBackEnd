from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..crud.user import create_user as create_user_crud, authenticate_user  # Cambia el nombre de la función importada
from ..schemas.user import User, UserCreate, UserLogin
from ..database import get_db
from ..utils.jwt import create_access_token, verify_access_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

@router.post("/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_crud(db=db, user=user)  # Usa el alias para llamar a la función CRUD

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    authenticated_user = authenticate_user(db, user.email, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        # Genera un token JWT
    token = create_access_token({"sub": authenticated_user.email})

    # Devuelve el token y los datos del usuario
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": authenticated_user.id,
            "email": authenticated_user.email,
            "business_name": authenticated_user.business_name,  # Si aplica
            # Añade más campos si son necesarios
        }
    }


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_access_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        return email
    except Exception as e:
        raise HTTPException(status_code=401, detail="Token inválido")
