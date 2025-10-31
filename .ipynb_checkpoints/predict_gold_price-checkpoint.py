# predict_gold_price.py

import joblib
import numpy as np

def predict():
    model = joblib.load("gold_price_rf_model.pkl")
    selected_features = [
        'oil close', 'nasdaq close', 'CPI', 'GDP', 
        'us_rates_%', 'silver close', 'usd_chf'
    ]

    print("\n=== Gold Price Prediction ===\n")
    print("Enter the following values:")

    user_input = []
    for feature in selected_features:
        value = float(input(f"Enter {feature}: "))
        user_input.append(value)

    input_array = np.array(user_input).reshape(1, -1)
    predicted_price = model.predict(input_array)[0]

    print("\n💰 Predicted Gold Price:", round(predicted_price, 2))


# 🚀 Run automatically on import
predict()
