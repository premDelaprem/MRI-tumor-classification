# Overview
The contents of this repo are designed to build and train a Convolutional Neural Network model using image data of MRI brain scans. The goal is to be able to accurately classify the type of tumor, or lack thereof, associated with the image in the testing dataset. The data has been gathered by a Kaggle user, and published for public use from [this Kaggle page](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset/data). I begin by analyzing and preprocessing my image data across all 4 clases (glioma, meningioma, pituitary, and notumor). Due to hardware limitations, I build models in Google Colab using their A100 GPU to train all 3 of my basic models. After evaluating the models, I set aside the best performing (*Xception*) model and generate predictions based on testing data. The model, though simplistic, achieved an accuracy of 95%, along with precision and recall as high as 99% for 3 of the 4 classes. Additionally, I've created a streamlit web app to deploy my model that is currently still in development.

# Problem Statement
Brain tumors are collections of abnormal cells in the brain and they vary in size, shape, location, and severity. They may also be either malignant (cancerous and prone to spreading) or benign. Leaving them untreated is life threatening like any cancer and detecting brain tumors early is crucial, so the correct treatment plan can be identified to prolong the patient's life. <br>
With the emergence of machine learning tools, researchers have begun to study and develop advanced models that can assist physcians and medical professionals in the healthcare sector. Per Francois Chollet in his book, Deep Learning, even the simplest of neural network models can increase predictive accuracy substantially. <br> I work as a Biomedical Data Scientist for UW Health and want to create simple Convolutional Neural Network models to classify MRI brain scans by what brain tumor may be associated with them. The primary goal is to be able to show that these models can be complementary assets alongside Neurologists when it comes to predicting not just tumors, but a number of different neurological conditions especially if they are developed with more sophisticated architecture. I plan to build some models, discuss their performance, and generate predictions to show that CNN models can help physcians greatly. 

# Data
The data has been put together by a Kaggle user and it originally comes from 3 separate sources. All data is image data, and it has been split into `Training` and `Testing` folders, each containing 4 folders for the classes: "notumor", "glioma", "meningioma", and "pituitary". There are a total of 7,023 image files across all folders. <br>
All images vary in size and hue. MRI images are typically taken with or without contrast, so some images are extremely dark and others are brighter. Additionally, some of the images are in grayscale formatting, while others are in RGB. These issues are addressed and accounted for during the preprocessing stage in Notebook 01. <br> 
Here are a few examples of the MRI scans:

![Sample 1](https://github.com/premDelaprem/MRI-tumor-classification/blob/main/images/Tr-no_0020.jpg)

![Sample 2](https://github.com/premDelaprem/MRI-tumor-classification/blob/main/images/Tr-pi_0023.jpg)

# Summarizing Findings
Of the 3 models, the Xception pretrained model with a couple of Dropout layers to counter overfitting, performed the best. It achived 95% overall accuracy, and precision and recall scores as high as 99%. Perhaps the biggest limitation of the Xception model was in predicting "glioma", since the precision score for this class alone dropped to 86%. However, its overall performance is very promising and lends credence to the fact that a more advanced model that is further trained with parameters more suitable for MRI image, could perform exceptionally well. 
![Confusion Matrix - Xception Model](https://github.com/premDelaprem/MRI-tumor-classification/blob/main/graphs/cm_model2.jpeg)
The "y-axis" here is cutoff, but it represents the **actual** class. <br>
For more detailed analysis, please refer to my discussion in Notebook 02.

# Recommendations
As mentioned previously, CNN models can be extremely useful in aiding physcians and medical professionals make diagnoses in almost all fields in healthcare. Due to my personal hardware and time limitations, I was only able to train simple models. However, training an advanced model and feeding it stronger parameters, potentially some non-image data on patient demographics, may greatly improve predictive power to near human-intelligence like levels.

# Sources
1. https://www.frontiersin.org/articles/10.3389/fnhum.2023.1150120/full
2. https://www.evidentlyai.com/classification-metrics/multi-class-metrics
3. https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset/data
4. https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-023-02114-6#availability-of-data-and-materials

I also utilized Google Colab's A100 GPU to run all 3 of my CNN models. This helped reduce computing time by several hours.