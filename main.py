import cv2
import pytesseract
import os

imgs_path = []

def getImgs():
    for x in os.listdir('./input'):
        if x.endswith(".png"):
            imgs_path.append(x)
    print(imgs_path)
getImgs()

def ocr(img):
    text = pytesseract.image_to_string(img)
    return text

def get_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def remove_noise(img):
    return cv2.medianBlur(img, 5)

def thresholding(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def processImg(img):
    readImg = cv2.imread(img)
    readImg = get_grayscale(readImg)
    readImg = thresholding(readImg)
    readImg = remove_noise(readImg)
    return ocr(img).split('\n')

for img in imgs_path:
    with open("./output/"+'{}.txt'.format(img.rstrip('.png')), 'w') as f:
        for line in processImg("./input/"+img):
            f.write(line)
            f.write('\n')
