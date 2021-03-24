import numpy as np
from matplotlib import pyplot as plt
from scipy import sparse as sp
import cv2

# Image en niveau de gris
I = cv2.imread('./imagesTP/im_goutte.png', 0)
# Gradient de la norme de l'image (en x et y)
dst = cv2.Sobel(I,cv2.CV_32F,1,1)
Dx = cv2.Sobel(I,cv2.CV_32F,1,0)
Dy = cv2.Sobel(I,cv2.CV_32F,0,1)

## Paramètres du Snake
a = 1.5; #alpha
b = 0.5; #beta
g = 0.5; #gamma
K = 2*(len(I)+len(I[0])) #nombre de points du snake (périmètre image)

## Initialisation du Snake comme un cercle
c = np.zeros((2,K))
for k in range(K):
    c[0][k] = len(I[0])/2 * (1 + np.cos(k/K*2*np.pi))
    c[1][k] = len(I)/2 * (1 + np.sin(k/K*2*np.pi))


## Implémentation de l'algorithme


D2 = 0
D4 = 0

#Algorithme
D = a*D2 - b*D4
A = np.linalg.inv(I - D)
t=1
for k in range (1,K):
    while (t<1):
        c[0][k] = A * (c[0][k-1] + g*Dx*(D)^2)
        c[1][k] = A * (c[1][k-1] + g*Dy*(D)^2)
        t = t+1


## Affichage des images
plt.figure() 
plt.subplot(121) # Image 2
plt.imshow(dst, 'gray')
plt.title('Gradient Image Goutte')
plt.subplot(122)
plt.imshow(I, 'gray')
plt.plot(c[0][:],c[1][:])
plt.xlim([0,len(I[0])])
plt.ylim([len(I),0])
plt.title('Cercle initial')

plt.show()