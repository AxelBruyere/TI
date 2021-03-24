import numpy as np
import cv2
import matplotlib.pyplot as plt

#Récupération de l'image
image = cv2.imread("imagesTP/des.jpg",0)

plt.imshow(image,'gray')
plt.title("Image d'origine")
plt.show()
#Initialisation de l'élément structurant S
r = 10
S = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r,r))

#Ouverture de l'image avec l'élément structurant S
Im_erodee =cv2.erode(image,S,4)

#Initialisation de l'élément structurant qui servira à la reconstruction
#==> Cercle de rayon r2
r2 = 3
S2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r2,r2))


reconsi_1 = Im_erodee
reconsi = reconsi_1
plt.ion()
i = 0
while True:
    i+=1
    reconsi_1 = reconsi
    reconsi = cv2.dilate(np.minimum(reconsi,image),S2,1)
    if np.array_equal(reconsi,reconsi_1):
        break

    plt.subplot(121)
    plt.imshow(image,'gray')
    plt.title("Image d'origine")

    plt.subplot(122)
    plt.imshow(reconsi,'gray')
    plt.title("Imagi reconstruite")
    plt.show()
    plt.pause(0.1)

print("Nombre d'itérations : ",i)
