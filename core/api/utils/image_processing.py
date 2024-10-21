import cv2

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
