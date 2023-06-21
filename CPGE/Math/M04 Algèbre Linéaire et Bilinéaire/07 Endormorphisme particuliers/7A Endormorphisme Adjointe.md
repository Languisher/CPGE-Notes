> Date : 2023-03-01 Cours : [[Mercredi1erMars.pdf]]
> Date : 2023-03-06 Cours : [[Lundi6mars.pdf]]
> Date : 2023-03-08 Cours : [[Mercredi8mars.pdf]]

- On note $E$ un **espace euclidien** (donc de dimension finie)

```ad-note
title: 1-1 Relation entre une forme linéaire et un élément dans l'espace vectoriel
**Théorème :** Soit $E$ un **Espace Euclidien**,  $$\forall \varphi \in E^\star,\; \exists! a \in E,\; \forall x\in E,\; \varphi(x) =  \;<a,x>$$
- On dit que $a$, un élément de $E$ représent un forme linéaire de $E$ dans $\mathbb{R}$
- Demonstration : ![[201679120510_.pic.jpg]]
```
	
On va trouver les relations entre : ![[211679121338_.pic_hd.jpg]]

## L'adjoint d'un endomorphisme
```ad-note
title: L'adjoint d'un endomorphisme
**Définition** : Soit $E$ **espace euclidien**, soit $u \in \mathscr{L}(E)$, il exist un unique $u^\star \in \mathscr{L}(E)$, s'appelle appelle **l'adjoint de** $u$ : $$\forall(x,y) \in E^2,\;<u(x),y> = <x,u^\star(y)>$$

**Propriétés** : 
- Linéarité : $$(f+g)^\star = f^\star+g^ \star,\; (\lambda.f)^\star = \lambda.f^\star,\; (f^\star)^\star=f$$
- Relations : $$\begin{align}(0_{\mathscr{L}(E)})^\star&= 0_{\mathscr{L}(E)},\; (\mathrm{id}_{E})^\star = \mathrm{id}_{E} \\(f \circ g) ^\star &= g ^\star \circ f ^\star \\f \in \mathscr{GL} (E) &\implies f^\star\in \mathscr{GL}(E),\;(f^{-1})^\star = (f^\star)^{-1}\end{align}$$

**Propriétés** : Soit $u \in \mathscr{L}(E)$ $$\begin{align}
\text{Ker}(u^\star) &= \text{Im}(u)^\perp \\
\text{Im}(u^\star) &= \text{Ker}(u)^\perp
\end{align}$$
- Démonstration : ![[Pasted image 20230307213225.png]]
```

```ad-hint
title: L'adjoint d'un endomorphisme sous la forme matricielle
- Soit $\mathscr{E}$ est un base *orthonormée*, $$\boxed{\mathrm{Mat}(u, \mathscr{E}) = A \longmapsto \mathrm{Mat}(u^\star, \mathscr{E}) = \;^tA}$$Démonstration : ![[Pasted image 20230307211754.png]]
```


```ad-note
title: Cas particuliers : auto-adjoints, orthogonaux, projecteurs
- Cas particuliers :
	- $u^\star = u$ endomorphismes **auto-adjoints** ou symétriques
	- $u^{-1} = u^\star$ automorphismes *orthogonaux*
	- $u^\star = -u$ endomorphismes *anti-symétriques*, c'est-à-dire $<x,f(x)> =0$
	- Un projecteur $p$ qui suffit $p \circ p = p$ : ![[截屏2023-03-15 19.27.24.png]]
	- Un projecteur *orthogonal* $p$ suffit : $p^\star = p$, et en ce cas : $$\text{Im } p^\star=\text{Ker } p,\; \text{Ker } p^\star=\text{Im } p$$
```


