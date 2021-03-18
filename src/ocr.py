import cv2
import os

# preprocessing modules
import numpy as np
from PIL import Image
import glob

# ocr modules
import pytesseract

# load images
# cv_img = []
# for img in glob.glob('../output/*.jpg'):
#    n = cv2.imread(img)
#    cv_img.append(n)

# load test image
image = cv2.imread('..output/test.jpg')


# Get grayscale image
def get_grayscale(image):

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


image.show("image")
