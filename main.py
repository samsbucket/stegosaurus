"""
This project's goal is to be able to hide text into the lsb
of a random image and be able to decode the message from
said image.
"""

import cv2
coverimg = cv2.imread('coverimg.png')

#STEP 1: convert a string into binary
msg = "This is an example"
msg = ' '.join(format(ord(x), 'b') for x in msg)
print(msg)
bits = []
for x in range(len(msg)): bits.append(msg[x])

#STEP 2: receive the cover image and break into rgb bits
pix_val = list(coverimg.getdata())
print(pix_val)