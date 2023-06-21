## Permutations et Groupe Symétrique
```ad-important
title: Permutation
Soit E un ensemble non vide. 
Une **permutation** de E est une bijection de E dans E.
```
- $\mathfrak S_{p}$ : l'ensemble des permutations de $[\![ 1,p ]\!]$.
- Exemple : ![[截屏2023-02-11 14.06.14.png]]
- $\text{card} \;\mathfrak S_{p}= p!$

```ad-important
title: Transposition
La **transposition** $\tau _{i,j}$ est la permutation de $\mathfrak S_{p}$ qui échange $i$ et $j$ et qui laisse stable les autres entiers.
$$
\tau_{i,j}(i) = j, \;\tau_{i,j}(j)=i
$$
```

- Toute permutation s'écrit à l'aide de transpositions.
$$
\sigma = \tau_{1}\circ\dots\tau_{r}
$$

```ad-important
title: Signature d'une permutation
On appelle signature de σ et on note
$$
\epsilon(\sigma) = {\prod_{1 \leq i \leq j\leq p}} \frac{\sigma(j)-\sigma(i)}{j-i}
$$
```
- $\epsilon$ peut être 1 ou -1 et :
$$
\epsilon(\sigma \circ \sigma') = \epsilon(\sigma)\epsilon(\sigma')
$$
- La signature d'une transposition est -1.
- Exemple (On utilise la même permutation) : ![[截屏2023-02-11 14.07.02.png]]
## Formes p-linéaires sur un espace vectoriel de dimension n
```ad-important
title: Formes $p$-linéaires
Soit $E$ un $\mathbb K$-espace vectoriel de dimension finie, soit $p$,
On appelle **forme $p$-linéaire** sur $E$ toute application :
![[截屏2023-02-11 14.09.34.png]]
On note $\mathscr L_p(E, \mathbb K)$ l'ensemble des formes $p$-linéaires sur $E$.
```
- Exemple : ![[截屏2023-02-11 14.10.22.png]]
```ad-important
title: Forme $p$-linéaire symétrique et antisymétrique
On dite $\phi \in \mathscr L_{p}(E, \mathbb K)$ est **symétrique** ou **antisymétrique** :
![[截屏2023-02-11 14.37.54.png]]
```

- Plus fréquemment, on dite : ![[截屏2023-02-11 14.39.13.png]]
- $\phi$ est <u>antisymétrique</u> ssi elle est **alternée**, càd : ![[截屏2023-02-11 14.43.51.png]]
- Si $(x_{1},\dots ,x_{p})$ est liée, alors $\phi(x_{1},\dots x_{p})=0$. Démonstration : ![[截屏2023-02-11 14.46.42.png]]
- La valeur $\phi(x_1,\dots ,x_{p})$ ne change pas en ajoutant à $x_i$ une combination linéaire de tous les $x_k$ où $\forall k\in [\![1,p]\!], \; k \neq i$

- **Dimension de l'espace des formes n-linéaires alternées** : ![[截屏2023-02-11 14.52.49.png]]

