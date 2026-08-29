# backend/admin_routes.py
from fastapi import APIRouter
from pydantic import BaseModel
import json
import os

router = APIRouter()

class NewPriceData(BaseModel):
    buyer_id: str
    crop: str
    price_per_qtl: int
    quality_req: str

@router.post("/add-buyer-price")
def add_price(new_data: NewPriceData):
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database', 'mock_buyers.json')
    
    if not os.path.exists(db_path):
        return {"status": "Failed", "message": "Database file (mock_buyers.json) nahi mili!"}

    with open(db_path, "r") as file:
        buyers = json.load(file)

    updated = False
    for buyer in buyers:
        if buyer["buyer_id"] == new_data.buyer_id:
            buyer["buying_rates"].append({
                "crop": new_data.crop,
                "price_per_qtl": new_data.price_per_qtl,
                "quality_req": new_data.quality_req
            })
            updated = True
            break

    if updated:
        with open(db_path, "w") as file:
            json.dump(buyers, file, indent=4)
        return {"status": "Success", "message": f"{new_data.crop} ka naya rate update ho gaya!"}
    
    return {"status": "Failed", "message": "Buyer ID nahi mili."}