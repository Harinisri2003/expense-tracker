from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone
from datetime import date as date_type
from typing import Optional
from sqlmodel import Field, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Expense(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    amount: float
    category: str
    note: Optional[str] = None
    date: date_type
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))