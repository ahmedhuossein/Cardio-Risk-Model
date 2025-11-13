import streamlit as st
import joblib
import numpy as np

def main():
    st.title("Cardiovascular Risk Predictor")

    st.write("Fill in the patient information below:")

    # Load model
    model = joblib.load("cardio_risk_model.pkl")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age (years)", 1, 120, step=1)
        gender = st.selectbox("Gender", [1, 2], help="1 = Female, 2 = Male")
        height = st.number_input("Height (cm)", 50, 250, step=1)
        cholesterol = st.selectbox("Cholesterol level", [1, 2, 3],
                                   help="1 = normal, 2 = above normal, 3 = well above normal")
        smoke = st.selectbox("Smoking status", [0, 1], help="0 = No, 1 = Yes")
        active = st.selectbox("Physical activity", [0, 1], help="0 = Low, 1 = Active")

    with col2:
        weight = st.number_input("Weight (kg)", 10.0, 300.0, step=0.1)
        gluc = st.selectbox("Glucose level", [1, 2, 3],
                            help="1 = normal, 2 = above normal, 3 = well above normal")
        alco = st.selectbox("Alcohol use", [0, 1], help="0 = No, 1 = Yes")
        BMI = st.number_input("BMI", 10.0, 60.0, step=0.1)
        pulse_pressure = st.number_input("Pulse Pressure", 0, 200, step=1,
                                         help="Calculate the Systolic - Diastolic BP")

    if (st.button("Predict Risk", width="stretch")):
        features = [age, gender, height, str(cholesterol), smoke, active, weight, str(gluc), alco, BMI, pulse_pressure]
        prediction = int(model.predict(features))
        if prediction == 0:
            st.success("You are NOT at risk.")
        else:
            st.error("You ARE at risk.")
        st.caption("⚠️ This tool is for educational purposes only and is **not** medical advice.")
if __name__ == '__main__':
    main()
