# import module
from pdf2image import convert_from_path

# Store Pdf with convert_from_path function
images = convert_from_path('path/est.pdf')

# Save pages as images in the pdf
for i in range(len(images)):

    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
