clc;close all;clear variables;

%On récupère les 6 images et leur taille
images={'i1.tif','i2.tif','i3.tif','i4.tif','i5.tif','i6.tif'};
m=length(images);
im1=imread(char(images(1)));
[h,w]=size(im1);

% matrice de m images
I=zeros(h,w,m);
for k=1:m
    I(:,:,k)=im2double(imread(char(images(k))));
end

%Matrice de données
Y = reshape(I,h*w,m);

%Matrice de données centrées
X = Y - ones(h*w,1)*mean(Y); 

%Matrice de covariance
M = X'*X./(h*w);

%Diagonalisation de la matrice de covariance, lambda contient les valP et P
%les vecP
[P,lambda] = eig(M);
lambda = flipud(diag(lambda));
P = fliplr(P);

%Matrice des composantes principales
Xstar = X*P;

%Calcul du taux d'inertie
tau = 100*lambda/(sum(lambda));

%Choix de l'axe factoriel à utiliser pour la reconstruction
axe = 1;

%Reconstruction
image_recons = reshape(Xstar(:,axe),h,w);

%Partie graphique
figure(1)
for i = 1:m
    subplot (2,3,i)
    imshow(I(:,:,i))
end
sgtitle('6 images d''origine')

figure(2);
plot(lambda,'-*');
axis([0 7 0 0.03]);
grid on;
title('Valeurs propres de la matrice de covariance');

figure(3)
plot(tau,'-*')
title('Inertie expliquée par les axes factoriels')
for k = 1:m
   text(k,tau(k),[num2str(tau(k)),'%'])
end
figure(4)
subplot 121
imshow(I(:,:,axe))
title(sprintf('image %d d''origine',axe))
subplot 122
imshow(image_recons,[]);
title(sprintf('image reconstruite'));

%Décommenter le code de la figure 5 pour afficher toutes les images
%reconstruites dans un même plot

% figure(5);
% for axe = 1:m
%    subplot(2,3,axe)
%    image_recons = reshape(Xstar(:,axe),h,w);
%    imshow(image_recons,[])
%    title(sprintf('Axe factoriel : %d', axe))
% end









