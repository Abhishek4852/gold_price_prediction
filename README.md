# 🪙 Gold Price Prediction using Machine Learning & Streamlit

This project predicts **daily gold closing prices** using historical market data and multiple machine-learning models.  
It includes complete **data preprocessing, EDA, regression models, model evaluation, and a Streamlit web app** for real-time prediction.

---

## 📌 Objective

Gold price fluctuates daily due to global markets & economic indicators.  
**Goal:** Build a system that accurately predicts gold closing prices based on financial features like stock indices, currency rates & commodity prices.

---

## 📊 Dataset

- Source: [\[Kaggle\] ](https://www.kaggle.com/datasets/franciscogcc/financial-data) 
- Features include: SP500, Nasdaq, Oil, Silver, Platinum, Palladium, USD/CHF, EUR/USD, CPI, GDP, etc.  
- Target: `gold close` (daily closing price of gold)

---

## 🌐 Live Demo

🔗 **Live App:** *([link](https://gold-price-prediction-abhishek-yaduwanshi.streamlit.app/))*  

---


### Key Features Used
- SP500, Nasdaq (Stock Indices)  
- Oil, Silver, Platinum, Palladium (Commodities)  
- USD/CHF, EUR/USD (Forex Rates)  
- GDP, CPI (Economic Indicators)

---

## 🧠 Machine Learning Models Used

| Model | Status |
|------|--------|
| Linear Regression | ✅ |
| Polynomial Regression (Degree-2) | ✅ |
| Ridge Regression | ✅ |
| Lasso Regression | ✅ |
| **Random Forest Regressor** | ✅ ⭐ Best Performance |

---

### ✅ Model Performance

| Model                     | R²     | MAE     | RMSE    |
|---------------------------|--------|---------|---------|
| Linear Regression         | 0.8713 | 7.6714  | 10.3664 |
| Polynomial Regression (2) | 0.9596 | 4.3813  | 5.8061  |
| Ridge Regression          | 0.8713 | 7.6715  | 10.3663 |
| Lasso Regression          | 0.8713 | 7.6716  | 10.3660 |
| **Random Forest**         | **0.9951** | **1.2357** | **2.0220** ✅ |

📌 **Random Forest achieved the highest accuracy**

---

## 📈 Exploratory Data Analysis (EDA)

- ✅ Missing value handling  
- ✅ Correlation heatmap for feature importance  
- ✅ Scatter plots for top features  
- ✅ Distribution plots  
- ✅ Time-series line charts for price trends  

---

## 🧪 Project Features

- Real-time gold price prediction UI with Streamlit  
- User inputs multiple market parameters  
- Modular ML pipeline files  
- Trained model saved as `.pkl`  
- Jupyter notebooks for EDA & testing  

---

## 📂 Folder Structure

📦 Gold Price Prediction
│
├── data/
│ └── gold_data.csv
│
├── model/
│ └── model_training.ipynb
│
├── app.py
├── predict_gold_price.py
├── gold_price_rf_model.pkl
│
├── testing.ipynb
├── requirements.txt
└── README.md


---

## 🛠️ Tech Stack

| Category | Tools |
|--------|-------|
| Language | Python 3.12 |
| Libraries | Pandas, NumPy, Matplotlib, Seaborn |
| ML Framework | Scikit-Learn |
| UI | Streamlit |
| Model Storage | pickle |

---

## 🚀 How to Run This Project

### 1️⃣ Clone the Project
git clone https://github.com/Abhishek4852/gold_price_prediction.git
cd gold_price_prediction 

### 2️⃣ Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

Mac/Linux
python3 -m venv venv
source venv/bin/activate

### 3️⃣ Install Requirements
pip install -r requirements.txt

### 4️⃣ Run Streamlit App
streamlit run streamlit_app/app.py

---

### 🔮 Future Improvements

Add ARIMA / LSTM / Prophet for time-series forecasting

Multi-step future predictions (1 week / 1 month)

Improve UI with trend charts & real-time market feed

Deploy on cloud (Render / HuggingFace / AWS)

---

### 👤 Author

Abhishek Yaduwanshi
Machine Learning & Backend Developer

⭐ Support

If you like this project, please ⭐ star this repo on GitHub.
