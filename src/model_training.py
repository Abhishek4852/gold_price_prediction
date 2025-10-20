"""
model_training.py
Purpose: Train multiple regression and machine learning models for gold prediction
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load processed dataset
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "processed", "processed_gold_data.csv")

df = pd.read_csv(file_path)
# Select top correlated features
top_features = ['sp500 close', 'oil close', 'silver close', 'platinum close', 'palladium close']
X = df[top_features]
y = df['gold close']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Helper function to evaluate models
def evaluate(model, name):
    y_pred = model.predict(X_test)
    r2 = model.score(X_test, y_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"\n{name}")
    print(f"R²: {r2:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")

# 1️⃣ Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
evaluate(lin_reg, "Linear Regression")

# 2️⃣ Polynomial Regression (Degree 2)
poly_features = PolynomialFeatures(degree=2)
X_poly_train = poly_features.fit_transform(X_train)
X_poly_test = poly_features.transform(X_test)
poly_reg = LinearRegression()
poly_reg.fit(X_poly_train, y_train)
y_pred_poly = poly_reg.predict(X_poly_test)
r2_poly = poly_reg.score(X_poly_test, y_test)
mae_poly = mean_absolute_error(y_test, y_pred_poly)
rmse_poly = np.sqrt(mean_squared_error(y_test, y_pred_poly))
print("\nPolynomial Regression (Degree 2)")
print(f"R²: {r2_poly:.4f}")
print(f"MAE: {mae_poly:.4f}")
print(f"RMSE: {rmse_poly:.4f}")

# 3️⃣ Ridge Regression
ridge = Ridge()
ridge.fit(X_train, y_train)
evaluate(ridge, "Ridge Regression")

# 4️⃣ Lasso Regression
lasso = Lasso()
lasso.fit(X_train, y_train)
evaluate(lasso, "Lasso Regression")

# 5️⃣ Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
evaluate(rf, "Random Forest Regression")
