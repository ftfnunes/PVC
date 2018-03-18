'''
    Copyright 2017 by Satya Mallick ( Big Vision LLC )
    http://www.learnopencv.com
'''

import cv2
import numpy as np
import math

selected_color = None

def distance(p1, p2):
    r = int(p1[2]) - int(p2[2])
    g = int(p1[1]) - int(p2[1])
    b = int(p1[0]) - int(p2[0])
    return math.sqrt(b*b + g*g + r*r)

def select_pixels(img):
    if selected_color != None:
        pixel = selected_color
        (height, width, _) = img.shape
        for i in range(height):
            for j in range(width):
                p = img[i, j]
                if distance(pixel, p) < 13:
                    img[i, j] = [0, 0, 255]
    cv2.imshow('Video', img)
    pass

def click(event, column, row, flags, img):
    global selected_color
    if event == cv2.EVENT_LBUTTONUP:
        selected_color = [b, g, r] = list(img[row, column])
        print "(R, G, B) = (%d, %d, %d)" % (r, g, b)
        print "(x, y) = (%d, %d)" % (column, row)
    pass

if __name__ == '__main__':
    # Read image
    video = cv2.VideoCapture("bars_100.avi")

    while video.isOpened():
        ret, frame = video.read()
        if ret == False:
            break
        select_pixels(frame)
        cv2.setMouseCallback('Video', click, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()