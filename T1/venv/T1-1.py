'''
    Copyright 2017 by Satya Mallick ( Big Vision LLC )
    http://www.learnopencv.com
'''

import cv2
import numpy as np

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        pixel = param[y, x]
        print "(R, G, B) = (%d, %d, %d)" % (pixel[2], pixel[1], pixel[0])
        print "(x, y) = (%d, %d)" % (x, y)
    pass

if __name__ == '__main__':
    # Read image
    img = cv2.imread("red_eyes.jpg", cv2.IMREAD_COLOR)

    # Display Result
    cv2.imshow('Red Eyes', img)
    cv2.setMouseCallback('Red Eyes', click, img)
    cv2.waitKey(0)