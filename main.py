import cv2 as cv
import numpy
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Directory of the check
img = Image.open('C:\\')

length,width = img.size
img = img.crop((400,900,1200,1100))
img = img.convert('RGB')
nameOnCheck = numpy.array(img)
nameOnCheck = nameOnCheck[:, :, ::-1]
img.show()

text = pytesseract.image_to_string(nameOnCheck)

print(text)
