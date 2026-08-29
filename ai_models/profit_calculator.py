# ai_models/profit_calculator.py
import math

def calculate_net_profit(farmer_lat: float, farmer_lon: float, buyer_lat: float, buyer_lon: float, price_per_qtl: int) -> dict:
    """
    Haversine Formula: Do GPS coordinates ke beech distance nikal kar actual net profit batata hai.
    """
    R = 6371.0 # Earth radius in kilometers
    
    # Degrees ko Radians me badalna
    lat1_rad, lon1_rad = math.radians(farmer_lat), math.radians(farmer_lon)
    lat2_rad, lon2_rad = math.radians(buyer_lat), math.radians(buyer_lon)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Deep Trigonometry (Sphere logic)
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance_km = round(R * c, 1)
    
    # Cost Logic (Maan lo ₹2.5 lagte hain 1km ka 1 quintal le jane me)
    transport_cost = int(distance_km * 2.5)
    net_profit = price_per_qtl - transport_cost

    return {
        "distance_km": distance_km,
        "transport_cost": transport_cost,
        "net_profit": net_profit
    }