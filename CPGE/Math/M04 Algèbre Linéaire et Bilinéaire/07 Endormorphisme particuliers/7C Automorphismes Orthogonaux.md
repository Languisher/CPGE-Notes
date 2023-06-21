## Automorphisme Orthogonal
```ad-note
title: Automorphisme orthogonal d’un espace euclidien
Soit $E$ un espace vectoriel *euclidien*, on appelle **automorphisme orthogonal** tout automorphisme $f\in \mathscr{GL}(E)$ qui vérifie $$f^\star \circ f = f\circ f^\star = \mathrm{id}_{E} \iff f^{-1} = f^\star$$
On l'appelle **groupe orthogonal** de $E$, et on note $$f \in \mathscr{O}(E)$$
- **Proposition** :
	- $\forall(u,v) \in \mathscr{O}(E)^2,\; u\circ v \in \mathscr{O}(E)$
	- $\forall u \in \mathscr{O}(E), \; u^{-1}\in \mathscr{O}(E)$
- **Proposition** : les propriétés de $f\in\mathscr{O}(E)$ : pour tout $x,y \in E$
	- $\Vert f(x)\Vert=\Vert x\Vert$ *conservation de la norme*
	- $<f(x), f(y)> = <x,y>$ *conservation du produit scalaire*
	- Il existe, et quelle que soit la base *orthonormée* de $E$ $(e_{1},\dots,e_{n})$ : $(f(e_{1}),\dots f(e_{n}))$ est encore une base *orthonormée*

```

- **Remarque** : Si $s$ est une **symétrie orthogonale** associé à $p$ **projecteur orthogonal**, alors $$s^\star = s \implies s^\star \circ s = s\circ s = \mathrm{id}_{E}$$Donc, $s$ est un **automorphisme orthogonal**.

- **Propriété - Décomposition polaire** : $$\forall f\in \mathscr{GL}(E),\; \exists!\;(\rho, \theta)\in \mathscr{S}^{++}(E)\times \mathscr{O}(E),\; f= \rho \circ \theta$$Démonstration : ![[Pasted image 20230319153514.png]]

## Décrire l'ensemble des automorphismes orthogonaux
```ad-hint
title: Analyse
Soit $u \in \mathscr{O}(\mathbb{R}^2)$, on note avec $\mathscr{E} = (e_{1},\dots,e_{n})$ BON, $$M = \mathrm{Mat}(u,(e_{1},\dots,e_{n}))= \begin{bmatrix}
a&c\\b&d
\end{bmatrix}$$On a, d'après les propriétés d'une authomorphisme orthognale [[#Automorphisme Orthogonal]] : $$\begin{cases}
a^2+b^2=1 \\
c^2+d^2=1 \\
ac+bd=0
\end{cases}\implies \exists(\theta,\phi)\in\mathbb{R}^2, \begin{cases}
a=\cos\theta;\;b=\sin\theta \\
c=\cos \phi;\;d=\sin\phi
\end{cases}$$Or $$ac+bd = \cos(\theta-\phi)=0 \implies \theta-\phi = k\pi + \frac{\pi}{2},\;k \in \mathbb{Z}$$Cela implique que $$M = \begin{bmatrix}
\cos\theta&-\sin\theta \\
\sin\theta &\cos \theta
\end{bmatrix}\text{ ou } S=\begin{bmatrix}
\cos\theta &\sin\theta \\
\sin\theta  & -\cos\theta
\end{bmatrix}$$Si on applique sur $(x=r\cos\varphi,y=r\sin\varphi)$, on a $$M\begin{bmatrix}
x \\
y 
\end{bmatrix}=r\begin{bmatrix}
\cos(\theta+\varphi ) \\
\sin(\theta+\varphi)
\end{bmatrix} \text{ ou }S=M\begin{bmatrix}
1&0 \\
0&-1
\end{bmatrix}$$C'est-à-dire, **rotation** d'angle $\theta$ et **réflexion**, *composée de la symétrie orthogonale par rapport à la droite faisant un angle $\theta/ 2$ avec l'axe $\vec{{e_{1}}}$*. ![[截屏2023-03-19 16.10.01.png]] Le droite, évidemment, suffit ==$u(x)=x$==.

- Donc, comment on trouver cette droite ? On résout l'équation $Sx=x$.
```

```ad-note
title: Réflexion
Soit $E$ euclidien, $u\in \mathscr{L}(E)$ est dite **réflexion** si
- C'est une *symétrie orthogonale*, $E_{1}=\{x,\;u(x)=x\} \perp E_{2}=\{x, \;u(x)=-x\}$
- $\text{dim }E_{1}=\text{dim }E-1$

Forme matricielle: $$\mathrm{Mat}(u,(e_{1},\dots,e_{n})) = \begin{bmatrix}
1& 0 &\dots&&0 \\
0&1  \\
\vdots&& \ddots \\ 
&&&1\\
0&&&&-1
\end{bmatrix}$$
```
```ad-note
title: Décomposition d'un automorphisme orthogonal en un produit de réflexions
On peut trouver $p$ réflexions pour $f\in \mathscr{O}(E)$ telle que $$f= s_{1}\circ\dots\circ s_{p}$$avec $p$ le nombre minimal de réflexions utiles, $p_{\min{}}=\text{codim}(\{x\in E,u(x)=x\})$ 
```
