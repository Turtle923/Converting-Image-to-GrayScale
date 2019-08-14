import numpy as np
import cv2

import math

th1 = cv2.imread('abc2.jpg')


iar = np.array(th1)
he = iar.shape[0]
wi = iar.shape[1]
x = 0      
while (x < he):
    y = 0
    while (y < wi ):
        v = 0
        z = 0
        while(z < 3 ):        
            iar[x][y][z] = math.ceil(iar[x][y][z]/5.1)
            v = iar[x][y][z] + v
            z += 1
        iar[x][y] = v
        y += 1
    x += 1


cv2.imshow('123',iar)
#cv2.imwrite('Converted Image 1.png',iar)
print(iar)

