import streamlit as st
import pandas as pd
from src.machine_learning.predictive_analysis import make_prediction


def predictive_model_body():
    st.header("🧠 Malware Threat Predictor")

    st.markdown("Enter the characteristics of the app below to predict its **threat level**.")

    # Example features — replace with actual feature names
    feature_1 = st.number_input("Permission Score", min_value=0.0, value=1.0)
    feature_2 = st.number_input("App Size (MB)", min_value=0.0, value=10.0)
    feature_3 = st.number_input("Request Count", min_value=0, value=5)

    if st.button("Predict Threat Level"):
        input_df = pd.DataFrame({
            "feature_1": [feature_1],
            "feature_2": [feature_2],
            "feature_3": [feature_3]
        })

        prediction = make_prediction(input_df)
        st.success(f"Predicted Threat Level: **{prediction}**")

        st.markdown("🔐 Based on the input, you may want to **restrict permissions**, **investigate the APK**, or **flag the app for deeper analysis**.")