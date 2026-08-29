# backend/routes.py

from fastapi import APIRouter
import sys
import os
import json

# Backend ko batana padega ki 'ai_models' folder main directory me hai
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

# Asli AI aur Math Models ko import karna
from ai_models.price_predictor import predict_action
from ai_models.profit_calculator import calculate_net_profit

# Router initialize karna
router = APIRouter()

@router.get("/dashboard-data")
def get_dashboard_data(crop: str = "Pyaz", farmer_lat: float = 27.86, farmer_lon: float = 75.38):
    """
    Yeh route dashboard ka sara complex data process karta hai aur live DB se read karta hai.
    """
    
    # 1. Mandi Location & Rate (Govt fixed for demo)
    mandi_lat, mandi_lon = 27.95, 75.40 
    mandi_price = 1200
    
    # Math Calculations (Distance & Transport via Haversine)
    profit_data = calculate_net_profit(farmer_lat, farmer_lon, mandi_lat, mandi_lon, mandi_price)
    
    # 2. LIVE DATABASE READ LOGIC (The X-Factor)
    # Default values agar DB khali ho
    private_price = 1350
    private_buyer_name = "AgriFresh Co."
    trust_score = 4.8

    # mock_buyers.json se real-time rate uthana
    db_path = os.path.join(base_dir, 'database', 'mock_buyers.json')
    if os.path.exists(db_path):
        with open(db_path, "r") as file:
            buyers = json.load(file)
            best_rate = 0
            # Loop laga kar us fasal ka sabse accha rate dhundhna
            for buyer in buyers:
                for rate in buyer.get("buying_rates", []):
                    if rate["crop"].lower() == crop.lower():
                        if rate["price_per_qtl"] > best_rate:
                            best_rate = rate["price_per_qtl"]
                            private_buyer_name = buyer["name"]
                            trust_score = buyer.get("trust_score", 4.5)
            
            # Agar rate mila, toh update kar do
            if best_rate > 0:
                private_price = best_rate

    # 3. REAL AI PREDICTION 
    current_arrival_tonnes = 150 
    current_weather = "Clear"
    ai_result = predict_action(current_arrival_tonnes, current_weather, mandi_price)

    # 4. Final Data Frontend ko bhejna
    return {
        "crop": crop,
        "mandiPrice": mandi_price,
        "transportCost": profit_data["transport_cost"], 
        "mandiDistanceKm": profit_data["distance_km"],
        "privatePrice": private_price,
        "privateBuyerName": private_buyer_name,
        "trustScore": trust_score,
        "aiPrediction": ai_result
    }