# import modules
import os
from pdf2image import convert_from_path

#detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)
input("Press enter to continue...")

#detect the input and output directories and print it
ipath = os.path.isdir("../input")
print ("The existence of an input directory is %s" % ipath)
input("Press enter to continue...")

opath = os.path.isdir("../output")
print ("The existence of an output directory is %s" % opath)
input("Press enter to continue...")

# Store Pdf with convert_from_path function
#try:
images = convert_from_path('../input/est.pdf', output_folder = "../output",
                            fmt = "JPEG", jpegopt = {"quality": 100})
