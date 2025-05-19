import pandas as pd
from pathlib import Path


def load_data(filename):
    data_path = Path("outputs") / "data"
    return pd.read_csv(data_path / filename)