# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Teeno alag-alag modules import kar rahe hain (Micro-architecture)
from routes import router as api_router           # Dashboard ka data dene ke liye
from auth_routes import router as auth_router     # Login & Security ke liye
from admin_routes import router as admin_router   # Data save/write karne ke liye

# 1. Server Initialize karna
app = FastAPI(
    title="Kisan Intel API",
    description="Farmer Price Intelligence Platform Backend",
    version="1.0.0"
)

# 2. CORS Setup (Taaki frontend kisi bhi port se baat kar sake)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Router Include Karna (Saare darwaze open karna)
app.include_router(api_router, prefix="/api")
app.include_router(auth_router, prefix="/api/auth") # Login API: /api/auth/login
app.include_router(admin_router, prefix="/api")     # Admin API: /api/add-buyer-price

# 4. Root Endpoint
@app.get("/")
def read_root():
    return {"status": "Server is running perfectly! 🚀", "architecture": "Modular Full-Stack"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)