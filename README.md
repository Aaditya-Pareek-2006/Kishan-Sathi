# 🌾 Kisan Intel: AI-Powered Price Intelligence & Market Visibility Platform

![Hackathon Domain](https://img.shields.io/badge/Domain-AgriTech-success)
![AI/ML](https://img.shields.io/badge/AI%2FML-Predictive%20Analytics-blue)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688)

## 📌 The Problem (Information Asymmetry)
In India, over 270 million farmers suffer from information asymmetry. Prices are delayed, and middlemen exploit this gap by offering 20–30% below fair market prices. Existing digital platforms either lack real-time data or fail to integrate multiple buyers, forcing farmers into distress sales.

## 🚀 Our Solution
**Kisan Intel** is a deep-tech, user-friendly platform designed to empower low-literacy farmers. It goes beyond just displaying data—it provides **actionable intelligence** using Machine Learning.

### 🔥 Key "X-Factor" Features:
1. **AI "Hold vs. Sell" Predictor:** Analyzes historical `Arrival_Tonnes` and `Weather` data to predict short-term price trends, helping farmers choose the best selling window.
2. **Net Profit Calculator (Deep Math):** Uses the **Haversine Formula** to calculate real-world distance between the farmer and the Mandi/Factory, dynamically deducting transport costs to show *actual* net profit.
3. **Verified Private Buyers & FPOs:** Bypasses middlemen by listing verified factories with trust scores.
4. **Low-Literacy UX:** Color-coded UI, voice-search simulation, and WhatsApp alert integration.

---

## 🏗️ System Architecture & Tech Stack

* **Frontend:** HTML5, Vanilla JavaScript (Modular Components), Tailwind CSS.
* **Backend Engine:** Python, FastAPI, Uvicorn (Micro-architecture routing).
* **AI & Data Core:** Pandas, Scikit-Learn, Math (for geographical calculations).
* **Database:** Local CSV (Historical Mandi Data) & JSON (Real-time Buyer Rates).

---

## 📂 Project Structure

```text
agri-intel-platform/
│
├── frontend/                     # Farmer & Admin UI
│   ├── index.html                # Main Dashboard
│   ├── admin.html                # Data Entry Portal
│   ├── app.js                    # Core UI Logic
│   └── components/               # Reusable UI parts (Gauge, Cards)
│
├── backend/                      # FastAPI Server
│   ├── main.py                   # Server Entry Point
│   ├── requirements.txt          # Dependencies
│   ├── routes/                   # API Endpoints (price_routes, admin_routes)
│   └── utils/                    # Math Logic (profit_calc.py)
│
├── database/                     # Mock Data Storage
│   ├── mandi_prices_2025.csv     # Time-series data for AI learning
│   └── mock_buyers.json          # Live private buyer rates
│
└── ai_models/                    # ML prediction scripts (Upcoming)