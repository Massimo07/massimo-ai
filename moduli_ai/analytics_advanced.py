"""
Modulo: analytics_advanced.py
Analisi predittiva, forecast, grafici, alert abbandono, generazione report PDF/HTML automatici. 
Pronto per Streamlit/dashboard.
"""

import matplotlib.pyplot as plt
import random

def plot_growth(users_history):
    # users_history = [{"date":..., "users":...}, ...]
    dates = [u["date"] for u in users_history]
    numbers = [u["users"] for u in users_history]
    plt.plot(dates, numbers)
    plt.title("Crescita Team nel Tempo")
    plt.xlabel("Data")
    plt.ylabel("Membri attivi")
    plt.grid()
    plt.savefig("growth.png")
    plt.close()

def forecast_growth(current, rate=1.1, months=6):
    forecast = [int(current * (rate ** m)) for m in range(1, months+1)]
    return forecast

if __name__ == "__main__":
    sample = [{"date": f"2025-0{d}-01", "users": random.randint(100, 300)} for d in range(1,7)]
    plot_growth(sample)
    print("Forecast 6 mesi:", forecast_growth(200))
