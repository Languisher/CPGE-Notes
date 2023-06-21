- Au-dessous, $E$ est un *espace euclidien*, c'est-à-dire, de dimension finie. [[Algèbre Linéaire#Espace Euclidien]]
## Endomorphismes Auto-Adjoints
En connaisant [[7A Endormorphisme Adjointe#L'adjoint d'un endomorphisme]], on définit : 
```ad-note
title: Endomorphismes auto-adjoints $\mathscr{S}(E)$
On dit que $f$ est **auto-adjoint** ou **symétrique** si $f^\star = f$, qui est appartient à : 
$$\mathscr S(E) = \{f\in \mathscr{L}(E),\; f^\star = f\}$$

On a donc : $$\forall(x,y) \in E^2,\; <u(x),y> = <x, u(y)>$$

- Remarque : Dans [[7A Endormorphisme Adjointe]], on a déjà en déduit que : $$\text{Im } (u) = (\text{Ker } u^\star)^\perp=(\text{Ker }  u)^\perp$$
- **Propriété** : $\mathscr{S}(E)$ est un *sous-espace vectoriel* de $\mathscr{L}(E)$ de dimension $$\frac{n(n+1)}{2} \text{ where } n= \text{dim }E$$C'est-à-dire, un demi, et les éléments sur la diagonal.
```


## Vecteur Propre, Valeur Propre
```ad-note
title: Définition-Vecteur Propre
-  On dit que $x\in E$ est un **vecteur propre** de $f$ ssi $$x \ne 0_{E} \text{ et } \exists \lambda \in \mathbb{K}, f(x) = \lambda x$$.
- $f(x)$ doit être *colinéaire* avec $x$ : ![[Appendix 2023-03-18 18.09.02.excalidraw]]
```


```ad-note
title: Définition-Valeur Propre
- On dit que $\lambda\in \mathbb{K}$ est une **valeur propre** de $f$ ssi $$\exists x \in E,\; x\ne 0_{E} \text{ et } f(x) = \lambda x$$
- En ce cas, on dit que $x$ est un **vecteur propre** associé à la **valeur propre** $\lambda$
- Exemple : Si $f$ est une *symétrie* alors ses valeurs propres sont $1$ et $-1$
- Exemple : Si $f$ est une *projection* alors ses valeurs propres sont $1$ et $0$
- **Proposition** : $0$ est une valeur propre de $f$ $\iff$ $\text{Ker }f \ne 0_{E}$, $f$ n'est pas injective.
```

```ad-note
title: Définition-Espace Propre
- Soit $\lambda \in \mathbb{K}$ une **valeur propre** de $f$, on appelle **espace propre de $f$ assoicé à $\lambda$** et on note $E_{\lambda}(f)$ l'espace $\text{Ker }(f - \lambda.\mathrm{id}_{E})$ car $$f(x) = \lambda x \iff(f-\lambda. \mathrm{id}_{E})(x) = 0_{E}$$
- Rappel que le vecteur propre ne peut pas un vecteur nul : $$E_{\lambda}(f) = \{0_{E}\} \cup \{\text{vecteurs propres associe a } \lambda\}$$
```

```ad-note
title: Définition-Spectre
On appelle **spectre** de $f$ et on note $\mathrm{sp}(f)$ l'ensemble des valeurs spectrales de $f$, cad les $\lambda\in \mathbb{K}$ pour que $f-\lambda.\mathrm{id}_{E}$ ne soit pas bijective, car : $$\lambda \text{ un valeur propre} \iff \text{Ker } (f-\lambda.\mathrm{id}_{E}) \ne \{0_{E}\}$$
Lorsque $\text{dim }E < + \infty$, $$\mathrm{sp}(f) = \{\text{valeurs propres de }f\}$$
```

```ad-hint
title: Comment déterminer si $\lambda \in \mathrm{sp}(f)$ ?
-  Soit $A \in \mathrm{M}_{n}(\mathbb{K})$, $\lambda \in \mathbb{K}$ est une **valeur propre** de $A$, cad $$\lambda\in \mathrm{sp}(f) \iff A-\lambda.I_{n} \text{ n'est pas inversible}$$Donc,
	- $\mathrm{rg}(A- \lambda.I_{n})< n$
	- $\mathrm{\det}(A-\lambda I_{n})=0_{\mathbb{K}}$
	- $\exists X\ne \{0_{E}\},\; AX=\lambda X$
	- $\chi_{A}(\lambda) =0$, ici $\chi_{A}(X) =\mathrm{\det}(XI_{n}-A)$
```

```ad-note
title: Polynôme caractéristique
- On note $\chi_{A}(X)$ le **polynôme caractéristique** d'une matrice $A$ :$$\chi_{A}(X) = \mathrm{\det}(XI_{n}-A)\in \mathbb{K}[X]$$
	- Donc $\lambda\in \mathrm{sp}(f) \implies \mathrm{\chi}_{A}(\lambda)=0$
- Si $A$ et $B$  sont *semblables* alors $\chi_{A}$ et $\chi_{B}$ sont égaux
- On note $\chi_{f}(X)$ le **polynôme caractéristique** d'une application associé à une base de $E$. $$\mathrm{M}_{\mathscr B}(f) = \begin{bmatrix}
\lambda_{1}&&0 \\
&\ddots& \\
0&&\lambda_{n}
\end{bmatrix} \iff \mathrm{sp}(f) = \{\lambda_{1},\dots,\lambda_{n}\}$$
```

## Théorème de Spectral

```ad-note
title: Transmission du stabilité entre $u$ et $u^\star$
- **Proposition** Technique : Si $u \in \mathscr{L}(E)$, $E_{1}$ un sous-espace de $E$, alors : $$u(E_{1}) \subset E_{1} \implies u^\star(E_{1}^\perp) \subset E_{1}^\perp$$
```

```ad-note
title: Théorème de Spectral ou Théorème de réduction des endomorphismes auto-adjoints
- ==Version vectorielle== : Soit $E$ un espace euclidien. Alors, il existe une base *orthonormée* $(e_{1},\dots,e_{n})$ de $E$ et il existe des scalaires $(\lambda_{1},\dots,\lambda_{n})\in \mathbb{R}^n$, tels que : $$f \in \mathscr{S}(E) \iff \forall k\in [\![1,n]\!],\;\underbrace{f(e_{k})}_{\mathrm{Mat}(f, (e_{1},\dots,e_{n}))} = \underbrace{\lambda_{k}.e_{k}}_{\mathrm{diag}(\lambda_{1},\dots,\lambda_{n})}$$On dit que $f$ **se diagonalise en base orthonormée**. 
	- Les vecteurs $e_{k}$ s'appellent **vecteurs propres** de $f$
	- Les réels $\lambda_{k}$ s'appellent des **valeurs propres** de $f$
- **Remarque** : En ce cas, soit $\mathscr{E}=(e_{1},\dots,e_{n})$ une base orthonormée, $$<f(x),x> = \sum_{k=1}^n\lambda_{k}<e_{k},x>^2$$
- Démonstration : ![[Pasted image 20230318200648.png]]
```

```ad-hint
title: Matrice Symétrique
On note les **matrice symétrique** $$M\in\mathrm{S}_{n}(\mathbb{R}) \iff ^tM=M$$
```

```ad-note
title: Relation entre endomorphisme auto-adjointe et matrice symétrique

Soit $A \in \mathrm{M}_{n}(\mathbb{R})$, $u \in \mathscr{L}(\mathbb{R}^n)$, $\mathrm{Mat}(u, \mathscr{C}^n)=A$,
1. Si $A \in \mathrm{S}_{n}(\mathbb{R})$, alors $u \in \mathscr{S}(\mathbb{R}^n)$, et $$\exists \;\underbrace{\mathscr{E}=(e_{1},\dots,e_{n})}_{\text{une base orthonormee}},\; \mathrm{Mat}(u, \mathscr{E}) = \begin{bmatrix}
\lambda_{1}&&0 \\
&\ddots& \\
0&&\lambda_{n}
\end{bmatrix}$$Cela implique $$\text{Si }\underbrace{P =P_{\mathscr{C}^n}^{\mathscr E}\in \mathscr{GL}_{n}(\mathbb{R})}_{^tP=P^{-1}},\;P^{-1}.A.P = \begin{bmatrix}
\lambda_{1}&&0 \\
&\ddots& \\
0&&\lambda_{n}
\end{bmatrix}$$
2. Si $A \in \mathrm{M}_{n}(\mathbb{R})$ et $^tA.A\in \mathrm{S}_{n}(\mathbb{R})$, $$\exists\;\underbrace{P \in \mathscr{GL}_{n}(\mathbb{R})}_{^tP=P^{-1}},\;P^{-1}.\;^tA.A.P = \begin{bmatrix}
\lambda_{1}&&0 \\
&\ddots& \\
0&&\lambda_{n}
\end{bmatrix}$$
```
> 
> Exemple : Soit $\mathscr{E} = (e_{1},e_{2},e_{3})$ une base de $E$, soit $$\begin{cases}
f(e_{1})&=e_{1}-e_{2}-e_{3} \\
f(e_{2})&=-e_{1}+e_{2}-e_{3} \\
f(e_{3})&=-e_{1}-e_{2}+e_{3}
\end{cases}$$Donc, $u_{1} = e_{1}+e_{2}+e_{3}$ et tout vecteur non nul et colinéaire à $u_1$ a une **valeur propre** $\lambda_{1}=-1$, car $f(u_{1}) =-u_{1}$. De même, $u_2=e_1-e_3$ et $u_{3}=e_{2}-e_{3}$ sont deux **vecteurs propres** associés à une **valeur propre** $\lambda_{2}=2$.

> Exemple : Pour une fonction $f:\phi \mapsto \phi'$, il a une **vecteur propre** $g: x \mapsto \exp(\lambda x)$ associé à une **valeur propre** $\lambda$.

## Endomorphisme Auto-adjoint Positif et Endomorphisme Auto-adjoint Définis Positif
```ad-note
title: Endomorphisme Auto-adjoint Positif
- **Définition** : Soit $f \in \mathscr{S}(E)$, on dit que $f$ est un **endomorphisme auto-adjoint positif** s'il vérifie : $$\forall x\in E,\;< x,f(x)> \geq 0 \text{ ou } \forall k\in [\![1,n]\!],\; \lambda_{k}\in \mathbb{R}_{+}$$On note $$f \in \mathscr{S}^+(E)$$Il *n'est pas un sous-espace vectoriel*. Contrairement, c'est un **cône positif** de $\mathscr{S}(E)$
- ==Version matricielle== Soit $u \in \mathscr{L}(E)$, $A=\mathrm{Mat}(u,(e_{1},\dots,e_{n}))$ sous une base orthonormée : $$u \in \mathscr{S}^ +(E) \iff ^tX.A.X \geq 0$$
```

```ad-note
title: Endomorphisme Auto-adjoint Définis Positif
- **Définition** : Soit $f \in \mathscr{S}(E)$, on dit que $f$ est un **endomorphisme auto-adjoint définis positif** s'il vérifie : $$\forall x\in E\backslash\{0_{E}\},\;< x,f(x)> > 0 \text{ ou } \forall k\in [\![1,n]\!],\; \lambda_{k}\in \mathbb{R}_{+}^*$$On note $$f \in \mathscr{S}^{++}(E)$$Il *n'est pas un sous-espace vectoriel*. Contrairement, c'est un **cône positif** de $\mathscr{S}(E)$
- ==Version matricielle== Soit $u \in \mathscr{L}(E)$, $A=\mathrm{Mat}(u,(e_{1},\dots,e_{n}))$ sous une base orthonormée : $$u \in \mathscr{S}^ {++}(E) \iff ^tX.A.X > 0$$
```

```ad-note
title: Version Matricielle
Soit $u \in \mathscr{L}(E)$, $A=\mathrm{Mat}(u,(e_{1},\dots,e_{n}))$ sous une base orthonormée : 
$$\begin{align}
u\in \mathscr{S}(E) &\iff A \in \mathrm{S}_{n}(E) \\
u\in \mathscr{S}^+(E) &\iff A \in \mathrm{S}_{n}^+(E)=\{A \in \mathrm{S}_{n}(E),\; \forall X\in \mathrm{M}_{n,1}(\mathbb{R}),\; ^tX.A.X \geq 0\} \\
u\in \mathscr{S}^{++}(E) &\iff A \in \mathrm{S}_{n}^{++}(E)=\{A \in \mathrm{S}_{n}(E),\; \forall X\in \mathrm{M}_{n,1}(\mathbb{R}),\; ^tX.A.X > 0\}
\end{align}$$
```

- **Proposition** : $$\begin{align}
u\in \mathscr{L}(E) &\implies u^\star \circ u \in \mathscr{S}^+(E) \\
u\in \mathscr{L}(E),\;u\in \mathscr{GL}(E) &\iff u^\star \circ u \in \mathscr{S}^{++}(E)
\end{align}$$


```ad-note
title: Transformation de $\mathscr{S}^+$ à $\mathscr{S}^{++}$
Si $f \in \mathscr{S^+}(E), \; \varepsilon>0$, alors : $$f + \varepsilon.\mathrm{id}_{E}\in \mathscr{S}^{++}$$
```



- **Proposition** : Soit $f\in \mathscr{S}^+(E)$, alors il existe un *unique* endomorphisme $g\in \mathscr{S}^+(E)$ tel que $$f = g \circ g=g^2$$