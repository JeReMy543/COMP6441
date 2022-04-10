# -*- coding: utf-8 -*-
import cv2
import numpy as np


image_encrypt = cv2.imread("imageT.png",1)

if image_encrypt is None:
    print ("the image read is None............")





def encryption(img,key):   
    return np.roll(img, key)


def decryption(img,key):   
    return np.roll(img, -key)


encrypted = encryption(image_encrypt,152)

cv2.imshow("Encrypted",encrypted)


cv2.imshow("Decrypted",decryption(encrypted,152))



cv2.waitKey(0)