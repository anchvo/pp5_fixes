import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import load_data

def eda_body():
    st.header("🔍 Exploratory Data Analysis")

    y_train = load_data("y_train.csv")

    st.subheader("Target Class Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x=y_train.values.ravel(), ax=ax)
    ax.set_xlabel("Threat Level")
    ax.set_ylabel("Count")
    st.pyplot(fig)