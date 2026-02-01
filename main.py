from fastapi import FastAPI, Depends, HTTPException
from database import Base, engine, SessionLocal
import models, schemas
from auth import hash_password, verify_password, create_access_token
from dependencies import get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CSBCRS-3 Backend")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- AUTH ----------
@app.post("/auth/signup")
def signup(user: schemas.UserCreate, db=Depends(get_db)):
    new_user = models.User(
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}

@app.post("/auth/login")
def login(data: schemas.LoginData, db=Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == data.email
    ).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}

# ---------- APPOINTMENTS ----------
@app.post("/appointments")
def create_appointment(
    data: schemas.AppointmentCreate,
    user=Depends(get_current_user),
    db=Depends(get_db)
):
    appointment = models.Appointment(
        user_id=1,
        provider=data.provider
    )
    db.add(appointment)
    db.commit()
    return {"message": "Appointment created"}

@app.get("/appointments")
def get_appointments(
    user=Depends(get_current_user),
    db=Depends(get_db)
):
    return db.query(models.Appointment).all()

# ---------- COMPLAINTS ----------
@app.post("/complaints")
def create_complaint(
    data: schemas.ComplaintCreate,
    user=Depends(get_current_user),
    db=Depends(get_db)
):
    complaint = models.Complaint(
        user_id=1,
        department=data.department
    )
    db.add(complaint)
    db.commit()
    return {"message": "Complaint submitted"}

@app.get("/complaints")
def get_complaints(
    user=Depends(get_current_user),
    db=Depends(get_db)
):
    return db.query(models.Complaint).all()