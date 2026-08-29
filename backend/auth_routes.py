# backend/auth_routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json
import os
import random

router = APIRouter()

# Path to mock database
db_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "database",
    "mock_users.json"
)


# ============================================================
# SCHEMAS
# ============================================================

class LoginRequest(BaseModel):
    phone: str
    pin: str


class SignupRequest(BaseModel):
    name: str
    phone: str
    pin: str
    village: str
    district: str


# ============================================================
# 1. LOGIN ROUTE
# ============================================================

@router.post("/login")
def login_user(request: LoginRequest):

    try:
        # Check whether database file exists
        if not os.path.exists(db_path):
            print("DATABASE FILE NOT FOUND:", db_path)

            raise HTTPException(
                status_code=500,
                detail="Database file not found!"
            )

        # Read users database
        with open(db_path, "r", encoding="utf-8") as file:
            users = json.load(file)

        # Check credentials
        for user in users:

            if (
                str(user.get("phone")) == str(request.phone)
                and str(user.get("pin")) == str(request.pin)
            ):
                # Don't send PIN back to frontend
                user_data = user.copy()
                user_data.pop("pin", None)

                return {
                    "status": "success",
                    "message": "Login successful",
                    "user": user_data
                }

        # Credentials don't match
        raise HTTPException(
            status_code=401,
            detail="Galat Phone Number ya PIN"
        )

    except HTTPException:
        raise

    except json.JSONDecodeError:
        print("LOGIN DATABASE ERROR: Invalid JSON")

        raise HTTPException(
            status_code=500,
            detail="Database Error: Invalid database file!"
        )

    except Exception as e:
        print("LOGIN DATABASE ERROR:", e)

        raise HTTPException(
            status_code=500,
            detail="Database Error!"
        )


# ============================================================
# 2. SIGNUP ROUTE
# ============================================================

@router.post("/signup")
def signup_user(request: SignupRequest):

    try:
        users = []

        # Load existing users
        if os.path.exists(db_path):

            with open(db_path, "r", encoding="utf-8") as file:

                try:
                    users = json.load(file)

                except json.JSONDecodeError:
                    users = []

        # Check if phone already exists
        for user in users:

            if str(user.get("phone")) == str(request.phone):

                raise HTTPException(
                    status_code=400,
                    detail="Yeh number pehle se register hai!"
                )

        # Generate farmer ID
        new_user = {
            "user_id": f"K-{random.randint(100, 999)}",
            "name": request.name,
            "phone": request.phone,
            "pin": request.pin,
            "village": request.village,
            "district": request.district,
            "crops": ["Pyaz"]
        }

        # Add user
        users.append(new_user)

        # Save database
        with open(db_path, "w", encoding="utf-8") as file:

            json.dump(
                users,
                file,
                indent=4,
                ensure_ascii=False
            )

        # Don't return PIN
        user_data = new_user.copy()
        user_data.pop("pin", None)

        return {
            "status": "success",
            "message": "Account ban gaya!",
            "user": user_data
        }

    except HTTPException:
        raise

    except Exception as e:
        print("SIGNUP DATABASE ERROR:", e)

        raise HTTPException(
            status_code=500,
            detail="Database Error!"
        )