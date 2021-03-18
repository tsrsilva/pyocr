import cv2
import os

#preprocessing modules
import numpy as np
from PIL import Image
import glob

#ocr modules
import pytesseract

#load images
cv_img = []
for img in glob.glob('../output/*.jpg'):
    n = cv2.imread(img)
    cv_img.append(n)
