import streamlit as st

st.set_page_config(page_title="Android Malware Threat Predictor", page_icon="🛡️")

import os
import matplotlib
from pathlib import Path

from app_pages import multipage
from app_pages.project_summary import project_summary_body
from app_pages.eda import eda_body
from app_pages.predictive_model import predictive_model_body
from app_pages.project_evaluation import project_evaluation_body

# Matplotlib font cache
custom_font_cache = Path("assets/matplotlib_cache")
os.environ["MPLCONFIGDIR"] = str(custom_font_cache.resolve())

# Matplotlib use headless backend
matplotlib.use("Agg")

app = multipage.MultiPage(app_name="Android Malware Threat Predictor")

app.add_page("📌 Project Summary", project_summary_body)
app.add_page("🔍 Exploratory Data Analysis", eda_body)
app.add_page("🧠 Malware Threat Predictor", predictive_model_body)
app.add_page("📊 Project Evaluation", project_evaluation_body)

app.run()