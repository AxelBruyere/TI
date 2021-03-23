import numpy as np
import cv2
import matplotlib.pyplot as plt


#Récupération de l'image en nuances de gris

image = cv2.imread("imagesTP/Ampoule.png",0)

#Elément structurant S => Cercle de rayon r pixels
r = 12
S = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r,r))

#Calcul du gradient morphologique de notre image
grad_morph = cv2.dilate(image,S,1)-cv2.erode(image,S,1)

#Ouverture de notre image
im_ouv =cv2.dilate(cv2.erode(image,S,1),S,1)

#Calcul du gradient morphologique de notre image ouverte
grad_morph_ouv = cv2.dilate(im_ouv,S,1) - cv2.erode(im_ouv,S,1)


plt.subplot(221)
plt.imshow(image,'gray')
plt.title("Image d'origine")

plt.subplot(222)
plt.imshow(grad_morph,'gray')
plt.title("Gradient morphologique de notre image d'origine")

plt.subplot(223)
plt.imshow(im_ouv,'gray')
plt.title("Image d'origine ouverte")

plt.subplot(224)
plt.imshow(grad_morph_ouv,'gray')
plt.title("Gradient morphologique de notre image ouverte")
plt.show()
