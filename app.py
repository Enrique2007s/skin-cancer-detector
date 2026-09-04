# set env variable so that protobuf uses the pure python implementation instead of the C++ implementation
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

import streamlit as st
from app_pages.multipage import MultiPage

#Load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.skin_visualizer import page_for_skn_visualizer_body
from app_pages.skin_lesion_detector import page_skin_lesion_detector_body
from app_pages.hypothesis import hypothesis_body
from app_pages.ml_performance import page_for_ml_performance_body

app = MultiPage(skin_cancer_detector="Skin Cancer Detector")

app.add_page("Summary", page_summary_body)
app.add_page("Skin Visualizer", page_for_skn_visualizer_body)
app.add_page("Skin Lesion Detector", page_skin_lesion_detector_body)
app.add_page("Hypothesis", hypothesis_body)
app.add_page("ML Performance", page_for_ml_performance_body)

app.run()