## Déterminant d'une famille de vecteurs
```ad-important
title: Déterminant d'une famille de vecteurs
Supposant $(x_{1}, \dots ,x_{n})\in E^p$, $\mathscr E=(e_{1},\dots,e_{n})$ une base de $E$, $x_{j} = \sum_{i=1}^nx_{i,j}.e_{i}$, alors on appelle **déterminant des vecteurs** $(x_{1},\dots,x_{n})$ dans la base $\mathscr E$ et on note :
$$
\det_{\mathscr E}(x_{1},\dots,x_{n}) = \sum_{\sigma \in \mathfrak S_{n}} [\epsilon(\sigma)\prod_{j=1}^nx_{{\sigma(j)},j}]
$$
```
- Exemple : ![[截屏2023-02-11 15.35.36.png]]
- $\det_{\mathscr E}$ est une forme $n$-linéaire <u>antisymétrique</u> sur $\mathscr{E}$.
- On a :
$$
\forall \phi \in \mathscr A_{n}(E),\; \phi = \phi(e_{1},\dots e_{n}).\det_{\mathscr E}
$$
- On a :
$$
\det_{\mathscr E}(e_{1},\dots ,e_{n}) = 1
$$
- Si $(x_1,\dots ,x_{n})$ est liée, alors $\det_{\mathscr E}(x_{1},\dots ,x_{n})=0$. (car $\det$ est antisymétrique)
- De même façon, La valeur $\det(x_1,\dots ,x_{p})$ ne change pas en ajoutant à $x_i$ une combination linéaire de tous les $x_k$ où $\forall k\in [\![1,p]\!], \; k \neq i$
- **Changement de base** :
$$
\det_{\mathscr B}= \det_{\mathscr B}(e_{1},\dots,e_{n}).\det_{\mathscr E}
$$
- Si $\mathscr C =(c_{1},\dots ,c_{n})$ est une base de $E$, alors : (car $\det_{\mathscr C}(c_{1},\dots,c_{n})=1$)
$$
\det_{\mathscr C}(e_{1},\dots,e_{n}) = \frac{1}{\det_{\mathscr E}(c_{1},\dots,c_{n})}
$$
## Déterminant d'une matrice carrée
```ad-important
title: Déterminant d'une matrice carrée
Il est indispensable que la matrice soit carrée.
![[截屏2023-02-11 15.59.17.png]]
```
- Exemple : ![[截屏2023-02-11 16.00.23.png]] 
- L'application $\det$ est une forme $n$-linéaire antisymétrique sur $M_{n,1}$ mais pas linéaire !
$$
(A_{1},\dots,A_{n}) \mapsto \det[A_{1}|\dots|A_{n}]
$$
- $\det(\lambda.A) = \lambda ^n\det(A)$
- On a $\det(A.B)=\det(A)\det(B)$
- $A$ est inversible ssi $\det(A)\neq 0$. En ce cas : $\det(A^{-1}) = \frac{1}{\det(A)}$
- On a : $\det(^tA)=\det(A)$

## Déterminant d'un endomorphisme
Soit $E$ est un $\mathbb K$-espace vectoriel de dimension finie, et siot $u\in\mathscr L(E)$, donc
$$
\det u=\det(\text{Mat}_{\mathscr E}(u))
$$
## Méthodes de calcul de déterminants
- Cas $A$ est triangulaire supérieure (ou inférieure), alors :
$$
\det A = \prod_{j=1}^na_{{j,j}}
$$
- Cas partie de $A$ vaut 0 :
![[截屏2023-02-11 16.16.20.png]]
- Algorithme générale : **Pivot de Gauss**
![[截屏2023-02-11 16.17.57.png]]
```ad-note
title: Mineur, Cofacteur, Comatrice
![[截屏2023-02-11 16.22.16.png]]
```
- La signe de la comatrice : ![[截屏2023-02-11 16.25.47.png]]
- Exemple : ![[截屏2023-02-11 16.28.48.png]]
- **Développement selon une ligne ou une colonne**:
Selon *la ligne* :
$$
\det A = \sum_{{j=1}}^na_{{i,j}} \;\text{Cofacteur}_{{i,j}}(A)
$$
ou *selon la colonne* :
$$
\det A = \sum_{i=1}^na_{i,j}\;\text{Cofacteur}_{i,j}(A)
$$
- Exemple : ![[截屏2023-02-11 16.29.37.png]]

- **Déterminant de Vandermonde** ![[截屏2023-02-11 16.34.05.png]]
	- Démonstration : ![[截屏2023-02-11 16.34.27.png]]
- Soit $A \in M_n$, alors : $^t\text{Com}(A).A=A.^t\text{Com(A)}=\det (A).I_{n}$
## Retour sur les systèmes linéaires
- **Système de Cramer** ![[截屏2023-02-11 16.36.50.png]]