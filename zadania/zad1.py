import cv2
import numpy as np

def zad1(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resized_img = cv2.resize(img_rgb,(30, 30))
    resized_img = np.expand_dims(resized_img, axis=0)
    return resized_img

img = zad1(r"data\pl_Test\0\000DK2PNLBPO9CUA-C122-F4.jpg")
print(img.shape)