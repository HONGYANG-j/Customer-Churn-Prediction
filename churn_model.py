import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os

def build_and_run_model():
    print("🧠 Initiating Machine Learning Engine...")
    
    # 1. Load historical data
    data_path = "data/customer_history.csv"
    df = pd.read_csv(data_path)
    
    # 2. Define Features (X) and Target (y)
    X = df[['Age', 'Total_Spend', 'Months_Active']] 
    y = df['Churned']
    
    # 3. Train the Random Forest Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    print("✅ Model training completed successfully!")
    
    # 4. Predict churn probability for all customers
    df['Churn_Risk_Probability (%)'] = model.predict_proba(X)[:, 1] * 100
    
    # Filter customers with > 50% risk of churning
    at_risk_customers = df[df['Churn_Risk_Probability (%)'] > 50].copy()
    
    # 5. Export the actionable report
    output_path = "data/at_risk_customers_report.csv"
    at_risk_customers.to_csv(output_path, index=False)
    
    print(f"🚨 ALERT: Identified {len(at_risk_customers)} customers at high risk of churning!")
    print(f"📄 Retention hit-list generated at: {output_path}")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    build_and_run_model()
