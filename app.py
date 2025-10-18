import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the saved pipeline (which includes preprocessing + trained model)
preprocess=joblib.load("preprocessor (2).joblib")
model=joblib.load("log_reg_model (2).joblib")

st.title("Bank Marketing Campaign Prediction App")
st.write("Predict whether the client will subscribe to a term deposit (y).")

# ---- User Inputs ----

campaign = st.number_input("Number of contacts performed during this campaign", min_value=0, step=1)
pdays = st.number_input("Number of days since last contact (-1 means never)", value=-1, step=1)
previous = st.number_input("Number of contacts performed before this campaign", min_value=0, step=1)
cons_conf_idx = st.number_input("Consumer confidence index", value=-40.0)

job = st.selectbox("Job Type", [
    'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 
    'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'
])

marital = st.selectbox("Marital Status", ['married', 'single', 'unknown'])
education = st.selectbox("Education Level", [
    'basic.6y', 'basic.9y', 'high.school', 'illiterate', 
    'professional.course', 'university.degree', 'unknown'
])

default = st.selectbox("Default", ['unknown', 'yes'])
contact = st.selectbox("Contact Type", ['telephone'])
month = st.selectbox("Month", ['aug', 'dec', 'jul', 'jun', 'mar', 'may', 'nov', 'oct', 'sep'])
day_of_week = st.selectbox("Day of Week", ['mon', 'thu', 'tue', 'wed'])
poutcome = st.selectbox("Previous Outcome", ['nonexistent', 'success'])

# ---- Combine into DataFrame ----
input_df = pd.DataFrame({
    'campaign': [campaign],
    'pdays': [pdays],
    'previous': [previous],
    'cons.conf.idx': [cons_conf_idx],
    'job': [job],
    'marital': [marital],
    'education': [education],
    'default': [default],
    'contact': [contact],
    'month': [month],
    'day_of_week': [day_of_week],
    'poutcome': [poutcome]
})

st.subheader("Input Summary:")
st.write(input_df)

# ---- Prediction ----
if st.button("Predict"):
    
    processed_df = preprocess.transform(input_df)
    prediction = model.predict(processed_df)
    output = "Yes" if prediction[0] == 1 else "No"
    st.success(f"Prediction: The client will subscribe? → {output}")
