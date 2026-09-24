from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from models import Expense, User
from schemas import ExpenseCreate, ExpenseRead
from auth_utils import get_current_user
from typing import List
from sqlmodel import select

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("", response_model=ExpenseRead, status_code=201)
def create_expense(
    expense_data: ExpenseCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    new_expense = Expense(
        **expense_data.model_dump(),
        user_id=current_user.id  # derived from the token, never from the request
    )

    session.add(new_expense)
    session.commit()
    session.refresh(new_expense)

    return new_expense

@router.get("", response_model=List[ExpenseRead])
def list_expenses(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    expenses = session.exec(
        select(Expense).where(Expense.user_id == current_user.id)
    ).all()

    return expenses