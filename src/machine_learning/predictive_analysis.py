import joblib
import pandas as pd

model = joblib.load("outputs/ml_pipeline/default_best_model.pkl")

def make_prediction(input_df):
    # Scale or process input_df if needed before prediction
    return model.predict(input_df)[0]