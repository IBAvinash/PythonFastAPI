# app/main.py
from fastapi import FastAPI, Depends
from . import models, schemas, crud
from .database import engine, get_db
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

#models.Base.metadata.create_all(bind=engine)

#app = FastAPI(title="FastAPI + PostgreSQL Example")
#http://127.0.0.1:8000/docs
#models.Base.metadata.drop_all(bind=engine)   # deletes all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI + PostgreSQL Example")

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI with PostgreSQL"}

@app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db=Depends(get_db)):
#     return crud.create_user(db, user)

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db=Depends(get_db)):
    return crud.create_user(db, user)
@app.get("/users/", response_model=list[schemas.User])
def read_users(db=Depends(get_db)):
    return crud.get_users(db)


# --- Employee Routes ---
@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db=Depends(get_db)):
    return crud.create_employee(db, employee)

@app.get("/employees/", response_model=list[schemas.Employee])
def read_employees(db=Depends(get_db)):
    return crud.get_employees(db)