import pandas as pd
import streamlit as st
from pathlib import Path

# Paths
evaluation_path = Path("outputs") / "evaluation"


# Cached function to load evaluation data
@st.cache_data
def load_evaluation_data(evaluation_path):
    try:
        df = pd.read_csv(evaluation_path, compression='gzip')
        return df
    except FileNotFoundError:
        print(f"File not found: {evaluation_path}")
        return pd.DataFrame()