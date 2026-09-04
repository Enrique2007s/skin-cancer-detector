import streamlit as st
import matplotlib.pyplot as plt

def page_summary_body():
    st.title("General information")
    st.info( f"*Skin cancer is a type of cancer that develops in the skin cells. "
            f"It is one of the most common types of cancer worldwide, and it can be caused by various factors, "
            f"including excessive sun exposure, genetic predisposition, and certain environmental factors. "
            f"Early detection and treatment are crucial for improving outcomes and reducing the risk of complications."
        )

    st.write("If you would like more information, please visit the [Skin Cancer Foundation](https://www.skincancer.org/skin-cancer-information/) "
             "or the [International Skin Imaging Collaboration](https://www.isic-archive.com/).")


    st.write("You can also visit and read the [Project README file](https://github.com/Enrique2007s/skin-cancer-detector/blob/main/README.md)"
             " for more information about the project.")


    st.success(
        f" The project has two business requirements: \n"
        f"1. The client is interested in identifying non malignant and malignant skin cancer in patients through a machine learning application, used as a second opinion.\n"
        f"2. The client is interested in knowing if benign and malignant skin lesions can be differentiated visually."
    )