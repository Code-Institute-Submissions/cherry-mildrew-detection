import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation

def page_ml_performance_metrics():
    st.header("ML Performance")

    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    st.info(

        f"* train - healthy: 1472 images\n"
        f"* train - powdery_mildew: 1472 images\n"
        f"* validation - healthy: 210 images\n"
        f"* validation - powdery_mildew: 210 images\n"
        f"* test - healthy: 422 images\n"
        f"* test - powdery_mildew: 422 images\n"
    )

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")


    st.write("### Model History")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Traninig Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Traninig Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))

    st.success(
        f"**The general accuracy rate is 100%!!** "
    )