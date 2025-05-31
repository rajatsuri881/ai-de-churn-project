import streamlit as st
import pandas as pd
import joblib

# Load model and feature list
model = joblib.load("../model/churn_logistic_model.pkl")
df = pd.read_csv("../data/ml_ready_churn.csv")
features = df.drop("Churn", axis=1).columns.tolist()

st.title("📊 Customer Churn Predictor")

# Input values
input_data = {}
for feature in features:
    if 'Yes' in feature or 'No' in feature or feature.startswith('gender_') or feature.startswith('Contract_'):
        input_data[feature] = st.selectbox(f"{feature}", [0, 1])
    else:
        input_data[feature] = st.number_input(f"{feature}", value=0.0)

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]
    st.markdown(f"### 🔮 Prediction: {'Churn' if prediction == 1 else 'No Churn'}")
    st.progress(prob)
    st.write(f"Churn Probability: {prob:.2%}")