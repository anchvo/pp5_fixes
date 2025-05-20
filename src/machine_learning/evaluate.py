import pandas as pd
from pathlib import Path

# Paths
evaluation_path = Path("outputs") / "evaluation"

# Load evaluation data CSV and return tidy DataFrame.
def load_evaluation_data(evaluation_path):
    try:
        df = pd.read_csv(evaluation_path)
        return df
    except FileNotFoundError:
        print(f"File not found: {evaluation_path}")
        return pd.DataFrame()