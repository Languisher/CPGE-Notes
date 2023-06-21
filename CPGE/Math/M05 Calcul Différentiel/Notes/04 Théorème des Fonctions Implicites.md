> Date : 2023-03-01 Cours : [[Slides Semaine 3 thÃ©orÃ¨me des fonctions implicites (remplis).pdf]]
> Date : 2023-03-08 Cours : [[Slides semaine 4 remplis.pdf]]

## Énoncé
```ad-hint
title: Pour une fonction implicite, est-ce que l'on peut exprimer une variable par autres variables ?
**But** : On s'intéresse à l'ensemble $$\Gamma _{f} : \{(x, y), \; f(x,y)=0\}$$Savoir si : ==on peut écrire $y$ en fonction de $x$ ou inversement==.

> Exemple (*Linéaire*) : Soit $f\in \mathscr{L}(\mathbb{R}^n,\mathbb{R}^p)$, $A = \mathrm{Mat}_{p,n}(f)$ dans les bases canoniques de $\mathbb{R}^n$ et $\mathbb{R}^p$, alors $$f(x_{1},\dots,x_{n})=0_{\mathbb{R}^p} \iff AX = 0$$Cette équation admet une infinité de solutions si $n>p$.
> La dimension de $\Gamma_{f}$ dépend du *rang de $A$ ou $f$*.
> Soit $X_{1}\in \mathbb{R}^j\;(j<n)$, $$\begin{bmatrix}
\underbrace{B}_{\in \mathrm{M}_{p,j}}&\underbrace{C}_{\in\mathrm{M}_{p,n-j}}
\end{bmatrix} \begin{bmatrix}
X_{1} \\
X_{2}
\end{bmatrix}= 0_{p,1} \iff CX_{2}=-BX_{1}$$en déduit que $X_{2}=-C^{-1}BX_{1}$ si $C$ est inversible, en ce cas $p=n-j$ car c'est une matrice carrée.

```


```ad-hint
title: Idée
L'idée centrale du calcul différentiel : Linéariser. La géométrie de $\Gamma_{f}$ de'pendre de la *différentielle de* $f$. (**Différentielle** : [[03 Différentielle]])
```

```ad-note
title: Notations de la différenetielle de la fonction
La **différentielle** de la fonction $f(x, y)\in \mathbb{R}^{n_{1}\times n_{2}} \to \mathbb{R}^p$ des variables en certain valeurs : $$\begin{align}
\mathrm{d}[f(a,\cdot)]_{b} &: \text{ differentielle de } y \mapsto f(a,y) \text{ en }b \\
\mathrm{d}[f(\cdot,b)]_{a} &: \text{ differentielle de } x \mapsto f(x,b) \text{ en }a
\end{align}$$
Les matrice jacobienne des dérivées partielle : ![[截屏2023-03-09 09.07.04.png]]
```

```ad-warning
title: La matrice de $\mathrm{d}[f(a,\cdot)]_{b}$ doit être *inversible*. En ce cas, nécessairement $p=n_{2}$.
```

