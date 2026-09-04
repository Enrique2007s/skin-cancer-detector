import streamlit as st
import matplotlib.pyplot as plt

def hypothesis_body():
    st.title("Hypothesis")

    st.info( f"*The client is interested in knowing if benign and malignant skin lesions can be differentiated visually."
            f" The hypothesis is that benign and malignant skin lesions can be differentiated visually."
            f" This hypothesis was tested by visualizing the average and variability images of benign and malignant skin lesions."
            f" If the average and variability images show a difference between benign and malignant skin lesions, "
            f"then the hypothesis is supported. However, this shall be left to the professionals in this area."
        )