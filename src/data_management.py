import pandas as pd
from pathlib import Path

# Paths
data_path = Path("outputs") / "data"
raw_data_path = Path("inputs") / "datasets" / "raw"


# Load raw unprocessed dataset
def load_raw_data() -> pd.DataFrame:
    return pd.read_csv(raw_data_path / "Android_Malware.csv.gz", compression='gzip')


# Load processed dataset
def load_prep_data() -> pd.DataFrame:
    return pd.read_csv(data_path / "Android_Malware_converted.csv.gz", compression='gzip')
