import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from streamlit.components.v1 import html
from src.data_management import load_prep_data, load_raw_data


def eda_body():
    st.header("🔍 Exploratory Data Analysis")

    # Page Explanation
    st.markdown("""
    The following content of the **Exploratory Data Analysis** gives an overview of the first steps of the development workflow: 
                
    - Data Understanding
    - Data Preparation

    In those steps, the dataset from Kaggle was collected, inspected and cleaned to allow working with the data. 
                
    Decisions were made based on the previously stated business requirements and hypothesis and the continous results of the data analysis.

    Visualisations of key analysis components include: 

    - Class Distribution
    - Correlation Heatmap
    - General Feature Importances Overview
    - Skewness & Missing Values

    Please allow Streamlit a moment to run and load the visualisations. The running process is indicated at the top right.
                     
    For the conclusion of the results, please view the end of this page. 
    """)

    # EDA Content
    df_prep = load_prep_data()
    df_raw = load_raw_data()

    # --- Class Distribution ---
    st.subheader("📊 Class Distribution")
    st.markdown("""
    This chart shows the distribution of malware types in the dataset, represented by the `Label` target variable.
    """)
    class_counts = df_raw['Label'].value_counts().reset_index()
    class_counts.columns = ['Malware Class', 'Count']
    fig = px.bar(class_counts, x='Malware Class', y='Count', color='Malware Class', title="Target Class Distribution")
    st.plotly_chart(fig)
    st.caption("The dataset is imbalanced, with some malware types being significantly more common than others.")

    # --- Correlation Heatmap ---
    st.subheader("🔗 Correlation Heatmap")
    st.markdown("""
    This heatmap visualizes the correlation between numeric features in the dataset.
    """)
    corr = df_prep.corr().round(2)
    fig_corr = px.imshow(corr, color_continuous_scale='Viridis', title="Feature Correlation Heatmap")
    st.plotly_chart(fig_corr)
    st.caption("There are clusters of strongly correlated features, potentially due to similar behavioral traits or data collection logic.")

    # --- Feature Importance ---
    st.subheader("🌟 General Feature Importance")
    st.markdown("""
    This plot highlights the 10 most impactful features based on their statistical correlation with the target label.
    """)
   
    # Ensure numeric-only data
    numeric_df = df_prep.select_dtypes(include='number')

    # Compute correlation with target
    correlation = numeric_df.corr()['Label_encoded'].drop('Label_encoded')
    top_corr = correlation.abs().sort_values(ascending=False).head(10)

    # Bar Plot of correlations
    fig_corr = px.bar(
        x=top_corr.index,
        y=top_corr.values,
        title="Top 10 Features Correlated with Target",
        labels={'x': 'Feature', 'y': 'Correlation Coefficient'}
    )
    fig_corr.update_layout(xaxis_title="Feature", yaxis_title="Correlation with Target")
    st.plotly_chart(fig_corr)

    st.caption("These features are the most statistically associated with the malware class and may carry high predictive value.")

    # --- Skewness and Missing Values ---
    st.subheader("📉 Skewness and Missing Values")
    st.markdown("""
    Visual summaries to evaluate skewed features and missing values.
    """)
    # Ensure only numeric columns are used for skewness
    numeric_df = df_prep.select_dtypes(include='number')
    skewed_feats = numeric_df.skew().sort_values(ascending=False).head(10)

    # Skewness Plot
    fig_skew = px.bar(
        x=skewed_feats.index,
        y=skewed_feats.values,
        title="Top Skewed Features",
        labels={'x': 'Feature', 'y': 'Skewness'}
    )
    fig_skew.update_layout(xaxis_title="Feature", yaxis_title="Skewness")
    st.plotly_chart(fig_skew)
    st.caption("Highly skewed features may need transformation or imputation techniques.")

    # Missing Values Plot
    st.markdown("### Missing Values Overview")
    missing = df_prep.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)

    if not missing.empty:
        fig_missing = px.bar(
            x=missing.index,
            y=missing.values,
            title="Missing Values by Feature",
            labels={'x': 'Feature', 'y': 'Missing Values'}
        )
        fig_missing.update_layout(xaxis_title="Feature", yaxis_title="Missing Values")
        st.plotly_chart(fig_missing)
    else:
        st.success("✅ No missing values detected in the dataset.")

    # Data Preparation & Data Cleaning
    st.info(
        f"**Data Preparation Steps**\n"
        f"* Pandas Profiling Report: Was created before and after data preparation to inspect the dataset in more detail. Due to loading issues, they could not be loaded here.\n"
        f"* Convert data types to be all numerical to allow working with them.\n"
        f"* Clean column labels to get rid of whitespace to avoid issues based on typos.\n"
        f"* Drop metadata features because of irrelevance for prediction.\n"
        f"* Handle missing data: drop features with all zero-values\n"
        f"* Handle skewed features via imputing\n"
    )

    # Analysis Conclusions
    st.warning(
        f"**Conclusions of EDA**\n"
        f"* Target variable: Label. Represents classes Adware, Spyware, SMS Adware and Benign.\n"
        f"* Dataset is highly imbalanced, which can affect model development\n"
        f"* Dataset contains a high amount of outliers, which can affect model development\n"
    )

    # Business Requirements and Hypotheses Conclusions
    st.success(
        f"**Answers to Business Requirements and Hypotheses**\n"
        f"* The dataset includes four malware categories (Adware, Scareware, SMS Malware, Benign), fulfilling the client's requirement for categorized malware analysis.\n"
        f"* Exploratory data analysis revealed distinct feature distributions across classes, suggesting that behavioral patterns of malware are present and can be leveraged.\n"
        f"* Feature correlation and importance analysis indicate that several features (e.g., flow duration, source/destination port) strongly influence class separability, supporting the hypothesis that malware behavior can be mapped via static features.\n"
    )