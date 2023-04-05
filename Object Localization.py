
'''
To install cvlib package

1. open cmd
2. type pip install cvlib
3. press enter
'''

# Packages required for Streamlit web app and Image fetching
import streamlit as st
from PIL import Image
import requests

# Packages required for Localization
import cv2
import matplotlib.pyplot as plt
import cvlib as cv 
from cvlib.object_detection import draw_bbox

# Packages required for Image Classification
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

# To predict the image
def predict(image1): 
    model = VGG16()
    image = load_img(image1, target_size=(224, 224))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare the image for the VGG model
    image = preprocess_input(image)
    # predict the probability across all output classes
    yhat = model.predict(image)
    # convert the probabilities to class labels
    label = decode_predictions(yhat)
    # retrieve the most likely result, e.g. highest probability
    label = label[0][0]
    return label 


# To fetch image from the web
def get_image(url):
    img = requests.get(url)
    file = open("sample_image.jpg", "wb")
    file.write(img.content)
    file.close()
    img_file_name = 'sample_image.jpg'
    return img_file_name


# Main driver
st.title("Image Classification and Localization using YOLOv4 pretrained Model")
st.write("Using YOLOv4 Model to classify and Localize objects in the image")

url = st.text_input("Enter Image Url:")
if url:
    image = get_image(url)
    st.image(image)
    classify_and_localize = st.button("Classify and Localize image")
    if classify_and_localize:
        st.write("")
        st.write("Classifying and Localizing...")

        # To classify object in image
        label = predict(image)
        st.write('%s (%.2f%%)' % (label[1], label[2]*100))

        # To draw boundbox
        im = cv2.imread(image)
        bbox, label, conf = cv.detect_common_objects(im)
        output_image = draw_bbox(im, bbox, label, conf)
        st.image(output_image)

else:
    st.write("Paste Image URL")

