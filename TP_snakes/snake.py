#Récupération de l'image en nuances de gris
image = cv2.imread('imagesTP/im10.png', 0)
#image = cv2.GaussianBlur(im,(3,3),cv2.BORDER_DEFAULT) 

#Calcul du carré de la norme du gradient de l'image

gradx,grady = np.gradient(image)
grad_norm = np.square(gradx)+np.square(grady)


#Initialisation des paramètres
alpha = 1.5
beta = 0.00000005
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



new_grad_x = np.zeros(len(x))
new_grad_y = np.zeros(len(y))
                                                                 12,0-1        15%

