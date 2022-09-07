import cv2 as cv
from PIL import Image

def blur(img):
    img = cv.imread(img)
    blurredImg = cv.blur(img, (15, 15))
    newImage = Image.fromarray(blurredImg)
    newImage.save('blurredImg.png')

def grayscale(img):
    img = cv.imread(img)
    grayscaledImg = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
    newImage = Image.fromarray(grayscaledImg)
    newImage.save('grayscaledImg.png')