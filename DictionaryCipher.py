# -*- coding: utf-8 -*-
import cv2
import random



image_encrypt = cv2.imread("imageT.png",1)

if image_encrypt is None:
    print ("the image read is None............")


encryp = {}
decryp = {}

temp = []

for i in range(0,256):
    temp.append(i);

for i in range(0,256):
    j = random.sample(temp, 1)
    decryp[j[0]]=i
    encryp[i] = j[0]   
    temp.remove(j[0])



height = image_encrypt.shape[0]
width = image_encrypt.shape[1]
channel = image_encrypt.shape[2]
            


def encryption (img):
    for i in range(0,height):
        for j in range(0,width):
              for k in range(0,channel):
                image_encrypt[i,j,k]= int(encryp[img[i,j,k]])


def decryption (img):
    for i in range(height):
        for j in range(width):
              for k in range(channel):
                img[i,j,k]=decryp[img[i,j,k]]





encryption(image_encrypt)
cv2.imshow("Encrypted",image_encrypt)
decryption(image_encrypt)
cv2.imshow("Decrypted",image_encrypt)
cv2.waitKey(0)
cv2.destroyAllWindows()

