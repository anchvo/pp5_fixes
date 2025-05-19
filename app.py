import streamlit as st

from app_pages import multipage, project_evaluation

from app_pages.project_summary import project_summary_body
from app_pages.eda import eda_body
from app_pages.predictive_model import predictive_model_body
from app_pages.project_evaluation import project_evaluation_body

app = multipage.MultiPage(app_name="Android Malware Threat Predictor")

app.add_page("📌 Project Summary", project_summary_body)
app.add_page("🔍 Exploratory Data Analysis", eda_body)
app.add_page("🧠 Malware Threat Predictor", predictive_model_body)
app.add_page("📊 Project Evaluation", project_evaluation_body)

app.run()