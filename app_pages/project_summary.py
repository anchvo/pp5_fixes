import streamlit as st


def project_summary_body():
    st.header("📌 Project Summary")
    st.markdown("""
    Welcome to the **Android Malware Threat Predictor** dashboard!

    This project uses machine learning to classify Android apps based on their malware threat level.

    **Pipeline Overview**:
    - Data Collection
    - Feature Engineering
    - Model Tuning
    - Evaluation
    - Interactive Prediction

    Navigate using the sidebar to explore different components of the project.
    """)