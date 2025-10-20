"""
feature_engineering.py
Purpose: Create features for gold price prediction
"""

import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/cleaned/cleaned_gold_data.csv")
df['date'] = pd.to_datetime(df['date'])

# Example: High-Low spread as a feature
df['gold high-low'] = df['gold high'] - df['gold low']
df['oil high-low'] = df['oil high'] - df['oil low']
df['silver high-low'] = df['silver high'] - df['silver low']

# Add more features if needed
# df['sp500 change'] = df['sp500 close'] - df['sp500 open']

# Save processed dataset
df.to_csv("../data/processed/processed_gold_data.csv", index=False)
print("Feature engineering completed. Saved to processed_gold_data.csv")
