import streamlit as st


def project_summary_body():
    st.header("📌 Project Summary")
    st.markdown("""
    Welcome to the **Android Malware Threat Predictor** dashboard!

    This project uses machine learning to predict the threat level of different types of malware on Android devices.
                
    It is an interactive project that allows users to predict their own threat level based on either malware type or advanced feature input.

    Navigate using the sidebar to explore different components of the project.
    """)

    # Glossary and dataset content
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* A **malware sample** refers to a software entity known or suspected to perform malicious actions.\n"
        f"* A **class** is a label assigned to a malware type, e.g., Adware, SMS Malware, Scareware, or Benign.\n"
        f"* A **threat level** reflects the probability that an app belongs to a specific malware class.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset contains labeled Android app samples categorized as Adware, SMS Malware, Scareware, or Benign. "
        f"Each record includes static or behavioral features extracted from app activity and system interactions."
    )

    # Hypothesis
    st.warning(
        f"**Project Hypotheses**\n"
        f"* Certain static or behavioral features in Android apps correlate with specific malware types, enabling accurate classification.\n"
        f"* A supervised classification model trained on labeled data can generalize well across malware classes.\n"
        f"* Predicted class probabilities can guide threat level assessments and real-time alerting.\n\n"
        f"Validation methods include exploratory analysis, correlation studies, feature importance evaluation, and model performance metrics "
        f"(accuracy, balanced accuracy, F1-score)"
    )

    # Business Requirements
    st.success(
        f"**Business Requirements**\n"
        f"* 1 - Understand the characteristics and distribution of malware types to prioritize threat management.\n"
        f"* 2 - Build an automated classifier to predict if an Android app is Adware, SMS Malware, Scareware, or Benign.\n"
        f"* 3 - Provide actionable insights on key features driving malware predictions to support cybersecurity strategy."
    )

    # Link to README
    st.write(
        f"* For additional details, please visit the "
        f"[Project README file](https://github.com/anchvo/pp5_android_malware_detector/blob/main/README.md)."
    )