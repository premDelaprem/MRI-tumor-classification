# basic imports
import pandas as pd 
import numpy as np
import streamlit as st

# os & image imports
import os
from PIL import Image

# tensorflow
import tensorflow as tf

# Misc.
from io import BytesIO, StringIO
import tempfile

##########################
###### Import Model ######
##########################
xception = tf.keras.models.load_model("./assets/cnn_models/model2.h5")


###########################
###### Stream Lit App #####
###########################

# Model prediction function from Notebook 03
def model_prediction(file, actual):    
    original = Image.open(file)
    
    # now, perform operations on the image and convert it into a format the model will accept
    copy = original.resize((256,256)) # resize to 256x256
    copy = copy.convert('RGB') # convert to RGB (3 channels deep)
    copy = np.array(copy) / 255. # turn image into an array of matrices & rescale!
    copy = np.expand_dims(copy, axis = 0) ## this is crucial --> needed to expand the dim from (256, 256, 3) to (1, 256, 256, 3)
    # the (1) denotes the batch size, in this case the size is just 1 since 1 image is being passed
    
    # load the model and use it to predict
    prediction_prob = xception.predict(copy)
    prediction = np.argmax(prediction_prob, axis = 1)[0]
    
    # make sure this is the same set up as the model!
    classes = {0: 'notumor', 1: 'glioma', 2: 'meningioma', 3: 'pituitary'}
    
    # CHANGING 'ACTUAL' 
    actual = actual
    
    # now create a dictionary that will set the class as the key, and that class's predicted probability as the value
    class_probs = {} 
    for i in range(len(prediction_prob[0])):
        class_probs.update({classes[i] : round(prediction_prob[0][i]*100, 2)}) 
    class_probs
    
    
    # return predicted class index, predicted class name, probabilities
    return f'Predicted Class: {prediction}', f'Tumor Detected: {classes[prediction]}', f'Actual Tumor: {actual}', class_probs


# Streamlit App
def main():
    st.title("Brain Tumor Classification App")
    uploaded_file = st.file_uploader("Upload an MRI Scan here:", type="jpg")

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        #######################
        # This is not the most ideal method! --> this is my work around since I cannot extract the filepath of the uploaded image
        actual_tumor = st.text_area("Enter actual tumor:", height = 10, max_chars = 50)

        # Make predictions when the "Predict" button is clicked
        if st.button("Predict"):
            # Call your model_prediction function
            prediction, tumor_name, actual_tumor, class_probs = model_prediction(uploaded_file, actual_tumor)

            # Display predictions
            st.success(f"{tumor_name}")
            st.info(f"{actual_tumor}")

            # Display the probabilities
            st.write("Class Probabilities:")
            for class_name, prob in class_probs.items():
                st.write(f"{class_name}: {prob}%")

# Needed to run the app
if __name__ == "__main__":
    main()