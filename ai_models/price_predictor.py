# ai_models/price_predictor.py
import pickle
import os

def predict_action(current_arrival: int, current_weather: str, current_price: int):
    """
    Yeh function trained model load karta hai aur SELL ya HOLD ka decision deta hai.
    """
    # Model ka sahi path dhundhna
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "price_model.pkl")
    
    # 1. Model Load Karna
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
    except FileNotFoundError:
        return {"action": "HOLD", "confidence": "0%", "reason": "Model nahi mila. Pehle .ipynb run karein."}

    # 2. Input Process Karna
    weather_map = {'Rain': 0, 'Clear': 1, 'Cloudy': 2}
    weather_code = weather_map.get(current_weather, 1)

    # 3. Future Price Predict Karna (Math logic)
    predicted_price = model.predict([[current_arrival, weather_code]])[0]

    # 4. Final Decision Dena
    if predicted_price > (current_price + 50):
        return {
            "action": "HOLD",
            "confidence": "85%",
            "reason": f"AI Logic: Aane wale time me bhav ₹{int(predicted_price)} tak ja sakta hai. Rukein."
        }
    else:
        return {
            "action": "SELL",
            "confidence": "90%",
            "reason": f"AI Logic: Supply badhne se bhav ₹{int(predicted_price)} tak gir sakta hai. Bechein."
        }