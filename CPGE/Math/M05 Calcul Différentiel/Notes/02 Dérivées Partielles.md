## Dérivées Partielles
```ad-note
title: Dérivées Partielles
- Soit $O$ un ouvert non vide de $\mathbb{R}^n$ et soit $f:O \to \mathbb{R}^p$.
- On dit que $f$ est **admet une dérivée partielle par rapport à la $j$-ième variable en** $x\in O$ si la fonction ci-dessous est dérivable en $x_{j}$ : $$t \mapsto f(x_{1},\dots,x_{j-1},t,x_{j+1},\dots ,x_{n})$$ou la fonction ci-dessous est dérivable en $0$ : ==ce que je prefère==$$t \mapsto f(x_{1},\dots,x_{j-1},x_{j}+t,x_{j+1},\dots,x_{n})$$
- *Le vecteur dérivée de $\mathbb{R}^p$ obtenu*, on note : $$\frac{\partial f}{\partial x_{j}}(x) \text{ ou } \partial_{j}f(x)$$
- On définit la **$j$-ième dérivée partielle de $f$** par $$\partial_{j}f:\begin{cases}
O &\to \mathbb{R}^p \\
x &\mapsto \partial_{j}f(x)
\end{cases}$$
```

```ad-caution
title: Une fonction peut admettre des dérivées partielles (dans toutes les directions) en un point sans y être continue.
- Exemple : $f(x,y)=\begin{cases}1 &\text{ si } 0 <y<x^2 \\0 &\text{ sinon }\end{cases}$
```


```ad-hint
title: Exploitation des symétries
$$\forall (x,y),\;f(x,y) = \alpha f(y,x) \implies \frac{\partial f}{\partial y}(x, y) = \alpha \frac{\partial f}{\partial x}(y,x)$$
![[截屏2023-03-11 10.10.44.png]]
```

- Calculation par Python :
```python
import sympy as sp
x, y = sp.symbols("x y")
f = lambda x, y: x * y + x
sp.diff(f(x, y), x)
```

```ad-question
- Calculer les dérivées partielles : TD2-1-1, TD2-5-1
- Montrer qu'une fonction admet des partielles en un point (spécial) : TD2-5-3
```

## Point Extremum
```ad-note
title: Possibilité d'un point extremum
Soit $f:\mathbb{R}^n\to \mathbb{R}$, si $f$ différentiable, et admet un **extremum local** en $a$, c'est nécessaire : $$\forall i\in [\![1,n]\!],\; \partial_{i}f(a) = 0$$
```
```ad-question
- Étudier les extremums locaux : TD2-4-2, TD2-5-5
```
## Matrice Jacobienne
```ad-note
title: ==Matrice Jacobienne==
- Soit $f:O\to \mathbb{R}^p$, La matrice de la différentielle $\mathrm{d}f_{{x_{0}}}$ de $f$ en $x_0$ dans les bases canoniques de $\mathbb{R}^n$ et de $\mathbb{R}^p$ est appelée le **matrice de jacobienne de $f$ en $x_{0}$** notée $\mathrm{J}f_{x_{0}}$ : $$\mathrm{J}f_{x_{0}}=[\partial_{j}f_{i}(x_{0})]=\begin{bmatrix}
\partial_{1}f_{1}(x_{0})& \dots &\partial_{n}f_{1}(x_{0} )\\ 
\vdots & \ddots & \vdots \\
\partial_{1}f_{p}(x_{0})& \dots& \partial_{n}f_{p}(x_{0})
\end{bmatrix}$$
```
## Dérivée suivant un vecteur

```ad-note
title: Dérivée Directionnelle d'une application dans certaine direction
- Pour un vecteur $v ∈ \mathbb{R}^ n$ non nul, on peut définir plus généralement (sous réserve d’existence) la **dérivée directionnelle de** $f$ **dans la direction** $v$ **en** $x$, la dérivée de la fonction $t \longmapsto f(x+tv)$ en $0$, notée $∂_v f (x)$, par $$\partial_{v}f(x) = \lim_{ t \to 0 } \frac{f(x+tv)-f(x)}{t}$$
- La **dérivée directionnelle de** $f$ **dans la direction** $v$ est alors définie par : $$\partial_{v}f:\begin{cases}
O \to \mathbb{R}^p \\
x \mapsto \partial_{v}f(x)
\end{cases}$$
> Exemple : **Dérivée directionnelle** de $f:(x,y) \mapsto x^3+5y$ selon $v=(2, 3)$ en $(0,0)$ : $$\partial_{v=(2,3)}f(x=(0,0))= \lim_{ t \to 0 } \frac{f(x+2t,x+3t)-f(x)}{t}=\lim_{ t \to 0 } (8t^2+15) = 15$$Mais, selon $2v=(4, 6)$ : $$\partial_{(4,6)}f(0,0) = \lim_{ t \to 0 }( 4^3t^2 + 30 )= 30$$
> Exemple : ![[截屏2023-03-11 09.47.35.png]]

- En particulier, $\partial_{j}f(x)$ est la **dérivée directionnelle de $f$ dans la direction $e_{j}$ en $x$** : $$\partial_{j}f(x) = \lim_{ t \to 0 } \frac{f(x+te_{j})-f(x)}{t}$$
```

```ad-hint
title: Pour calculer la **dérivée directionnelle d'une application**
On peut directement calculer la dérivée de $t \mapsto f(x+tv)$ en $0$.
Exemple : ![[截屏2023-03-11 10.01.11.png]]![[截屏2023-03-11 10.01.21.png]]
```

