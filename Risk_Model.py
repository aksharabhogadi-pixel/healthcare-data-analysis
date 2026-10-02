import streamlit as st
import pandas as pd
import joblib

model = joblib.load("risk_model.pkl")

st.title("Healthcare Risk Prediction Model")

age = st.number_input(
    "Enter Age:",
    min_value=0,
    max_value=120,
    value=30
)

Test1 = st.number_input(
    "Enter Blood Sugar Level:",
    min_value=0,
    max_value=500,
    value=100
)

Test2 = st.number_input(
    "Enter Cholesterol Level:",
    min_value=0,
    max_value=500,
    value=150
)

# Count abnormal test results
abnormal_count = 0

if Test1 > 120:
    abnormal_count += 1

if Test2 > 200:
    abnormal_count += 1

st.write("Number of abnormal test results:", abnormal_count)


# Predict risk
if st.button("Predict Risk"):

    HighRisk = 1 if age > 65 or Test1 > 120 or Test2 > 200 else 0

    input_data = pd.DataFrame({
        "Age": [age],
        "HighRisk": [HighRisk]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        risk = "High Risk"
    else:
        risk = "Low Risk"

    st.write("Predicted Risk Level:", risk)