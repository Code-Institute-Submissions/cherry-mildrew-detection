import streamlit as st


def page_summary_body():
    st.header("Page summary")


    st.info(
        f"* Cherry Mildew is caused by Podosphaera clandestina, an obligate biotrophic fungus \n"
        f"* Mid- and late-season sweet cherry (Prunus avium) cultivars are commonly affected, "
        f"rendering them unmarketable due to the covering of white fungal growth on the cherry surface.\n "
        f"* Initial symptoms, often occurring 7 to 10 days after the onset of the first irrigation,are light roughly-circular "
        f"powdery looking patches on young, susceptible leaves (newly unfolded, and light green expanding leaves).\n"
        f"* [Washington State University](http://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/#:~:text=Powdery%20mildew%20of%20sweet%20and,1)"
        f"\n provides full inforamtion around the fungus."
    )


    st.warning(
        f"**Project Dataset** \n"
        f" \n The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).\n"
        f" The dataset contains +4 thousand images taken from Farmy & Foods crop fields. "
        f"The Images have been split evenly with Healthly Cherry leaves and leaves with powdery Mildew"
    )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/benlamb95/cherry-mildrew-detection/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a visual study to differentiate "
        f"a cherry leaf that contains powdery mildew or is healthy.\n"
        f"* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew "
        )
        