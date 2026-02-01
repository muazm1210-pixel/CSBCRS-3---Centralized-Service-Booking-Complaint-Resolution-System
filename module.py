from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)   # admin, provider, officer, user


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    provider = Column(String)
    status = Column(String, default="pending")


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    department = Column(String)
    status = Column(String, default="pending")