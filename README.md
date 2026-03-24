# 🔮 The Churn Predictor: Machine Learning for Customer Retention

## 📊 The Business Problem
Acquiring a new customer costs 5x more than retaining an existing one. Most businesses only realize a customer is unhappy *after* they cancel their subscription. 

## 💡 The Solution
A predictive Machine Learning model (Random Forest) that analyzes historical customer behavior (spend, tenure, demographics) to identify "At-Risk" customers *before* they churn. 

## 📈 Business Impact & ROI
* **Proactive Retention:** Generates a daily "Hit List" of high-risk customers for the sales team to contact.
* **Revenue Protection:** A 5% increase in customer retention can increase company profitability by 25% to 95%.

## 🛠️ Technical Implementation
* **Algorithm:** Random Forest Classifier (`scikit-learn`)
* **Features Used:** Account Tenure, Lifetime Value (LTV), Demographic Data.
* **Output:** Actionable CSV report with probability risk scoring.

🔒 Security Note: This application requires a Google Gemini API Key. To run it locally, please set your environment variable: export GOOGLE_API_KEY="your_api_key_here".
