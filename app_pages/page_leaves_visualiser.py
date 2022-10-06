import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_leaves_visualiser_body():
    st.header("Cherry Leaf Visualiser")

    st.success(
        f"**Business Requirement 1**\n"
        f"* The client is interested to have a study to visually differentiate "
        f"a cherry leaf that contains powdery mildew or is healthy.")
    
    version = 'v1'
    if st.checkbox("Difference between average and variability in image"):
      
      avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
      avg_var_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

      st.info(
        f"* We notice the average and variability images didn't show "
        f"patterns where we could intuitively differentiate the shape of a healthy leaf to an affected one. " 
        f"The only small difference is the color pigment of the Healthy leaves would"
        f"have a much darker pigmentation in the centre. This can be seen  on the average and Variability.")

      st.image(avg_powdery_mildew, caption='Powdery mildew leaf- Average and Variability')
      st.image(avg_var_healthy, caption='Healthy leaf- Average and Variability')
      st.write("---")

    if st.checkbox("Differences between average powdery mildew and average healthy leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            f"* This again was very difficult as the difference image produced appears  "
            f"to be an all back sqaure. However on closer inspection again there is a lighter "
            f"colour/pigmentation towards the centre of the image. ")
        st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"): 
      st.write("* To refresh the montage, click on 'Create Montage' button")
      my_data_dir = 'inputs/cherryleaves_dataset/cherry-leaves'
      labels = os.listdir(my_data_dir+ '/validation')
      label_to_display = st.selectbox(label="Select label:", options=labels, index=0)
      if st.button("Create Montage"):      
        image_montage(dir_path= my_data_dir + '/validation',
                      label_to_display=label_to_display,
                      nrows=8, ncols=3, figsize=(10,25))
      st.write("---")

def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if label_to_display in labels:

    # checks if your montage space is greater than subset size
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
   

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(f"{dir_path}/{label_to_display}/{img_idx[x]}")
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)