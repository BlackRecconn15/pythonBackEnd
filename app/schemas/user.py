from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    business_name: str
    phone: str
    email: EmailStr
    street: str
    ext_number: str
    int_number: str | None = None
    colony: str
    postal_code: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    official_id_url: str | None = None
    cfs_url: str | None = None

    class Config:
        orm_mode = True


# Nuevo esquema para el login
class UserLogin(BaseModel):
    email: str
    password: str
