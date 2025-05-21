import pandas as pd
import streamlit as st
from pathlib import Path

# Paths
data_path = Path("outputs") / "data"
raw_data_path = Path("inputs") / "datasets" / "raw"


# Cache raw unprocessed dataset
@st.cache_data
def load_raw_data() -> pd.DataFrame:
    return pd.read_csv(raw_data_path / "Android_Malware.csv.gz", compression='gzip')


# Cache processed dataset
@st.cache_data
def load_prep_data() -> pd.DataFrame:
    return pd.read_csv(data_path / "Android_Malware_converted.csv.gz", compression='gzip')