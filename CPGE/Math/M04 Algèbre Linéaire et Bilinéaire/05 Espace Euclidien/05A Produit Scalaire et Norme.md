## Produit Scalaire
```ad-note
title: Espace Préhilbertien, Espace Euclidien, Produit Scalaire, Norme
Soit $E$ muni d'une *forme bilinéaire symétrique* $f$ où $f$ est
- *positif*, $\forall x \in E,\; f(x,x) \geq 0$
- *définie*, $\forall x\in E,\; f(x,x)=0 \implies x=0_{E}$

Donc, $E$ est dite **Espace Préhilibertien**, si $E$ est de dimension finie, elle est dite **Espace Euclidien**.
En même temps, $f$ est dite **Produit Scalaire**.
On note pour $f$ un **produit scalaire** et sa **norme** : $$f(x,y) = <x,y>,\quad f(x,x)=\Vert x\Vert ^2$$
```

Exemples : 
1. $f(x,y)=\sum_{i=1}^nx_{i}y_{i}$ sur $\mathbb{R}^n$
2. $f(A,B) = \mathrm{tr}(^tAB)$ sur $\mathrm{M}_{n}(\mathbb{R})$
3. $\varphi(f,g)=\int _{a}^b f(t)g(t) \, \mathrm{d}x$ sur $\mathcal{C}([a, b], \mathbb{R})$

Proposition : On souvent calcule le **produit scalaire** à l'aide de la **norme** : $$\forall(x,y)\in E^2,\;<x,y> = \frac{1}{2}(\Vert x+y\Vert ^2-\Vert x\Vert ^2-\Vert y\Vert^2 )=\frac{1}{4}(\Vert x+y\Vert ^2-\Vert x-y\Vert ^2)$$
```ad-note
title: Norme, Espace Normé
Les **norme** $N$ vérifiant les propriétés :
- $\forall x\in E,\;N(x)=0 \iff x=0$
- $\forall x\in E,\;N(\lambda x) = |\lambda|N(x)$
- $\forall(x,y)\in E^2,\; N(x+y) \leq N(x)+N(y)$
Dans ce case $(E,N)$ est un **espace normé**.
```

- Exemple : $\forall x\in \mathbb{R}^n,\Vert x\Vert_{\infty} = \mathrm{sup}_{1 \leq i\leq n}|x_{i}|$

## Inégalité de Cauchy-Schwarz
```ad-note
title: Inégalité de Cauchy-Schwarz
Théorème : Soit $E$ muni d'une forme bilinéaire symétrique positive, alors on a $$\forall(x,y)\in E^2,\;|f(x,y)| \leq \sqrt{ f(x,x) }\sqrt{ f(y,y) }$$c'est-à-dire $$\forall(x,y)\in E^2, \; |<x,y>| \leq \Vert x\Vert \Vert y\Vert$$
L'égalité est prise lorsque $x$ et $y$ est lié.
```

Exemple : $$|\sum_{i=0}^\infty x_{i}y_{i}| \leq \left( \sum_{i=1}^nx_{i}^2 \right)^{\frac{1}{2}} \left( \sum_{i=1}^ny_{i}^2 \right)^{\frac{1}{2}}$$
