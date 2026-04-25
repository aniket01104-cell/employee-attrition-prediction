import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Attrition Predictor", layout="wide")
model= joblib.load("attrition_model.pkl")
# scaler = joblib.load("scaler.pkl")
training_columns = joblib.load("training_columns.pkl")
st.title("Employee Attrition Prediction System")
st.markdown("Predict employee churn risk using machine learning.")
st.sidebar.header("Enter Employee Details")

 

age = st.sidebar.number_input("Age", 18,60,30)
monthly_income = st.sidebar.number_input("Monthly Income", 1000, 50000, 5000)
daily_rate = st.sidebar.number_input("Daily Rate", 100, 1500,500)
distance = st.sidebar.number_input("Distance From Home", 1,30,5)
education = st.sidebar.slider("Education Level",1,5,3)
env_sat = st.sidebar.slider("Environment Satisfaction",1,4,3)
hourly_rate = st.sidebar.number_input("Hourly Rate", 10, 200,50)
job_involve = st.sidebar.slider("Job Involvement",1,4,3)
worklife = st.sidebar.slider("Work Life Balance",1,4,3)
total_years = st.sidebar.number_input("Total Working Years", 0,40,10)
years_at_company = st.sidebar.number_input("Years at Company", 0,40,5)
job_satisfaction = st.sidebar.slider("Job Satisfaction",1,4,3)
overtime = st.sidebar.selectbox("OverTime", ["Yes", "No"])
job_role = st.selectbox("Job Role", ["Sales Executive", "Research Scientist","Laboratory Technician", "Manufacturing Director","Healthcare Representative", "Manager",
"Sales Representative", "Research Director","Human Resources"])


input_df = pd.DataFrame({"Age": [age],"Monthly Income" : [monthly_income],"DailyRate":[daily_rate],"DistanceFromHome": [distance],
"Education": [education],"EnvironmentSatisfaction": [env_sat],"HourlyRate": [hourly_rate],"JobInvolvement":[job_involve],
"WorkLifeBalance" : [worklife],"TotalworkingYears" : [total_years],"YearsAtCompany" : [years_at_company],"JobSatisfaction":[job_satisfaction],
"OverTime": [overtime],"JobRole": [job_role]})

 
input_df = pd.get_dummies(input_df, drop_first=True)
input_df =input_df.reindex(columns=training_columns, fill_value=0)

 

# num_cols = scaler.feature_names_in_

 

# input_df[num_cols] = scaler.transform(input_df[num_cols])

st.subheader("Prediction")

 

if st.button("Predict Attrition"):
  prob = model.predict_proba(input_df) [0][1]
  percent = int(prob*100)
  st.progress(percent)
  st.metric("Attrition Probability", f"{percent}%")

  if prob>0.6:
   st.error("High Risk Employee")

  elif prob>0.3:
   st.warning("Medium Risk Employee")

  else:
   st.success("Low Risk Employee")
   st.markdown("---")
   st.caption("ML Model: Logistic Regression | Built with Streamlit")