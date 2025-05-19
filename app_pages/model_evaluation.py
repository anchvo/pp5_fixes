import streamlit as st
from PIL import Image
import os


def model_evaluation_body():
    st.header("📊 Model Evaluation")

    st.markdown("These plots help explain the model development process and performance across stages.")

    figure_path = "outputs/eda/figures"

    # st.subheader("📈 Metric Comparison by Stage")
    # st.image(os.path.join(figure_path, "models_metric_stage_comparison.png"))

    st.subheader("📉 Confusion Matrix (Final Model)")
    st.image(os.path.join(figure_path, "final_model_confusion_matrix.png"))

    st.markdown("- The **confusion matrix** shows how well the final model predicts different threat levels.")

    st.subheader("📊 Feature Importances (Final Model)")
    st.image(os.path.join(figure_path, "final_feature_importances.png"))

    st.markdown("- The **feature importances** give insights into which input variables influenced predictions most.")