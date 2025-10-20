# Gold Price Prediction

Predicting daily gold closing prices using historical market data and multiple regression & machine learning models.

## 📂 Project Structure

data/ # Dataset files (raw, cleaned, processed)
notebooks/ # Jupyter notebooks for analysis and model building
src/ # Python scripts for cleaning, feature engineering, and modeling
requirements.txt # Python dependencies
README.md # Project overview


## 📊 Dataset

- Source: [Your source or mention “Collected dataset”]  
- Features include: SP500, Nasdaq, Oil, Silver, Platinum, Palladium, USD/CHF, EUR/USD, CPI, GDP, etc.  
- Target: `gold close` (daily closing price of gold)

## 🛠️ Technologies Used

- Python 3.12  
- Pandas, Numpy, Matplotlib, Seaborn  
- scikit-learn (Linear Regression, Random Forest, Ridge, Lasso)  

## 🔍 Exploratory Data Analysis

- Correlation heatmaps for feature importance  
- Scatter plots for top correlated features  
- Time series plots for gold price trends  

## 🤖 Model Training

- Linear Regression  
- Polynomial Regression (degree 2)  
- Ridge & Lasso Regression  
- Random Forest Regression  

### Model Performance

| Model                     | R²     | MAE     | RMSE    |
|----------------------------|--------|---------|---------|
| Linear Regression          | 0.8713 | 7.6714  | 10.3664 |
| Polynomial Regression (2)  | 0.9596 | 4.3813  | 5.8061  |
| Ridge Regression           | 0.8713 | 7.6715  | 10.3663 |
| Lasso Regression           | 0.8713 | 7.6716  | 10.3660 |
| Random Forest Regression   | 0.9951 | 1.2357  | 2.0220  |

Random Forest showed the highest accuracy.

## 🔮 Predicting Future Prices

- Current models can predict same-day gold prices using other market variables.  
- For next month predictions, time-series lag features or models like ARIMA, Prophet, or LSTM are recommended.

## 🚀 How to Run

1. Clone the repo:  
git clone https://github.com/Abhishek4852/gold_price_prediction.git


2. Install dependencies:
pip install -r requirements.txt

3. Run Python scripts or notebooks from notebooks/ or src/.



## 📈 Future Improvements

- Use lag features for time series forecasting

- Predict multi-step future gold prices

- Deploy as a web app with interactive charts