```ad-note
title: Théroème des fonctions implicites
Soit $f: O \to \mathbb{R}^p$ de classe $\mathcal{C}^k$, $O=(\mathbb{R}^{n_{1}}\times \mathbb{R}^{n_{2}}) =( \mathbb{R}^{n} \times \mathbb{R}^p)$, On suppose que $$f(a,b) = 0_{\mathbb{R}^p}, \quad \mathrm{d}[f(a,\cdot)]_{b} \text{ inversible}$$Alors : ($\phi$ est de classe $\mathcal{C}^k$) $$f(x,y) = 0_{\mathbb{R}^p} \iff\exists\; \phi: \begin{cases} 
U &\to V \quad (U \times V \subset O) \\
x &\mapsto y = \phi(x)
\end{cases}$$
- On a $\phi(a)=b$
- L'*inversibilité* de $\mathrm{d}[f(a,\cdot)]_{b}$ se traduit matriciellement par le fait que la matrice ![[截屏2023-03-10 14.09.07.png]]est *inversible* ssi son déterminant est $\ne 0$
- Puisque $\mathrm{d}[f(a, \cdot)]_{b}$ est inversible et $\mathrm{d}f$ est continue, on en déduit que $$\mathrm{d}[f(x,\cdot)]_{y} \text{ est inversible}$$
- Différentielle la relation donne la *différentielle de la fonction* d'aprèes [[1A Dérivée Partielle et Différentielle#Cas des fonctions bilinéaire]]: $$\begin{align}
f(x, \phi(x)) =0 &\iff \mathrm{d}[f(\cdot, \phi(x))] _{x} + \mathrm{d}[f(x,\cdot)]_{\phi(x)} \circ \mathrm{d}\phi_{x}= 0_{\mathbb{R}^p} \\
&\iff \mathrm{d}[f(x,\cdot)]_{\phi(x)} \circ \mathrm{d}\phi_{x}= -\mathrm{d}[f(\cdot, \phi(x))] _{x}  \\
&\iff \mathrm{d}\phi_{x} = -(\mathrm{d}[f(x, \cdot)]_{\phi(x)})^{-1} \circ \mathrm{d}[f(\cdot, \phi(x))]_{x}
\end{align}$$


- Exemple : Les courbes du plan (dans $\mathbb{R}^2$) 
	- Rappel que $(x, y) \in \mathbb{R}^n \times \mathbb{R}^p$, ici c'est $$n =p =1$$.
	- La condition d'inversibilité $$\mathrm{d}[f(x, \cdot)]_{y} = \partial_{2}f(x,y) \neq 0$$par exemple : la fonction donné : $f(x,y) =x^2+y^2 - 1 =0$, donc $\partial_{2}f(a,b) =2b \ne 0$
	- Si c'est le cas, au voisinage de $(a, b)$, si $f(x,y)=0$ alors $y=y(x)$
	- ![[截屏2023-03-10 14.44.30.png]]
- Exemple : Les surface de l'espace
	- Rappel que $((x,y),z) \in \mathbb{R}^n \times \mathbb{R}^p$ avec $n=2,p=1$
	- La condition d'inversibilité est $$\partial_{3}f(x,y,z) \ne 0$$
	- Si c'est le cas, au voisinage de $(a,b)$, si $f(x,y,z) = 0$, alors $z=z(x,y)$

- Exemple : Les courbes de l'espace 
	- Rappel que $(x, (y,z)) \in \mathbb{R}^n \times \mathbb{R}^p$ avec $n=1,p=2$
	- La condition d'inversibilité est $$\mathrm{\det}\begin{bmatrix}
\partial_{2}f_{1}(x,y,z)& \partial_{3}f_{1}(x,y,z) \\
\partial_{2}f_{2}(x,y,z)& \partial_{3}f_{2}(x, y,z)
\end{bmatrix} \ne 0$$Au voisinage de $(a,b)$, si $f(x,y,z) =0$ alors $y =y(x)$ et $z=z(x)$
```

```ad-question
- Démontrer qu’il existe un voisinage de 0 et une unique fonction telle que $\phi(x)=y$ et pour tout $x\in \mathcal{V}$, $\psi(x,\phi(x))=0$. (TD2-1-2, TD2-2, TD2-3-1, TD2-4-3, TD2-5-6, TD2-5-7, TD2-9-1)
```

