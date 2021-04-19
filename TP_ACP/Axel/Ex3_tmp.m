
clear variables;
close all;

% fichiers images
tab_images={'i1.tif','i2.tif','i3.tif','i4.tif','i5.tif','i6.tif'};
m=length(tab_images);

% taille des image
tmp=imread(char(tab_images(1)));
[H,W]=size(tmp);

% matrice de m images
I=zeros(H,W,m);

% affichage des images satellitaires
for k=1:m
    I(:,:,k)=im2double(imread(char(tab_images(k))));
    subplot(2,3,k);
    imshow(I(:,:,k));
end

% matrice des données
% ré-arrangement dans une matrice de n=H*W lignes et 6 colonnes
n=H*W;

%On récupere les données des 6 images dans Y
Y = reshape(I,n,m);
[n,m] = size(Y);

%On centre les données en enlevant la moyenne dans X
X = Y - ones(n,1)*mean(Y); 

%On calcule la matrice de covariance selon la formule:
M = (1/n)*X'*X;

%on diagonalise la matrice de covariance
Mdiag = diag(M);

%On stocke les valeurs propres dans lambda et dans P les vecteurs propres associés
[P, Lambda] = eig(M); 

%On passe Lambda en vecteur colonnes, on diag Lambda pour effectuer le flip
Lambda = fliplr(diag(Lambda));

%On calcul le taux d'inertie
tx_inertie = Lambda/(sum(Lambda));

%On calcul Xtsar la matrice des com^posantes principales
Xstar = X*P;

%on essaye de reconstruire l'image n°_
num=1;
Irec = reshape(Xstar(:,num),H,W);

%Affichage
figure(2);
plot(Lambda,'-*');
axis([0 7 0 0.03]);
grid on;
title('Valeurs propres de la matrice de covariance');

figure(3);
imshow(Irec,[]);
chaine=join(['Image finale n°',num2str(num)]);
title(chaine);