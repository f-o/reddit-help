import pytesseract as pyt
from PIL import Image
import cv2
import numpy as np

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_file = 'LCD-tesseract/lcd.png'

#img = Image.open(img_file)

# Optimizing the image
img = cv2.imread(img_file)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
img = cv2.medianBlur(img, 3)

# erode to fill the gaps
kernel = np.ones((6, 6), np.uint8)
img = cv2.erode(img, kernel, iterations=4)

""" display = cv2.imread(img_file, 0)
kernel = np.ones((6,6),np.uint8)
display = cv2.erode(display,kernel,iterations = 5) """

# Display the image
cv2.imshow('image', img)
cv2.waitKey(0)


# OCR
ocr_result = pyt.image_to_string(img)

print(ocr_result)