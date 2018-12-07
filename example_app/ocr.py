from PIL import Image
import pytesseract
from pytesseract import *
import argparse
import cv2
import os
print (image_to_string(Image.open('C:\ocr\testocr.png')))
#print image_to_string(Image.open('test-english.jpg'), lang='eng')