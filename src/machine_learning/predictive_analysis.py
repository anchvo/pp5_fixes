import pandas as pd
import compress_pickle as cpickle
import streamlit as st
from pathlib import Path


# Cache the model loading as a resource
@st.cache_resource
def load_model():
    model_path = Path("outputs/ml_pipeline/default_best_model.pkl.gz")
    return cpickle.load(model_path, compression="gzip")


# Cache the feature column loading as data
@st.cache_data
def load_feature_columns():
    return pd.read_csv("outputs/data/X_test_scaled.csv.gz", compression='gzip', nrows=1).columns.tolist()


# Predict threat level with selected class input
def make_prediction(X_input: pd.DataFrame, selected_class_num: int) -> float:
    model = load_model()
    proba = model.predict_proba(X_input)
    threat_level = proba[:, selected_class_num].mean()
    return threat_level


# Predict the malware class and probabilities from user input
def predict_class_from_input(user_input_df: pd.DataFrame):
    model = load_model()
    FEATURE_COLUMNS = load_feature_columns()

    # Create full feature row with default 0s
    full_input = pd.DataFrame(columns=FEATURE_COLUMNS)
    full_input.loc[0] = 0  # Fill with 0s

    # Overwrite selected features with actual input
    for col in user_input_df.columns:
        if col in full_input.columns:
            full_input.at[0, col] = user_input_df[col].values[0]

    # Predict
    class_probs = model.predict_proba(full_input)[0]
    predicted_class = class_probs.argmax()
    return predicted_class, class_probs