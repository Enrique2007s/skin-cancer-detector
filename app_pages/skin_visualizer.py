import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

my_data_dir = 'inputs/skin_cancer_dataset'
labels = os.listdir(my_data_dir + '/validation')

def page_for_skn_visualizer_body():
    st.write("### Skin Lesion Visualizer")
    st.info(f"The client is interested in knowing if benign and malignant skin lesions can be differentiated visually.")

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):

        avg_benign = plt.imread(f"outputs/{version}/avg_var_benign.png")
        avg_malignant = plt.imread(f"outputs/{version}/avg_var_malignant.png")
        st.image(avg_benign, caption='Average and Variability Image for Benign Skin Lesions')
        st.image(avg_malignant, caption='Average and Variability Image for Malignant Skin Lesions')

        st.warning(
        f"We notice the average and variability images could show a slight difference between benign and malignant skin lesions, "
        f"which could be enough to make a distinction(difference in colour between benign and malignant skin lesions)."
        f"However, this shall be left to the professionals in this area.")
        

    if st.checkbox("Difference between benign and malignant skin lesions"):
        diff_between_skin_lesions = plt.imread(f"outputs/{version}/benign_vs_malignant_difference.png")
        st.image(diff_between_skin_lesions, caption='Difference between Benign and Malignant Skin Lesions')

        st.warning(
            f"We notice the difference image could show a slight difference between benign and malignant skin lesions, "
            f"which could be enough to make a distinction(difference in colour between benign and malignant skin lesions)."
            f"However, this shall be left to the professionals in this area."
        )

    if st.checkbox("Malignant image montage"):
        malignant_montage = plt.imread(f"outputs/{version}/malignant_montage.png")
        st.image(malignant_montage, caption='Montage of Malignant Skin Lesions')

    if st.checkbox("Benign image montage"):
        benign_montage = plt.imread(f"outputs/{version}/benign_montage.png")
        st.image(benign_montage, caption='Montage of Benign Skin Lesions')
