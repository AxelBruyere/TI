clc;close all;clear variables;


%Coordonnées de nos points
PX = [2,-1,3,-2,-2]';
PY = [-1,1,1,-4,3]';
PZ = [1,-1,0,1,-1]';





%Matrice de données
Y = [PX,PY,PZ];

%3 variables à 5 données : m = 3, n = 5
[m,n] = size(Y);

% %Matrice de données centrée
% meanx = mean(PX)*ones(n,1);
% meany = mean(PY)*ones(n,1);
% meanz = mean(PZ)*ones(n,1);
% X = [PX-meanx,PY-meany,PZ-meanz];

X = Y;
%Matrice de covariance
M = X'*X./m;

%Diagonalisation de la matrice de covariance, lambda contient les valP et P
%les vecP
[P,lambda] = eig(M);
lambda = flipud(eig(M));
P = fliplr(P);


I = [];
tau=[];
%Calcul de l'inertie expliquée de chaque axe factoriel
for i = 1:1:n
    I = [I,P(:,i)'*lambda(i)*P(:,i)];
    tau = [tau,lambda(i)/sum(lambda)];
end

%Matrice des composantes principales
Xstar = [X*P(:,1),X*P(:,2),X*P(:,3)];
%Les valeurs de a,b,c sont contenues par P(:,n)


%Affichage du plan 
xx = min(Y(:,1)):0.1:max(Y(:,1));
yy = min(Y(:,2)):0.1:max(Y(:,2));
[x,y] = meshgrid(xx,yy);

%surf(x,y,z)

%Partie graphique
figure(1)
subplot 221
plot3(PX,PY,PZ,'o')
grid on
title('Nuage de point de départ')
xlabel('x')
ylabel('y')
zlabel('z')
subplot 222
plot(lambda,'-o')
title('Courbe des valeurs propres')
grid on
axis tight
subplot 223
plot(Xstar(:,1),Xstar(:,2),'o')
title('Projection des points sur le plan factoriel principal')
xlabel("e1 ("+100*tau(1)+"%)")
ylabel("e2 ("+100*tau(2)+"%)")
grid on







