import joblib
import pandas as pd


model = joblib.load("outputs/ml_pipeline/default_best_model.pkl")


def make_prediction(X_input: pd.DataFrame, selected_class_num: int) -> float:
    """
    Given input features and selected class index, return the predicted threat level (probability).
    """
    proba = model.predict_proba(X_input)
    threat_level = proba[:, selected_class_num].mean()
    return threat_level