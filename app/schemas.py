# app/schemas.py
from pydantic import BaseModel

# --- User Schemas ---
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# --- Employee Schemas ---
class EmployeeBase(BaseModel):
    name: str
    position: str

class EmployeeCreate(EmployeeBase):
    user_id: int


class Employee(EmployeeBase):
    id: int
    user_id: int
    user_email: str | None = None  # ✅ only email

    class Config:
        from_attributes = True
