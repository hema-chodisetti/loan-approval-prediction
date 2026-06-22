import streamlit as st
import pandas as pd
import joblib

# Load saved model
model = joblib.load("loan_approval_model.pkl")

st.set_page_config(page_title="Loan Approval Prediction", page_icon="🏦")

st.title("🏦 Loan Approval Prediction System")
st.write("Enter applicant details to predict whether the loan will be approved or rejected.")

# User inputs
no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0)

education_input = st.selectbox("Education", ["Graduate", "Not Graduate"])

self_employed_input = st.selectbox("Self Employed", ["Yes", "No"])

income_annum = st.number_input("Annual Income", min_value=0, value=5000000)

loan_amount = st.number_input("Loan Amount", min_value=0, value=10000000)

loan_term = st.number_input("Loan Term in Years", min_value=1, max_value=30, value=10)

cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, value=700)

residential_assets_value = st.number_input("Residential Assets Value", min_value=0, value=5000000)

commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0, value=3000000)

luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0, value=2000000)

bank_asset_value = st.number_input("Bank Asset Value", min_value=0, value=1000000)

# Encode categorical values
education = 1 if education_input == "Graduate" else 0
self_employed = 1 if self_employed_input == "Yes" else 0

# Create dataframe in same order as training data
input_data = pd.DataFrame({
    "no_of_dependents": [no_of_dependents],
    "education": [education],
    "self_employed": [self_employed],
    "income_annum": [income_annum],
    "loan_amount": [loan_amount],
    "loan_term": [loan_term],
    "cibil_score": [cibil_score],
    "residential_assets_value": [residential_assets_value],
    "commercial_assets_value": [commercial_assets_value],
    "luxury_assets_value": [luxury_assets_value],
    "bank_asset_value": [bank_asset_value]
})

st.subheader("Applicant Input Data")
st.dataframe(input_data)

# Prediction
if st.button("Predict Loan Status"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")