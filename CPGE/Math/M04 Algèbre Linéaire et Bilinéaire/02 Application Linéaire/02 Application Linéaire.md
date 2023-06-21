## Application Linéaire
- Soit $E$ et $E'$ deux $\mathbb{K}$-espace vectoriels, une application $f: E\to E'$ est dite **application linéaire** si : en notant $\mathscr{L}(E,E')$ l'ensemble de l'applications.
$$
\forall(x,y)\in E^2,\; \forall(\lambda,\mu) \in \mathbb{K}^2,\; f(\lambda.x+\mu.y)= \lambda.f(x) +\mu.f(y)
$$
- Exemple : $\text{id}$ et dérivation des fonctions de classe $\mathscr C^1$
- Cas particulier :
	- **Endomorphisme** si $E = E'$, notant $\mathscr{L}(E)$
	- **Isomorphisme** si $f$ est bijective
	- **Automorphisme** si à la fois endomorphisme et isomorphisme
	- **Forme Linéaire**, si $E'= \mathbb{K}$

- $\mathscr{L}(E, E')$ est un $\mathbb{K}$-espace vectoriel.
	- ![[截屏2023-02-13 19.16.42.png]]
- Soit $E$ et $E'$ deux $\mathbb{K}$-espaces vectoriels et soit $f \in \mathscr{L}(E, E')$. Si $F$ est un sous-espace vectoriel de $E$, alors : $f(F)$ est un sous-espace vectoriel de $E'$, et $f^{-1}(F') = \{x\in E,\;f(x)\in F' \}$ est un sous-espace vectoriel de $E$.

## Images et Noyaux
```ad-note
title: Noyau et Image d'une application linéare
Soit $u \in \mathscr{L}(E,F)$, On appelle :
- **noyau** de $u$, notant $\text{Ker }u$, le sous-espace vectoriel de $E$ : $$\text{Ker } u=u^{-1}(\{0\})=\{x\in E, \; u(x)=0\}$$
- **image** de $u$, notant $\text{Im }u$, le sous-espace vectoriel de $F$ : $$\text{Im } u=u(E) = \{u(x),\; x \in E\}$$
- Exemple : ![[截屏2023-03-11 14.44.54.png]]
```

- Soit $E$ et $E'$ deux $\mathbb{K}$-espaces vectoriels et soit $f \in \mathscr{L}(E, E')$.
	- $f$ est **injective** ssi $\text{Ker } f=\{ 0_{E }\}$ (car $f$ est linéaire)
	- $f$ est **surjective** ssi $\text{Im }f=E'$.

```ad-note
title: Injectivité et Noyau
- **Théorème** : Une application est **injective** ssi $\text{Ker }u=\{0\}$
- Exemple : ![[截屏2023-03-11 14.47.02.png]]
```

```ad-hint
title: Pour montrer qu'une application est **injective**
Pour démontrer qu’une application linéaire est injective, systématiquement prouver $\text{Ker }u = \{0\}$ ou plus simplement (puisque $\{0\} ⊂ \text{Ker }u$) : $$∀x ∈ E,\; u(x) = 0 ⇒ x = 0$$Évidemment, il faut savoir que $u$ est une application linéaire
```



- Propriétés : ![[截屏2023-02-13 19.59.37.png]]
- Propriétés : ![[截屏2023-02-13 20.00.28.png]]
## Projecteurs et Symétries
- Soit $E$ un $\mathbb{K}$-espace vectoriel, $F$ et $G$ deux sous-espaces vectoriels de $E$ tel que $E = F \oplus G$. On appelle **projection de** $E$ sur $F$ parallèlement à $G$ l'*endomorphisme* de $E$ défini par :
$$
p_{F \parallel G} : \begin{cases}
E \to E  \\
x \mapsto x_{F} \text{ où } x = x_{F}+x_{G}
\end{cases}
$$
- Soit $E$ un $\mathbb{K}$-espace vectoriel, $F$ et $G$ deux sous-espaces vectoriels de $E$ tel que $E = F \oplus G$. Alors : $p_{F \parallel G} + p_{G \parallel F} = \text{id}_{E}$
- $G = \text{Ker }(p_{F \parallel G})$ et $F = \text{Im}(p_{F \parallel G})=\text{Ker}(p_{F \parallel G}-id_{E})$
- Soit $E$ un $\mathbb{K}$-espace vectoriel. On appelle **projecteur de** $E$ tout *endomorphisme* $p$ de $E$ tel que $p\circ p=p$.
- **projection** $=$ **projecteur**
- Soit $E$ un $\mathbb{K}$-espace vectoriel, $F$ et $G$ deux sous-espaces vectoriels de $E$ tel que $E = F \oplus G$. On appelle **symétrie de** $E$ par rapport à $F$ parallèlement à $G$ l'*automorphisme* de $E$ défini par :
$$
s_{F \parallel G} : \begin{cases}
E \to E \\
x \mapsto x_{F}-x_{G} \text{ où } x=x_{F}+x_{G}
\end{cases}
$$
- $s_{F \parallel G}\circ s_{F \parallel G} = \text{id}_{E}$
- $F= \text{Ker }(s_{F \parallel G}-\text{id}_{E})$, $G = \text{Ker }(s_{F \parallel G}+\text{id}_{E})$ (考虑什么时候 $x\in F,\;f(x)=0$)

## Cas Particulier de la Dimension Finie
- Soit $E$ et $E'$ deux $\mathbb{K}$-espaces vectoriels et soit $f \in \mathscr{L}(E, E')$. Alors, $\text{Im}(f)$ est de dimension finie et $\text{dim } \text{Im}f \leq \text{dim }E$.
- $\text{dim } \text{Im}f=\text{dim } E \iff f$ injective
- On appelle **rang de** $f$ et on note $\text{rang}(f) = \text{dim}(\text{Im}(f))$
- ![[截屏2023-02-13 20.20.31.png]]
- ![[截屏2023-02-13 20.20.45.png]]
- **Théorème du rang :**
$$
\text{rang}(f)= \text{dim } E -\text{dim } \text{Ker}(f)
$$
- $E$ de dimension finie et $f \in \mathscr{L}(E)$, donc $f$ injective $\iff$ $f$ surjective $\iff$ $f$ bijective.
- $\mathscr{L}(E,  E')$ est de *dimension finie*, égale à $\text{dim }E \times \text{ dim }E'$.（可以用矩阵的思路去考虑这个问题，每个位置都是一个基底）
	- Démonstration : Soit $u \in \mathscr{L}(E, E')$, soit $\text{dim }E =n$, on construit $\phi$ qui suffit : $\phi:\begin{cases}\mathscr{L}(E,E') \to (E')^n\\u \mapsto (u(e_{1}),\dots,u(e_{n}))\end{cases}$, $\phi$ est isomorphisme de $\mathscr{L}(E,E')$ sur $(E')^n$.

