from pydantic import BaseModel, EmailStr
from datetime import date as date_type
from typing import Optional
from typing import Dict

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

class ExpenseCreate(BaseModel):
    """What the client sends us"""
    amount: float
    category: str
    note: Optional[str] = None
    date: date_type

class ExpenseRead(BaseModel):
    """What we send back"""
    id: int
    user_id: int
    amount: float
    category: str
    note: Optional[str] = None
    date: date_type

class ExpenseSummary(BaseModel):
    total: float
    by_category: Dict[str, float]