Je rappelle que l'objectif des Td-Tps est multiple
1. Vérifier qu'on a bien compris les notions mathématiques
1. S'assurer qu'on sait utiliser `Python` pour faire les calculs utiles
1. Apprendre à coordonner les réflexions mathématiques et les calculs informatiques.

## Exercice : Utilisation de la dualité
On considère l'espace vectoriel $E=\mathscr{C}\left([a,b],\mathbb{R}\right)$ où $(a,b)\in\mathbb{R}^2$ et $a<b$. Soit $c\in]a,b[$, on définit les 4 formes linéaires de $E^\star$ suivantes
$$\varphi_1\;:\;f\longmapsto f(a),\quad \varphi_2\;:\;f\longmapsto f(b),\quad \varphi_3\;:\;f\longmapsto f(c) \quad\text{et}\quad\varphi_4\;:\; f\longmapsto \int_a^b f(t)\;\mathrm{d}t$$
1. À quelle(s) condition(s) nécessaire(s) et suffisante(s) ces 4 formes linéaires sont-elles indépendantes (=famille libres) dans $E^\star$ ?
2. On considère le sous-espace vectoriel de $E$ défini par  $$E_1=\mathrm{Vect}\left(\left\{x\longmapsto x^k,\;k\in\{0,\ldots,3\}\right\}\right)$$Montrer que ces 4 formes linéaires sont indépendantes dans $E_1^\star$ si, et seulement si, $c\ne \frac{a+b}2$.
3. En déduire une méthode approchée de calcul d'intégrale. *On notera $I_f$ la valeur approchée trouvée.*

### Réponse
**Question 1** Elles sont toujours indépendantes. Soit $(\alpha_1,\alpha_2,\alpha_3,\alpha_4)\in\mathbb{R}^4$ tels que
$$\sum_{k=1}^4 \alpha_k.\varphi_k=0_{_{E^\star}}$$

Si on l'applique à $f\;:\;x\longmapsto (x-a)\,(x-b)\,(x-c)\,g(t)$, où $g$ est une fonction de $E$ quelconque, on obtient
$$\alpha_4\,\int_a^b f(t)\;\mathrm{d}t=0$$
![[截屏2023-03-06 00.13.37.png]]
Donc si $c\ne\frac{a+b}2$, $\alpha_4=0$. Que se passe-t-il si $c=\frac{a+b}2$ ?
![[截屏2023-03-06 00.15.01.png]]
On trouve encore $\alpha_4=0$. une fois que $\alpha_4=0$ est connu, en appliquant successivement aux fonctions $x\longmapsto (x-a)\,(x-b)$, $x\longmapsto(x-a)\,(x-c)$ et $x\longmapsto (x-b)\,(x-c)$ on trouve que $\alpha_1=\alpha_2=\alpha_3=0$.

**Question 2** Le deuxième calcul ci-dessus n'est plus possible. Si on suppose que $c=\frac{a+b}2$, les formes linéaires sont liées. En effet ![[截屏2023-03-06 00.17.55.png]]


**Question 3** On aura donc
$$I_f=\frac{b-a}6\,\left(f(a)+2\,f\left(\frac{a+b}2\right)+f(b)\right)$$



## Exercice : Interpolation
Soit $a_1<a_2<\cdots<a_n$, $n$ réels, où $n\in\mathbb{N}^*\setminus\{1\}$. Soit $(y_1,\ldots,y_{n},z_1,\ldots,z_n)\in\mathbb{R}^{2\,n}$.
1. Montrer l'existence et l'unicité d'une fonction polynomiale $P$ de degré $\le 2\,n-1$ qui vérifie $$\forall i\in\{1,\ldots,n\},\; P(a_i)=y_i\quad\text{ et }\quad P'(a_{n+i})=z_i$$
2. Calculer $P$.

### Réponse
**Question 1** Considérons les formes linéaires définies sur $E=\mathrm{Vect}\left(\left\{x\longmapsto x^k,\; k\in\{0,\ldots,2\,n+1\}\right\}\right)$ par
1. Pour $i\in\{1,\ldots,n\}$, $\varphi_i\;:\;P\longmapsto P(a_i)$
1. Pour $i\in\{n+1,\ldots,2\,n-1\}$, $\varphi_i\;:\;P\longmapsto P'(a_i)$
- *Ces formes linéaires sont indépendantes.* Soit $(\alpha_1,\ldots,\alpha_{2\,n-1})\in\mathbb{R}^{2\,n-1}$ tels que
$$\sum_{k=1}^{2\,n-1} \alpha_k.\varphi_k=0_{_{E^\star}}$$
Pour $j\in\{1,\ldots,n\}$, on considère la fonction polynomiale définie par
$$P_j\;:\;x\longmapsto (x-a_1)^2\cdots(x-a_{j-1})^2\,(x-a_j)\,(x-a_{j+1})^2\cdots(x-a_n)^2$$
et on calcule
$$0=\left(\sum_{k=1}^{2\,n-1} \alpha_k.\varphi_k\right)(P_j)=\alpha_{n+j}\, \prod_{k\ne j} (a_j-a_k)^2$$
donc $\alpha_{n+j}=0$ (pour tout $j\in\{1,\ldots,n\}$). On a donc
$$\sum_{k=1}^n \alpha_k.\varphi_k=0_{_{E^\star}}$$
En considérant ensuite la fonction polynomiale définie par 
$$Q_j\;:\; x\longmapsto \prod_{k\ne j}(x-a_k)$$
on obtient
$$0=\left(\sum_{k=1}^n \alpha_k.\varphi_k\right)(Q_j)=\alpha_j\,Q_j(a_j)$$
donc $\alpha_j=0$, pour tout $j\in\{1,\ldots,n\}$. La famille est bien libre.
- *Ces $2\,n-1$ formes linéaires forment une base de $E^\star$.* Car elles forment une partie libre de cardinal $2\,n-1$ dans $E^\star$ qui est de dimension $2\,n-1$.
- En considérant la base ante-duale de $(\varphi_1,\ldots,\varphi_{2\,n-1})$, que nous noterons $(R_1,\ldots,R_{2\,n-1})$, la fonction $P$ cherchée s'écrit comme combinaison linéaire de cette base, il existe donc $(\beta_1,\ldots,\beta_{2\,n-1})\in\mathbb{R}^{2\,n-1}$ tels que
$$P=\sum_{k=1}^{2\,n-1} \beta_k.R_k$$
En appliquant pour $j\in\{1,\ldots,2\,n-1\}$, la forme linéaire sur $P$, on obtient
$$\forall j\in\{1,\ldots,n\},\; \beta_j=\begin{cases} y_j&\text{si } j\le n\\ z_{j-n}&\text{si } j>n\end{cases}$$
Ce qui montre l'existence et l'unicité de $P$ qui vaut
$$\boxed{P=\sum_{k=1}^n \left(y_k.R_k+z_k.R_{n+k}\right)}$$