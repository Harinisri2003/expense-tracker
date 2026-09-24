from fastapi import FastAPI
from database import create_db_and_tables
from routers import auth, expenses


app = FastAPI(title="Expense Tracker API")

app.include_router(auth.router)
app.include_router(expenses.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "Expense Tracker API is running"}