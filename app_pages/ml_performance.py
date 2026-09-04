import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as imread
from src.machine_learning.evaluate_clf import evaluate_clf_performance

def page_for_ml_performance_body():
    version = 'v1'
    st.write("### Machine Learning Model Performance")

    st.info(f"train, validation, and test set label frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")

    st.image(labels_distribution, caption='Label distribution for train, validation, and test sets')
    st.write('---')


    st.write("### Model Performance Metrics")
    st.write("Model performance metrics for the machine learning model used to classify skin lesions as benign or malignant.")

    col_1, col_2 = st.columns(2)
    with col_1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')

    with col_2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Loss')

st.write('---')
st.warning(
    f"From the model performance metrics, we notice that the model is performing badly in all areas."
    f"This might be due to the small dataset the model was trained on. Many different parameters were used, and this was the best result")