clear; close; clc;
%%--Analyse en Composantes Principales--%%

%%Individus (n)
P1=[ 2,-1, 1];
P2=[-1, 1,-1];
P3=[ 3, 1, 0];
P4=[-2,-4, 1];
P5=[-2, 3,-1];
%%Variables (m)
Px=[P1(1),P2(1),P3(1),P4(1),P5(1)];
Py=[P1(2),P2(1),P3(2),P4(2),P5(2)];
Pz=[P1(3),P2(3),P3(3),P4(3),P5(3)];

%%Matrice des donnees 
Y=[P1;P2;P3;P4;P5];
[n,m]=size(Y);
%%Matrice des donnees centrees 
X=Y-mean(Y); 
%%Matrice de covariance
M=1/n*(X'*X);
%%Diagonalisation de M
[P,lambda]= eig(M);
lambda = sort(diag(lambda),'descend');
P=fliplr(P);
%%Taux d'inertie de chaque colonne
tau = zeros(1,m);
for j=1:m
    tau(j) = lambda(j)/sum(lambda);
end
%%Matrice associee au nouveau nuage de points
Xstar = X*P;

%%Affichage en nuagede points
figure(1)
hold on
subplot(121)
plot3(Px,Py,Pz,'*');
axis([-4 4 -4 4 -2 2])
xx=min(Y(:,1)):0.1:max(Y(:,1));
yy=min(Y(:,2)):0.1:max(Y(:,2));
[x,y]=meshgrid(xx,yy);
z=ones(size(x))*lambda(3);
surf(x,y,z);
view(-60,60);
grid on;
subplot(122)
plot(Xstar(:,1),Xstar(:,2),'o');
axis([-8 10 -6 6])
grid on;

%%Affichage des valeurs propres (ordre decroissant)
figure(2)
plot(lambda,'-*')
xlim([0 4])




