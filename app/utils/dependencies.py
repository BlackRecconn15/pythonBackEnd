from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from ..utils.jwt import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    return payload
