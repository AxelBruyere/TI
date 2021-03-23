import numpy as np
import cv2
import matplotlib.pyplot as plt

#Récupération de l'image en nuances de gris
image = cv2.imread("imagesTP/angiogram.png",0)

#Elément structurant S => Cercle de rayon r pixels
r = 10
S = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r,r))

#Ouverture de notre image
im_ouv =cv2.dilate(cv2.erode(image,S,1),S,1)

#Calcul du top-hat de notre image
top_hat = image - im_ouv

#Ouverture du top-hat de notre image d'origine pour un ES de rayon r2 
r2 = 3
S2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r2,r2))
ouv_th = cv2.dilate(cv2.erode(top_hat,S2,1),S2,1)


plt.subplot(221)
plt.imshow(image,'gray')
plt.title("Image d'origine")

plt.subplot(222)
plt.imshow(top_hat,'gray')
plt.title("Top-hat de notre image d'origine")

plt.subplot(223)
plt.imshow(ouv_th,'gray')
plt.title("Top-hat ouvert de notre image d'origine")

plt.show()