## Application : Trouver une DL autour de ce point
```ad-question
- Calculer le développement limité à l’ordre $n$ de $\phi$ en $x_0$. (TD2-1-3, TD2-3-2, TD2-4-4, TD2-5-8, TD2-9-2)
```
## Application à la thermodynamique
On va appliquer le théorème des fonctions implicites sur l’équation $$PV = nRT$$Autrement dit, on souhaite *exprimer une (resp. deux) variable(s) en fonction des autres* (resp. de l’autre). Pour cela il faut :
- Une fonction : $$f: (P,V,T) \longmapsto PV-nRT$$
- Trouver un bon ouvert, en ce cas $$O = \{(P,V,T) \in \mathbb{R}^3,\; P>0, \; V>0,\; T>0\}$$
- Se placer en un point $(P_{0},V_{0},T_{0})$ tel que $$f(P_{0},V_{0},T_{0}) = 0 \text{ avec les restreints d'inversibilite}$$
Alors, $f$ est de classe $\mathcal C^\infty$ sur $O$. Le **théorème des fonctions implicites** assure que dans un voisinage de $(P_{0},V_{0},T_{0})$, $$f(P,V,T) = 0 \iff P = P(V,T),\; \text{ resp. autres choses}$$
On remplace $P$ par $P(V,T)$. En dérivant par rapport à $V$ l'équation $f(P(V,T),V,T)=0$, il vient : $$\partial_{1}f(P(V,T),V,T) \circ \partial_{1}P(V,T) + \partial_{2}f(P(V,T),V,T) = 0$$
Dans ce voisinage de $(P_{0},V_{0},T_{0})$ on a donc : $$\left( \frac{\partial P}{\partial V} \right)_{T} = \partial_{1}P(V,T) = - \frac{\partial_{2}f(P(V,T),V,T)}{\partial_{1}f(P(V,T), V, T)}$$
De même, $$\left( \frac{\partial V}{\partial P} \right)_{T}= \partial_{2}V(P,T) = - \frac{\partial_{3}f(P,V(P,T),T)}{\partial_{2}f(P,V(P,T),T)}$$
Finalement, on retrouve donc la formule $$\left( \frac{\partial P}{\partial V} \right)_{T}\left( \frac{\partial V}{\partial T} \right)_{P}\left( \frac{\partial T}{\partial P} \right)_{V} = -1$$

## Application : Les racines de polynômes
### Cas degré 2
On veut trouver les paramètres qui suffit l'équation du second degré : $$x^2 + px+ q=0$$
Considérons l'application : $$f(x_{0},p_{0},q_{0}) = x_{0}^2+p_{0}x_{0}+q_{0}=0$$
Évidement, le **théorème des fonctions implicites** ne s'applique pas si $$\partial_{1}f(x_{0},p_{0},q_{0})=2x_{0}+p_{0}=0 \implies x_{0}= - \frac{p_{0}}{2}$$
Dans l'équation, c'est la condtion : $p_{0}^2 - 4q_{0}=0$. Donc, il existe un voisinage $V$ de $(x_{0},p_{0},q_{0})$ tel que$$\text{Si }p_{0}^2-4q_{0}>0,\; \forall(x,p,q)\in V,\; f(x,p,q)=0\iff x=x(p, q)$$
### Cas degré supérieur à 2
Soit $n \in \mathbb{N}^*$, soit une fonction polynomiale de degré $n$ et soit $x_{0}\in \mathbb{R}$ $$P : x \longmapsto \sum_{k=0}^n a_{k}x^k$$
- Si $P(x_{0}) = 0$, on dit que $x_{0}$ est une **racine** de $P$
- L'**ordre de la racine** $x_{0}$ est le plus petit entier $l\geq 1$ tel que $P^{(l)} (x_{0}) \ne 0$ mais $P(x_{0}) = \dots = P^{(l-1)}(x_{0})=0$
- Si $l=1$, c'est une **racine simple**, sinon **racine multiple**
Considérones l'application : $$f(x,a_{0},\dots,a_{n}) = 0 \text{ en meme temps } \partial_{1}f(x,a_{0},\dots,a_{n}) \ne 0$$
On peut toujours trouver un ouvert $U$ de $\mathbb{R}^{n+1}$ et une fonction $\phi: U \to V$ tels que $$f(x_{0},a_{0},\dots,a_{n}) = 0 \iff x = \phi(b_{0}, \dots,b_{n})$$
