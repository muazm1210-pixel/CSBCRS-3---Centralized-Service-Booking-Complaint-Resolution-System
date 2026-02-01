from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    role: str


class LoginData(BaseModel):
    email: str
    password: str


class AppointmentCreate(BaseModel):
    provider: str


class ComplaintCreate(BaseModel):
    department: str