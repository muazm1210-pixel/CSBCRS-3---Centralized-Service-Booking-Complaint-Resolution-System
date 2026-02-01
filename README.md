# CSBCRS-3 (Centralized Service Booking & Complaint Resolution System)

CSBCRS-3 is an industry-oriented backend project developed using **Python and FastAPI**. 
The system provides a centralized platform for **service appointment booking** and **public complaint management** such as Food Authority, Police, Rescue, and Municipal services.

## 🔑 Key Features
- Python FastAPI backend
- JWT-based Authentication & Authorization
- Secure Signup and Login system
- Role-based access (Admin, Service Provider, Officer, User)
- Appointment booking and management
- Online complaint registration and tracking
- RESTful GET and POST APIs
- Same backend for Mobile, Web, and Desktop applications
- Designed with scalability and high-traffic handling concepts

## 🛠️ Technologies Used
- Python 3
- FastAPI
- SQLAlchemy (ORM)
- SQLite Database
- JWT (JSON Web Tokens)
- Uvicorn Server

## 🚀 How to Run the Project
1. Create virtual environment  
   -python -m venv venv
   -venv\Scripts\activate
   -pip install fastapi uvicorn sqlalchemy python-jose passlib[bcrypt]
   -uvicorn main:app --reload
   -http://127.0.0.1:8000/docs

 CSBCRS-3/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── routes/
│   │   ├── users.py
│   │   ├── appointments.py
│   │   └── complaints.py
│
├── venv/               
│
├── requirements.txt    
├── .gitignore
├── README.md
  


 


