from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)

    # Relationship: User has many Employees
    employees = relationship("Employee", back_populates="user")  # must match Employee.user


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    position = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relationship: Employee belongs to User
    user = relationship("User", back_populates="employees")  # must match User.employees
