import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import load_data

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
    - Pandas Profiling Report
                
    For the conclusion of the results, please view the end of this page. 
    """)

    # EDA Content


    # Data Preparation & Data Cleaning
    st.info(
        f"**Data Preparation Steps**\n"
        f"* Convert data types to be all numerical to allow working with them.\n"
        f"* Clean column labels to get rid of whitespace to avoid issues based on typos.\n"
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
        f"* \n"
        f"* \n"
        f"* \n"
    )