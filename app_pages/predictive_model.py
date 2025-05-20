import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.machine_learning.predictive_analysis import make_prediction, model, predict_class_from_input

class_labels = {0: "Adware", 1: "SMS Malware", 2: "Scareware", 3: "Benign"}

st.header("🧠 Malware Threat Predictor")
st.markdown("""
    The following content of the **Malware Threat Predictor** allows the use of two prediction models: 
                
    - Threat Level Prediction by Class
    - Threat Prediction by Feature Input

    The prediction runs with a trained model based on Rain Forest Classification. It currently has a balanced accuracy of 45%.
                
    Please be aware that predictions can therefore not be fully accurate. 
                 
    For the conclusion of the results and additional information, please view the end of this page. 
    """)


def predictive_model_body():

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

    st.title("🎯 Threat Prediction by Feature Input")
    st.markdown("""
        Enter values for three key network features to predict the **most likely malware class** and its associated probabilities.
        """)
    
    # Input fields (floats only)
    src_port = st.number_input("Source Port", min_value=0.0, value=1234.0)
    dst_port = st.number_input("Destination Port", min_value=0.0, value=80.0)
    flow_duration = st.number_input("Flow Duration", min_value=0.0, value=50000.0)

    if st.button("Run Threat Prediction"):
        # Prepare single-row input DataFrame
        user_input_df = pd.DataFrame([{
            "Source Port": src_port,
            "Destination Port": dst_port,
            "Flow Duration": flow_duration
        }])

        # Match column order expected by the model (if needed, adjust accordingly)
        # Predict class
        predicted_class, class_probs = predict_class_from_input(user_input_df)

        predicted_label = class_labels.get(predicted_class, "Unknown")

        st.markdown(f"### 🛡️ Predicted Threat Type: **{predicted_label}**")
        st.markdown("### 🔢 Threat Probability Distribution:")
        
        # Visualize class probabilities
        proba_df = pd.DataFrame({
            "Malware Class": [class_labels[i] for i in range(len(class_probs))],
            "Probability": [round(p * 100, 2) for p in class_probs]
        })

        st.dataframe(proba_df)

        # Optional bar chart
        import plotly.express as px
        fig = px.bar(proba_df, x="Malware Class", y="Probability",
                     title="Predicted Class Probabilities", text="Probability")
        fig.update_layout(yaxis_title="Probability (%)")
        st.plotly_chart(fig)


    # Model Development
    st.info(
        f"**Model Development**\n"
        f"* Multiple models were trained to test for the best option: Linear Regression, Rain Forest, Linear SVC, XGB.\n"
        f"* Rain Forest Classification was chosen for the final model based on performance results of different types of models.\n"
        f"* The final model was tuned with feature adjustment and hyperparemeter tuning.\n"
        f"* The final model is currently based on a balanced train set accounting for high imbalance in the original dataset.\n"
    )

    # Predictive Model Conclusions
    st.warning(
        f"**Conclusions of Malware Threat Predictor**\n"
        f"* Basic functionality of the trained model exists.\n"
        f"* The model can successfully predict two different types of threat assessments.\n"
        f"* The balanced accuracy of 45% however, restrict the real world use as the predictions are made with too high inaccuracy.\n"
    )

    # Business Requirements and Hypotheses Conclusions
    st.success(
        f"**Answers to Business Requirements and Hypotheses**\n"
        f"* A predictive model was developed that allows automated threat classification into four distinct classes, supporting the client's requirement for real-time detection.\n"
        f"* Model performance reached 45% balanced accuracy, confirming that classification is possible but not yet reliable for production use — further tuning or data balancing needed.\n"
        f"* Class probability outputs for both bulk and individual predictions demonstrate the model's ability to produce risk-level outputs, partially validating the use of probability thresholds for alerting.\n"
    )