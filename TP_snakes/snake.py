import numpy as np
from matplotlib import pyplot as plt
from scipy import sparse as sp
import cv2

#Récupération de l'image en nuances de gris
image = cv2.imread('imagesTP/im_goutte.png', 0)
len_x = len(image)
len_y = len(image[0])
#Calcul de la norme du gradient de l'image
gradx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
grady = cv2.Sobel(image, cv2.CV_64F, 0, 1)
grad = cv2.Sobel(image, cv2.CV_64F,1,1)
grad_norm = gradx**2+grady**2

#Initialisation des paramètres
alpha = 1
beta = 1
gamma = 1
K = len_y


#Initialisation de notre snake
c = np.zeros((2,K))

for i in range(K):

    c[0][i] = len(image[0])/2 * (1 +0.8* np.cos(i/K*2*np.pi))

    c[1][i] = len(image)/2 * (1 +0.8* np.sin(i/K*2*np.pi))


len_c = len(c[0])
#Initialisation de la matrice D2
D2 = sp.diags([1,1, -2, 1,1], [-(len_c-1),-1, 0, 1,len_c-1], shape=(len_c,len_c))

#Initialisation de la matrice D4
D4 = sp.diags([-4,1,1,-4,6,-4,1,1,-4],[-(len_c-1),-(len_c-2),-2,-1,0,1,2,len_c-2,len_c-1],shape = (len_c,len_c))

#Calcul de la matrice A
D = alpha * D2 - beta * D4
A = np.linalg.inv(np.eye(len_c)-D)

#Définition des vecteurs x et y
x = c[0][:]
y = c[1][:]

i = 0

im_inter = np.zeros((len(grad_norm),len(grad_norm[0])))

while i < 1:
    for p in range (0,len(x)):
       for q in range(0,len(y)):
           if grad_norm[int(np.round(y[p]))][int(np.round(x[q]))] == 1: 
                im_inter[int(np.round(y[p]))][int(np.round(x[q]))] = 1
    
    x = (x+gamma*(cv2.Sobel(im_inter**2, cv2.CV_64F, 1, 0)))
    y = (y+gamma*(cv2.Sobel(im_inter**2, cv2.CV_64F, 0,1)))

    i+=1



#Partie graphique
plt.subplot(121)
plt.imshow(grad,'gray')
plt.subplot(122)
plt.plot(x,y)
plt.imshow(grad_norm,'gray')
plt.show()

