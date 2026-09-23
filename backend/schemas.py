from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """What the client sends us on signup"""
    email: EmailStr
    password: str

class UserRead(BaseModel):
    """What we send back — notice: no password field at all"""
    id: int
    email: str