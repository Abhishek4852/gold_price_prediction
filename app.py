import streamlit as st
import joblib
import numpy as np
import pandas as pd
from datetime import datetime

# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_model():
    return joblib.load("gold_price_rf_model.pkl")

model = load_model()

# ----------------------------
# App UI Styling
# ----------------------------
st.set_page_config(page_title="Gold Price Predictor", layout="centered")

st.markdown("""
<style>
    .main-title {
        font-size: 35px !important;
        text-align: center;
        color: #DAA520;
        font-weight: bold;
    }
    .stButton button {
        background-color: #DAA520;
        color: black;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: black;
        color: #DAA520;
    }
</style>
""", unsafe_allow_html=True)


# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("🔧 Options")
page = st.sidebar.radio("Select Page", ["Predict Price", "Prediction History", "About"])

# To store history
if "history" not in st.session_state:
    st.session_state.history = []


# ----------------------------
# Prediction Page
# ----------------------------
if page == "Predict Price":
    
    st.markdown("<h1 class='main-title'>💰 Gold Price Prediction</h1>", unsafe_allow_html=True)
    st.write("Enter financial indicators below to estimate the gold price.")

    # Inputs
    oil_close = st.number_input("Oil Close Price", format="%.4f")
    nasdaq_close = st.number_input("Nasdaq Close Price", format="%.4f")
    sp500_close = st.number_input("S&P 500 Close Price", format="%.4f")
    CPI = st.number_input("CPI (Consumer Price Index)", format="%.4f")
    GDP = st.number_input("GDP Growth Value", format="%.4f")
    silver_close = st.number_input("Silver Close Price", format="%.4f")
    usd_chf = st.number_input("USD/CHF Forex Rate", format="%.4f")

    if st.button("🔮 Predict Gold Price"):
        try:
            # Validate inputs
            values = [oil_close, nasdaq_close, sp500_close, CPI, GDP, silver_close, usd_chf]
            if any(v == 0 for v in values):
                st.warning("⚠️ Please enter valid non-zero values.")
            else:
                input_data = np.array([values])
                prediction = model.predict(input_data)[0]

                st.success(f"✅ Predicted Gold Price: **${prediction:.2f}**")

                # Save prediction record
                st.session_state.history.append(
                    {
                        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "Oil": oil_close,
                        "NASDAQ": nasdaq_close,
                        "S&P500": sp500_close,
                        "CPI": CPI,
                        "GDP": GDP,
                        "Silver": silver_close,
                        "USD/CHF": usd_chf,
                        "Predicted Price": prediction
                    }
                )
        except Exception as e:
            st.error(f"Error: {e}")

    st.info("💡 Tip: Use real market data for better accuracy!")


# ----------------------------
# History Page
# ----------------------------
elif page == "Prediction History":
    st.title("📊 Prediction History")

    if len(st.session_state.history) == 0:
        st.warning("No predictions yet.")
    else:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df)

        # Download CSV
        csv = df.to_csv(index=False)
        st.download_button("⬇️ Download History CSV", csv, "prediction_history.csv")


# ----------------------------
# About Page
# ----------------------------
elif page == "About":
    st.title("ℹ️ About This App")
    st.write("""
    This Gold Price Predictor uses a trained **Random Forest Machine Learning Model**  
    to estimate gold prices based on financial market indicators.

    **Features:**
    - Realtime Prediction
    - Financial Inputs UI
    - Beautiful UI Design
    - Downloadable Prediction Logs
    - Fast, Simple & Accurate

    Developed using:
    - Python
    - Scikit-Learn
    - Streamlit
    - Joblib
    """)

    st.write("👨‍💻 Developer: **Abhishek Yaduwanshi**")
    st.write("📅 Version: 1.0.0")
