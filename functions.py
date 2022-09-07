import cv2 as cv
from PIL import Image

def blur(img):
    img = cv.imread(img)
    blurredImg = cv.blur(img, (15, 15))
    cv.imwrite('blurredImg.png', blurredImg)

def grayscale(img):
    img = cv.imread(img)
    grayscaledImg = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
    cv.imwrite('grayscaledImg.png', grayscaledImg)