import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image

if __name__ == "__main__":

    img = cv.imread(r'C:\Users\sathy\PycharmProjects\mathuCV\greenThingsRemastered.png')

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lower_range = np.array([40, 0, 0])
    upper_range = np.array([70, 255, 255])

    mask = cv.inRange(hsv, lower_range, upper_range)

    cv.imshow("img", img)
    cv.imshow("mask", mask)
    cv.imwrite(r"C:\Users\sathy\PycharmProjects\mathuCV\maskog.jpg", mask)
    cv.waitKey(0)