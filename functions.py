import cv2 as cv
from PIL import Image

def blur(img):
    img = cv.imread(img)
    blurredImg = cv.blur(img, (15, 15))
    print(blurredImg)
    newImage = Image.fromarray(blurredImg)
    newImage.save('blurredImg.png')