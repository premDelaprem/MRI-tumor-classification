# Overview
The contents of this repo are designed to build and train a Convolutional Neural Network model using image data of MRI brain scans. The goal is to be able to accurately classify the type of tumor, or lack thereof, associated with the image in the testing dataset. The data has been gathered by a Kaggle user, and published for public use from [this Kaggle page](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset/data). I begin by analyzing and preprocessing my image data across all 4 clases (glioma, meningioma, pituitary, and notumor). Due to hardware limitations, I build models in Google Colab using their A100 GPU to train all 3 of my basic models. After evaluating the models, I set aside the best performing (*Xception*) model and generate predictions based on testing data. The model, though simplistic, achieved an accuracy of 95%, along with precision and recall as high as 99% for 3 of the 4 classes. Additionally, I've created a streamlit web app to deploy my model that is currently still in development.

# Problem Statement
Brain tumors are collections of abnormal cells in the brain and they vary in size, shape, location, and severity. They may also be either malignant (cancerous and prone to spreading) or benign. Leaving them untreated is life threatening like any cancer and detecting brain tumors early is crucial, so the correct treatment plan can be identified to prolong the patient's life. <br>
With the emergence of machine learning tools, researchers have begun to study and develop advanced models that can assist physcians and medical professionals in the healthcare sector. Per Francois Chollet in his book, Deep Learning, even the simplest of neural network models can do increase predictive accuracy substantially. <br> I work as a Biomedical Data Scientist for UW Health and want to create simple Convolutional Neural Network models to classify MRI brain scans by what brain tumor may be associated with them. The primary goal is to be able to show that these models can, if developed with more sophisticated architecture, be complementary assets alongside Neurologists when it comes to predicting not just tumors, but a number of different neurological conditions. I plan to build some models, discuss their performance, and generate predictions to show that CNN models can help physcians greatly.

# Data
The data has been put together by a Kaggle user and it originally comes from 3 separate sources. All data is image data, and it has been split into `Training` and `Testing` folders, each containing 4 folders for the classes: "notumor", "glioma", "meningioma", and "pituitary". There are a total of 7,023 image files across all folders. <br>
All images vary in size and hue. MRI images are typically taken with or without contrast, so some images are extremely dark and others are brighter. Additionally, some of the images are in grayscale formatting, while others are in RGB. These issues are addressed and accounted for during the preprocessing stage in Notebook 01. <br> 
Here are a few examples of the MRI scans:

![Sample 1]('./images/Tr-no_0020.jpg')

![Sample 2]('./images/Tr-pi_0023.jpg')


