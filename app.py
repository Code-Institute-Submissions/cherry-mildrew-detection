import streamlit as st
from app_pages.multi_page import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_leaves_visualiser import page_leaves_visualiser_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

app = MultiPage(app_name="Cherry Mildew Detector")

app.add_page("Summary of the project", page_summary_body)
app.add_page("Cherry Leaf visualiser ", page_leaves_visualiser_body)
app.add_page("Mildew Detection", page_mildew_detector_body)
app.add_page("Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML performance ", page_ml_performance_metrics)

app.run()