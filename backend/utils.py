# backend/utils.py

import math

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Haversine Formula: Do GPS coordinates (Latitude/Longitude) ke beech 
    ka sabse chota distance (as the crow flies) calculate karne ke liye, 
    Earth ke spherical shape ko dhyan me rakhte hue.
    """
    R = 6371.0 # Earth ka radius kilometers mein

    # Degrees ko Radians mein convert karna
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Difference nikalna
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Deep Math Logic (Haversine formula)
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance_km = R * c
    return round(distance_km, 1)

def get_transport_cost(distance_km: float, cost_per_km_per_qtl: float = 2.5) -> int:
    """
    Distance ke hisaab se transport cost nikalna.
    Maan lo 1 quintal fasal le jane ka kharcha ₹2.5 per km hai.
    """
    total_cost = distance_km * cost_per_km_per_qtl
    return int(total_cost)