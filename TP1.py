import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

I = cv.imread('smarties.png',0)
n,p = I.shape
ret,I_seuil = cv.threshold(I,245,255,cv.THRESH_BINARY)

I_dist = cv.distanceTransform(255-I_seuil, cv.DIST_L2, 5)
ret2,I_dist_seuil = cv.threshold(I_dist,10,255,cv.THRESH_BINARY)

element = np.ones((2, 17), np.uint8) 
I_ero = cv.erode(I_dist_seuil, element,iterations = 1)

num_labels,labels = cv.connectedComponents(I_ero.astype(np.uint8))

I_marquee = labels + I_seuil * (num_labels + 1) / 255



plt.subplot(2,3,1)
plt.imshow(I,'gray')
plt.title("Image d'origine en nuances de gris")
plt.subplot(2,3,2)
plt.imshow(I_seuil,'gray')
plt.title("Image seuillée")
plt.subplot(2,3,3)
plt.imshow(I_dist,'gray')
plt.title("Image de la fonction distance")
plt.subplot(2,3,4)
plt.imshow(I_dist_seuil,'gray')
plt.title("Image de la fonction distance seuillée")
plt.subplot(2,3,5)
plt.imshow(I_ero,'gray')
plt.title("Image de la fonction distance, seuillée et érodée")
plt.subplot(2,3,6)
plt.imshow(I_marquee,'jet')
plt.title("Image seuillée et marquée")
plt.show()
