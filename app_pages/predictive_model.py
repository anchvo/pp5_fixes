import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.machine_learning.predictive_analysis import make_prediction, model

class_labels = {0: "Adware", 1: "SMS Malware", 2: "Scareware", 3: "Benign"}


def predictive_model_body():
    st.header("🧠 Malware Threat Predictor")

    st.title("Threat Level Prediction by Class")

    selected_class_name = st.selectbox("Select Threat Class", list(class_labels.values()))
    selected_class_num = [k for k, v in class_labels.items() if v == selected_class_name][0]

    st.write(f"You selected: **{selected_class_name}**")

    # Load preprocessed test set features for demonstration
    X_test_scaled = pd.read_csv("outputs/data/X_test_scaled.csv")

    threat_level = make_prediction(X_test_scaled, selected_class_num)

    st.markdown(f"### Average predicted threat level for **{selected_class_name}** in test set:")
    st.metric(label="Threat Probability", value=f"{threat_level:.2%}")

    plt.figure(figsize=(8, 4))
    proba = model.predict_proba(X_test_scaled) 
    sns.histplot(proba[:, selected_class_num], bins=30, kde=True)
    plt.title(f"Distribution of predicted probabilities for {selected_class_name}")
    plt.xlabel("Predicted Probability")
    plt.ylabel("Number of Samples")
    st.pyplot(plt)