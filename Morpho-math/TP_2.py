import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("imagesTP/blobs2.png",0)

dist = cv2.distanceTransform(image,cv2.DIST_L2,5)






plt.subplot(121)
plt.imshow(image,'gray')
plt.title("Image d'origine")

plt.subplot(122)
plt.imshow(dist,'gray')
plt.title("Carte des distances")

plt.show()
