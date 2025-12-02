# app/crud.py
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status
from . import models, schemas

# --- USER CRUD ---
def create_user(db: Session, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Duplicate email — user already exists."
        )
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()


# --- EMPLOYEE CRUD ---
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    user = db.query(models.User).filter(models.User.id == employee.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db_employee = models.Employee(
        name=employee.name,
        position=employee.position,
        user_id=employee.user_id
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


# def get_employees(db: Session):
#     employees = db.query(models.Employee).options(joinedload(models.Employee.user)).all()
#     for emp in employees:
#         emp.user_email = emp.user.email if emp.user else None
#     return employees

def get_employees(db: Session):
    employees = db.query(models.Employee).options(joinedload(models.Employee.user)).all()
    result = []

    for emp in employees:
        result.append({
            "name": emp.name,
            "position": emp.position,
            "email": emp.user.email if emp.user else None
        })

    return result