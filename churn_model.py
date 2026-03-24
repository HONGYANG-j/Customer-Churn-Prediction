import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import google.generativeai as genai
import os

# 1. Initialize the AI Brain (REPLACE WITH YOUR ACTUAL API KEY)
GOOGLE_API_KEY = "AIzaSyB3ze2WPRSaV705MSXD_kVa-pCd_PoOf5o" 
genai.configure(api_key=GOOGLE_API_KEY)
# Using the advanced Gemini model
model_llm = genai.GenerativeModel('gemini-2.5-flash')

def build_ai_retention_system():
    print("🧠 Step 1: Initiating Machine Learning Engine...")
    
    # Load data and train the predictive model (Your existing skill)
    df = pd.read_csv("data/customer_history.csv")
    X = df[['Age', 'Total_Spend', 'Months_Active']] 
    y = df['Churned']
    
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X, y)
    
    # Predict probabilities
    df['Risk_Probability'] = rf_model.predict_proba(X)[:, 1] * 100
    at_risk = df[df['Risk_Probability'] > 50].copy()
    
    print(f"🚨 ALERT: Identified {len(at_risk)} customers at high risk of churning!")
    print("🤖 Step 2: Activating LLM Agent for Personalized Retention Campaigns...\n")
    
    # 2. The Full-Stack Magic: AI generating personalized emails
    os.makedirs("data/campaigns", exist_ok=True)
    
    for index, customer in at_risk.iterrows():
        cid = customer['Customer_ID']
        age = customer['Age']
        spend = customer['Total_Spend']
        tenure = customer['Months_Active']
        
        print(f"Drafting personalized rescue email for Customer {cid}...")
        
        # Crafting the prompt for the LLM
        prompt = f"""
        You are an expert customer retention specialist for an e-commerce brand.
        Write a short, highly personalized, and empathetic email to a customer who is likely to cancel their subscription.
        
        Customer Profile:
        - Age: {age}
        - Total Lifetime Spend: ${spend}
        - Months Active: {tenure}
        
        Instructions:
        1. Acknowledge their loyalty based on their tenure and spend.
        2. Offer a specific, targeted discount code (e.g., COMEBACK20) to incentivize them to stay.
        3. Keep it under 100 words, professional yet warm. Do not include subject lines, just the body.
        """
        
        # Call the Google Gemini API to generate the text
        response = model_llm.generate_content(prompt)
        email_body = response.text.strip()
        
        # Save the AI-generated email to a text file
        with open(f"data/campaigns/email_to_{cid}.txt", "w", encoding="utf-8") as file:
            file.write(email_body)
            
    print("\n✅ MISSION ACCOMPLISHED: Automated retention emails generated successfully!")
    print("📁 Check the 'data/campaigns' folder for the results.")

if __name__ == "__main__":
    build_ai_retention_system()
