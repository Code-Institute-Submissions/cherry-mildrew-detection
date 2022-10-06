import streamlit as st

def page_project_hypothesis_body():
    st.header("Hypothesis and Validation")

    st.write(
        f"* We suspect that Cherry leaves affected by powdery mildew have a white colour/ lighter "
        f"pigmentation in the centre of the leaf compared to a healthy leaf. Also distorted edges.\n"

        f"* The Average image and Variability Image confirmed this hypothesis, "
        f" as they would show a much lighter colour within the centre of each image however; "
        f" there was no clear pattern to identify them by shape."
    )
