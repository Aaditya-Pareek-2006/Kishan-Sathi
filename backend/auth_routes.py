# backend/auth_routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json
import os
import random

router = APIRouter()
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database', 'mock_users.json')

# Schemas
class LoginRequest(BaseModel):
    phone: str
    pin: str

class SignupRequest(BaseModel):
    name: str
    phone: str
    pin: str
    village: str
    district: str

# 1. LOGIN ROUTE
@router.post("/login")
def login_user(request: LoginRequest):
    try:
        if os.path.exists(db_path):
            with open(db_path, 'r') as file:
                users = json.load(file)
            for user in users:
                if user['phone'] == request.phone and user['pin'] == request.pin:
                    user_data = user.copy()
                    del user_data['pin'] 
                    return {"status": "success", "message": "Login successful", "user": user_data}
        raise HTTPException(status_code=401, detail="Galat Phone Number ya PIN")
    @router.post("/login")

def login_user(request: LoginRequest):
    try:
        if os.path.exists(db_path):
            with open(db_path, 'r') as file:
                users = json.load(file)

            for user in users:
                if user['phone'] == request.phone and user['pin'] == request.pin:
                    user_data = user.copy()
                    del user_data['pin']

                    return {
                        "status": "success",
                        "message": "Login successful",
                        "user": user_data
                    }

        raise HTTPException(
            status_code=401,
            detail="Galat Phone Number ya PIN"
        )

    except HTTPException:
        raise

    except Exception as e:
        print("LOGIN DATABASE ERROR:", e)
        raise HTTPException(
            status_code=500,
            detail="Database Error!"
        )

# 2. SIGNUP ROUTE (Naya Kisaan Jodna)
@router.post("/signup")
def signup_user(request: SignupRequest):
    users = []
    if os.path.exists(db_path):
        with open(db_path, 'r') as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                users = []
                
    # Check karna ki number pehle se toh nahi hai
    for user in users:
        if user['phone'] == request.phone:
            raise HTTPException(status_code=400, detail="Yeh number pehle se register hai!")

    # Naya kisaan ID generate karna
    new_user = {
        "user_id": f"K-{random.randint(100, 999)}",
        "name": request.name,
        "phone": request.phone,
        "pin": request.pin,
        "village": request.village,
        "district": request.district,
        "crops": ["Pyaz"] # Default crop
    }
    
    # Naya user database me add aur save karna
    users.append(new_user)
    with open(db_path, 'w') as file:
        json.dump(users, file, indent=4)
        
    # Auto-login ke liye bina PIN ka data wapas bhejna
    user_data = new_user.copy()
    del user_data['pin']
    return {"status": "success", "message": "Account ban gaya!", "user": user_data}