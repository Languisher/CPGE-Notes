## Orthogonalité, Orthonomalité
```ad-note
title: Orthogonal, Orthonormal
Soit $E$ un **espace préhilbertien réel**, $\varphi$ un **produit scalaire** de $E$.
- $x\in E$ est **unitaire** si $\Vert x\Vert=1$
- $(x,y)\in E^ 2$ sont **orthogonaux** si $$\varphi(x,y)=0$$
- Une famille de vecteurs est **orthogonale** (resp. **orthonormale**) si les vecteurs sont 2 à 2 **orthogonaux** (resp. et aussi **unitaire**)

**Orthogonal** d'une sous espace $A \subset E$ : On note $$A^\perp=\{x\in E,\; \forall a\in A,\; <a,x> =0\} $$
```

- Propriété : $$A^\perp = (\text{Vect}(A))^\perp$$
- Propriété : $$E_{1}\subset((E_{1})^\perp)^\perp$$avec égalité en dimension finie.
- Propriété : $$(E_{1}+E_{2})^\perp = E_{1}^\perp \cap E_{2}^\perp$$
- Propriété : Somme directe orthogonale
- Proposition : Soit $E$ un **espace euclidien** de dimension $n$, muni d'une base **orthonormale** $(e_{1},\dots,e_{n})$. Alors, on a $$\forall x\in E,\; x=\sum_{i=1}^n<x,e_{i}>e_{i}$$et $$\forall (x,y)\in E^2,\; <x,y> = \sum_{i=1}^n<x,e_{i}><y,e_{i}>$$
## Orthonormalisation de Gram-Schmidt
Soit $E$ un **espace euclidien** de dimension $n$, et $(v_{1},\dots,v_{n})$ une base quelconque de $E$. Alors, il existe une base **orthonormale** unique $(e_{1},\dots,e_{n})$ de $E$, tel que $$\text{Vect}(e_{1},\dots,e_{n})=\text{Vect}(v_{1},\dots,v_{n})$$
On construit les vecteurs par récurrence de la manière : $$\begin{align}
e_{1}&=\frac{v_{1}}{\Vert v_{1}\Vert   } \\
e_{2}'&=v_{2}-<v_{2},e_{1}>.e_{1},\quad e_{2}=\frac{e_{2}'}{\Vert e_{2}'\Vert } \\
&\vdots \\
e_{n}' &=v_{n}-\sum_{k=1}^n<v_{n},e_{k}> .e_{k},\quad e_{n}=\frac{e_{n} '}{\Vert e_{n}'\Vert }
\end{align}$$Preuve : ![[Pasted image 20230228003455.png]]Orthogon