"""
data_cleaning.py
Purpose: Clean raw gold market dataset
"""

import pandas as pd

# Load raw data
df = pd.read_csv("../data/raw/gold_data.csv")

# Drop rows with missing important values (gold, SP500, Nasdaq, metals)
important_cols = ["sp500 close", "nasdaq close", "silver close", "oil close",
                  "platinum close", "palladium close", "gold close"]
df_cleaned = df.dropna(subset=important_cols)

# Fill other missing values
df_cleaned['us_rates_%'] = df_cleaned['us_rates_%'].ffill()
df_cleaned['CPI'] = df_cleaned['CPI'].ffill()
df_cleaned['GDP'] = df_cleaned['GDP'].ffill()
df_cleaned['usd_chf'] = df_cleaned['usd_chf'].fillna(df_cleaned['usd_chf'].mean())
df_cleaned['eur_usd'] = df_cleaned['eur_usd'].fillna(df_cleaned['eur_usd'].mean())

# Reset index
df_cleaned = df_cleaned.reset_index(drop=True)

# Save cleaned dataset
df_cleaned.to_csv("../data/cleaned/cleaned_gold_data.csv", index=False)
print("Data cleaning completed. Saved to cleaned_gold_data.csv")
