import pandas as pd
from pathlib import Path

# Paths
data_path = Path("outputs") / "data"
raw_data_path = Path("inputs") / "datasets" / "raw"


# Load raw unprocessed dataset
def load_raw_data() -> pd.DataFrame:
    return pd.read_csv(raw_data_path / "Android_Malware.csv")


# Load processed dataset
def load_prep_data() -> pd.DataFrame:
    return pd.read_csv(data_path / "Android_Malware_converted.csv")


# Load target variable for visualising class distribution
def load_target_data() -> pd.Series:
    return pd.read_csv(data_path / "y_train.csv").squeeze()