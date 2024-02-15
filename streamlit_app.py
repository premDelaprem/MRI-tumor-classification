# basic imports
import pandas as pd 
import numpy as np
import streamlit as st

# os & image imports
import os
from PIL import Image

# tensorflow
import tensorflow as tf

#####################################

st.set_page_config()

st.title('Classifying Brain Tumors from MRIs')

page = st.sidebar.selectbox(
    'Page',
    ('About', 'Load Image', 'Prediction')
)

if page == 'About':
    st.subheader('About this Project')
    st.write('''
        This Streamlit based app hosts my CNN model for predicting the type of brain tumor
        given an MRI Brain scan. I trained and evaluated 3 models prior to loading the best one
        in this application. The best model was a pretrained simplistic Xception model which achieved roughly
        95 percent accuracy despite not being further developed beyond its original architecture.
        
        This project is still currently under work.''')

elif page == 'Load Image':
    st.subheader('Load MRI Image')

    # Function to process the uploaded image
    def process_uploaded_image(uploaded_file):
        if uploaded_file is not None:
            # Open and display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            
            # You can perform further processing on the image here
            # For example, you can use a machine learning model to make predictions

    # Streamlit app
    def main():
        st.title("Upload Image Example")

        # Create a button for uploading the image
        upload_button = st.button("Upload Image")

        if upload_button:
            # Upload image through file uploader
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

            # Process the uploaded image
            process_uploaded_image(uploaded_file)


elif page == 'Prediction':
    st.subheader('CNN Model Prediction')



if __name__ == "__main__":
    main()