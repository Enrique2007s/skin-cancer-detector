import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (load_model_and_predict,resize_input_image,plot_predictions_probabilities)

def page_skin_lesion_detector_body():
    st.info(f"The client is interested in identifying non malignant and malignant skin cancer in patients through"
             f" a machine learning application, used as a second opinion."
             f" WARNING: The model cannot accurately predict the skin lesion type, "
             f"and should not be used as a diagnostic tool. It is only for educational purposes.")

    st.write("---")

    image_file = st.file_uploader("Upload an image of a skin lesion", type=["jpg", "jpeg", "png"])

    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Resize the image
        resized_image = resize_input_image(image, (224, 224))

        # Make prediction
        version = 'v1'
        pred_prob, pred_class = load_model_and_predict(resized_image, version = version)

        # Plot prediction probabilities
        plot_predictions_probabilities(pred_prob, pred_class)

    else:
        st.warning("Please upload an image to proceed with the prediction(Image must be in jpg, jpeg, or png format).")