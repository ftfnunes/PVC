'''
    Copyright 2017 by Satya Mallick ( Big Vision LLC )
    http://www.learnopencv.com
'''

import cv2
import numpy as np
import math

def distance(p1, p2):
    r = int(p1[2]) - int(p2[2])
    g = int(p1[1]) - int(p2[1])
    b = int(p1[0]) - int(p2[0])
    return math.sqrt(b*b + g*g + r*r)
def select_pixels(img, row, column):
    pixel = list(img[row, column])
    (height, width, _) = img.shape
    for i in range(height):
        for j in range(width):
            p = img[i, j]
            if distance(pixel, p) < 13:
                img[i, j] = [0, 0, 255]
    cv2.imshow('Image', img)
    pass

def click(event, column, row, flags, img):
    if event == cv2.EVENT_LBUTTONUP:
        [b, g, r] = img[row, column]
        select_pixels(img, row, column)
        print "(R, G, B) = (%d, %d, %d)" % (r, g, b)
        print "(x, y) = (%d, %d)" % (column, row)
    pass

if __name__ == '__main__':
    # Read image
    img = cv2.imread("scale.jpg", cv2.IMREAD_COLOR)

    # Display Result
    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', click, img)
    cv2.waitKey(0)