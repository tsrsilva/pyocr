import cv2
import os

# preprocessing modules
# import numpy as np
# from PIL import Image
# import glob

# ocr modules
import pytesseract

# load images
# cv_img = []
# for img in glob.glob('../output/*.jpg'):
#    n = cv2.imread(img)
#    cv_img.append(n)

# detect the current working directory and print it
path = os.getcwd()
print("The current working directory is %s" % path)
input("Press enter to continue...")

# load test image
image = cv2.imread('..output/test.jpg')

# Adding custom options
pytesseract.image_to_string('image')


# Get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255,
                         cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# apply grayscale, noise removal and thresholding
gray = get_grayscale(image)
thresh = thresholding(gray)
