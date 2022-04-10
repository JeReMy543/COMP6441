import cv2
import numpy as np


image_encrypt = cv2.imread("imageT.png",1)

height = image_encrypt.shape[0]
width = image_encrypt.shape[1]

if image_encrypt is None:
    print ("the image read is None............")

key = np.random.randint(0,255,size = [height,width], dtype=np.uint8);



image_encrypt_B= image_encrypt[:,:,0]

image_encrypt_G= image_encrypt[:,:,1]

image_encrypt_R= image_encrypt[:,:,2]

encrypted_B = cv2.bitwise_xor(image_encrypt_B,key)
encrypted_G = cv2.bitwise_xor(image_encrypt_G,key)
encrypted_R = cv2.bitwise_xor(image_encrypt_R,key)
encrypted = cv2.merge([encrypted_B,encrypted_G,encrypted_R])

cv2.imshow("encrypted",encrypted)

decrypted_B = cv2.bitwise_xor(encrypted_B,key)
decrypted_G = cv2.bitwise_xor(encrypted_G,key)
decrypted_R = cv2.bitwise_xor(encrypted_R,key)
decrypted = cv2.merge([decrypted_B,decrypted_G,decrypted_R])


cv2.imshow("decrypted",decrypted)

cv2.waitKey(0)

#cv2.imwrite("Key.png",key)