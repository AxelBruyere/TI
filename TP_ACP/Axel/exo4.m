clc;close all;clear variables;

image = imread('ballon.tif');
[H,W,p] = size(image);

%Matrice de donn�es
Y = zeros(H*W,p);
for k = 1:p
    A=image(:,:,k);
    Y(:,k) = A(:);
end

%Matrice de donn�es centr�e
X = Y - ones(H*W,p) .* mean(Y);

%Matrice de covariance
M = X'*X./(H*W);

%Diagonalisation de la matrice de covariance, lambda contient les valP et P
%les vecP
[P,lambda] = eig(M);
lambda = flipud(diag(lambda));
P = fliplr(P);

%Matrice des composantes principales
Xstar = X*P;

%Calcul de l'inertie expliqu�e et de son taux par chacun des axes factoriels
I = zeros(1,p);
tau = 100*lambda/sum(lambda);
for k = 1:p
    I(k) = P(:,k)'*M*P(:,k);   
end


%Reconstruction
Irec = reshape(Xstar(:,1),[H,W]);

%Partie graphique
figure(1)
subplot 121
imshow(image)
title('Image d''origine')
subplot 122
imshow(Irec)
title('Image reconstruite � partir de la premi�re composante principale')
caxis([min(min(Irec)),max(max(Irec))])