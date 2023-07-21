import cv2
import numpy as np
img_1 = np.zeros([512,512,1],dtype=np.uint8)
img_1.fill(255)
# or img[:] = 255
cv2.imshow('Single Channel Window', img_1)
print("image shape: ", img_1.shape)
cv2.rectangle(img1, (250, 60), (350, 170), (0, 255, 0), -1)
points = np.array([[100, 2], [125, 20], [179, 10], [230, 15], [50, 60]], np.int32)
points = points.reshape((-1, 1, 2))
cv2.imshow('Hanif', img1)
cv2.waitKey(0)
#cv2.destroyWindow('Hanif')

