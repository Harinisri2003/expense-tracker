from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """What the client sends us on signup"""
    email: EmailStr
    password: str

class UserRead(BaseModel):
    """What we send back — notice: no password field at all"""
    id: int
    email: str

class UserLogin(BaseModel):
    """What the client sends us on login"""
    email: EmailStr
    password: str

class Token(BaseModel):
    """What we send back after successful login"""
    access_token: str
    token_type: str = "bearer"