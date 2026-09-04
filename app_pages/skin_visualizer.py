import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_for_skn_visualizer_body():
    st.write("### Skin Lesion Visualizer")
    st.info(f"The client is interested in knowing if benign and malignant skin lesions can be differentiated visually.")

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):

        avg_benign = plt.imread(f"outputs/{version}/avg_var_benign.png")
        avg_malignant = plt.imread(f"outputs/{version}/avg_var_malignant.png")