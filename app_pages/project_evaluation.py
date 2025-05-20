import os
import streamlit as st
import plotly.express as px
from pathlib import Path
from src.machine_learning.evaluate import load_evaluation_data


def project_evaluation_body():
    st.header("📊 Project Evaluation")
    
    st.markdown("""
    The following content of the **Project Evaluation** gives an overview of the model evaluation and an overall evaluation of the project development.
                
    Included steps from the workflow: 
    
    - Evaluation
       
    Visualisations of key evaluation components include: 

    - Confusion Matrix Final Model
    - Feature Importances Final Model
    - Performance Comparison Final Model and Model with Advanced Feature Engineering

    Please allow Streamlit a moment to run and load the visualisations. The running process is indicated at the top right.
                     
    For the conclusion of the results, please view the end of this page.
    """)

    st.markdown("These plots help explain the model development process and performance across stages.")

    figure_path = "outputs/eda/figures"

    # st.subheader("📈 Metric Comparison by Stage")
    # st.image(os.path.join(figure_path, "models_metric_stage_comparison.png"))

    st.subheader("📉 Confusion Matrix Final Model")
    st.image(os.path.join(figure_path, "final_model_confusion_matrix.png"))

    st.markdown("- The confusion matrix shows how well the final model predicts different threat levels.")

    st.subheader("📊 Feature Importances Final Model")
    st.image(os.path.join(figure_path, "final_feature_importances.png"))

    st.markdown("- The feature importances give insights into which input variables influenced predictions most.")

    # Model Performance Comparison
    st.subheader("📊 Model Performance Comparison")
    st.markdown("""
    The following section compares performance across different model development stages:
    
    - Baseline models
    - Hyperparameter-tuned models
    - Feature-engineered final model
    - Final model performance
    
    Models are evaluated using:
    - Accuracy
    - Balanced Accuracy
    - F1 Macro
    - F1 Weighted
    """)

    # --- Define CSVs and labels --- 
    evaluations = {
        "Baseline Models": Path("outputs/evaluation/model_training_results.csv.gz"),
        "🔸Hyperparameter Tuning": Path("outputs/evaluation/model_tuning_results.csv.gz"),
        "🔸Feature Engineering": Path("outputs/evaluation/best_model_fe_results.csv.gz"),
        "🏁 Test Set Model Performance": Path("outputs/evaluation/best_model_final_results.csv.gz")
    }

    # --- Streamlit Tabs --- 
    tabs = st.tabs(list(evaluations.keys()))
    
    for tab, (title, path) in zip(tabs, evaluations.items()):
        with tab:
            st.subheader(title)
            df_eval = load_evaluation_data(path)

            if df_eval.empty:
                st.warning("No data found or file not available.")
            else:
                # Melt to long format for plotly
                df_long = df_eval.melt(id_vars='Model', 
                                       var_name='Metric', 
                                       value_name='Score')

                # Create grouped bar plot
                fig = px.bar(df_long, 
                             x='Model', 
                             y='Score', 
                             color='Metric', 
                             barmode='group',
                             title=f"{title} - Model Comparison",
                             height=500)

                fig.update_layout(yaxis=dict(title="Score", range=[0, 1]))
                st.plotly_chart(fig)

                st.caption("Higher scores indicate better model performance. Balanced Accuracy and F1 scores help when handling class imbalance.")

    # General Development Evaluation 
    st.info(
        f"**Development Process**\n"
        f"* The development process followed the CRISP-DM workflow: Business Understanding, Data Understanding, Data Preparation, Modelling, Evaluation and Deployment\n"
    )

    # Evaluation Conclusions
    st.warning(
        f"**Conclusions of Evaluation**\n"
        f"* The final model works with a balanced accuracy of 45%, which is not enough.\n"
        f"* Advanced feature engineering on the final model worsened the performance.\n"
        f"* Running the final model against the raw test set data showed an even worse performance - this is due to the high imbalance in the raw test set.\n"
        f"* For the model to work somewhat accurately, it needs to be trained with a balanced test set.\n"
        f"* Because of the current best performance with resampled data, it can be said that the model can not very well generalise actual class distributions from raw, unseen data.\n"
    )

    # Business Requirements and Hypotheses Conclusions
    st.success(
        f"**Answers to Business Requirements and Hypotheses**\n"
        f"* The final model delivers a functional prototype for class-based malware classification, but does not meet real-world readiness standards due to limited generalization and low balanced accuracy.\n"
        f"* Hypothesis regarding feature-driven classification was validated, though not with high predictive power; key features remain consistent indicators of class but are insufficient alone for robust classification.\n"
        f"* Probability-based outputs offer insight into potential thresholds, but real-world decision-making would require more reliable probability calibration and expert-driven tuning.\n"
    )
