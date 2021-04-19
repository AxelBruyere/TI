import numpy as np
from matplotlib import pyplot as plt
from scipy import sparse as sp
import math
import cv2


#Récupération de l'image en nuances de gris
image = cv2.imread('imagesTP/im_goutte.png', 0)
#image = cv2.GaussianBlur(im,(3,3),cv2.BORDER_DEFAULT) 

#Calcul du carré de la norme du gradient de l'image et passage en image binaire

gradx,grady = np.gradient(image)
grad_norm = np.square(gradx)+np.square(grady)
ret,grad_thresh = cv2.threshold(grad_norm,10,245,cv2.THRESH_BINARY)

#Initialisation des paramètres
alpha = 1.5
beta = 0.5
gamma = 0.01
L_snake = 1000

#Initialisation de notre snake
x = []
y = []

for i in range(L_snake):

    x.append(len(image[0])/2 + len(image)/2.5 * math.cos(i*2*np.pi/L_snake))
    y.append(len(image)/2 + len(image)/2.5 * math.sin(i*2*np.pi/L_snake))

#Initialisation de la matrice D2
D2 = sp.diags([1,1, -2, 1,1], [-(L_snake-1),-1, 0, 1,L_snake-1], shape=(L_snake,L_snake)).toarray()

#Initialisation de la matrice D4
D4 = sp.diags([-4,1,1,-4,6,-4,1,1,-4],[-(L_snake-1),-(L_snake-2),-2,-1,0,1,2,L_snake-2,L_snake-1],shape = (L_snake,L_snake)).toarray()

#Calcul de la matrice A
D = alpha * D2 - beta * D4
A = np.linalg.inv(np.eye(L_snake)-D)


#initialisation des différents gradients 
grad_norm_x,grad_norm_y = np.gradient(grad_thresh)
grad_int_x = np.zeros(len(x))
grad_int_y = np.zeros(len(y))

plt.ion()

for i in range (30000):
    for p in range (L_snake):
		#Mise à jour du gradient intermédiaire
        grad_int_x[p]=grad_norm_x[int(y[p])][int(x[p])]
        grad_int_y[p]=grad_norm_y[int(y[p])][int(x[p])]
	#Mise à jour de x et y
    x = np.dot(A, x + gamma * grad_int_x)
    y = np.dot(A, y + gamma * grad_int_y)
    
	#On efface les anciens x,y et on trace les nouveaux 
    if i%2000 == 0:
        plt.clf()
        plt.imshow(image,'gray')
        plt.plot(x,y)
        plt.title("Snake après %d itérations" %i)
        plt.pause(0.01)
                     
plt.show()
