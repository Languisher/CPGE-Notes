> Date : 2023-02-13 Matériaux : [[Lundi13fevrier.pdf]]
> Date : 2023-02-15 Matéiraux : [[Mercredi15fÃ©vrier.pdf]], QCM : [[15fÃ©vrier2023.pdf]]

## Dualité, Formes Linéaires

- L'idée : Pour étudier un $\mathbb{K}$-espace vectoriel $E$, on va étudier $\mathscr L(E, \mathbb K)$.

- Qu'apporte la **dualité** ? <u>Mise en équation</u> de sous-espace vectoriels (particuliers)

> [!note] Dual d'un espace vectoriel, Formes Linéaires 对偶空间，线性泛函
> L'application linéaire de $E$ dans $\mathbb{K}$ ==$\mathscr{L}(E,\mathbb{K})$== où ==$E$ est un $\mathbb{K}$-espace vectoriel== s'appelle **dual de $E$**, et se note $$E ^\star$$(*Attention: star, pas étoile*)
> Les éléments de $E ^\star$ s'appellent des **formes linéaires**.


- Exemples : Les **formes linéaires** de $\mathbb K_{n}$ sont les applications de $\mathbb{K}_{n}$ dans $\mathbb{K}$ : $$l:(x_{1},x_{2},\dots,x_{n})\longmapsto\; <a,x> =a_{1}x_{1}+a_{2}x_{2}+\dots +a_{n}x_{n}$$
- Exemples : Les **formes linéares** de $\mathrm{M}_{n}(\mathbb{R})$ est : $$\varphi : M \longmapsto \mathrm{tr}(AM) \text{ tq } A \in \mathrm{M}_{n}(\mathbb{R})$$
- Propriété : $E^\star$ est un $\mathbb{K}$-espace vectoriel.
- Propriété : Si $E$ est de *dimension finie*, alors $E^\star$ est de dimension finie, et $$\text{dim }E = \text{dim } E^\star$$Ils sont donc *isomorphes*. Mais c'est FAUX en dimension *infinie*.

- En général $\mathscr{L}(E,F)$ n'est pas isomorphe à $\mathscr{L}(E,F)$. Mais, si $E,F$ respectivement de dimension $p,q \in \mathbb{N}$, $\mathrm{Mat}_{p,q}(\mathbb{K})$ est isomorphe à $\text{Mat}_{q,p}(\mathbb{K})$.

## Famille Duale, Base Duale, Base Ante-duale
Cette chapitre, on va trouver les expressions d'une forme linéaire dans une base
```ad-note
title: Famille Duale
- Si $(e_{i})_{i\in I}$ est une *base* de $E$, on peut définir la **famille duale** associée $(e_{i}^\star) \in (E^\star)^I$ (en connaisant $(e_{i})$) par $$\forall j\in I,\; e_{i}^\star(e_{j}) = \delta_{i,j}$$$\delta_{i,j} = 1$ si $i=j$, sinon $0$.
- Si on change $(e_{i})$ en $(e_{i}')$, en général $e_{i}^\star \ne e_{i}^{'\star}$
```

- $(e_{i}^\star)_{i\in I}$ est une *famille libre* de $E^\star$ : ![[Pasted image 20230226202424.png]]
C'est beaucoup plus facile de montrer l'indépendance de formes linéaires, que l'indépendance de formes linéaires, que l'indépendance de vecteurs.

```ad-note
title: Base Duale
- Plus spécifiquement, pour une famille duale, si $E$ est de *dimension finie*, la **famille duale** associée est une **base** de $E^\star$
- En ce cas, soit $f\in E^\star$ on a : $$\varphi = \sum_{i=1}^n\varphi(e_{i}).e_{i}^\star$$
```

- *Utilité* : **Polynômes d'interpolation de Lagrange**, Soit $(a_{1},\dots,a_{n})\in I^n,\;(y_{1},\dots,y_{n})\in \mathbb{R}^n$, La fonction $$\varphi_k : x \mapsto \frac{\prod_{j \ne k}(x-a_{j})}{\prod_{j\ne k}(a_{k}-a_{j})}$$est : (1) bien une **forme linéaire**, (2) $\varphi_{k}= \text{Vect}(\{x \to x^j\})^\star$ (3) vérifie $\varphi_{k}(a_{j}) = \delta_{k,j}$. En ce cas $P = \sum_{k=1}^n y_{k}.\varphi_{k}$ convient. （补充）

```ad-attention
title: Rappelle encore une fois : en *dimension infinie*, $(e_{i}^ \star)$ n'est jamais génératrice.
```
```ad-note
title: Base Ante-duale
- Soit $(\varphi_{1},\dots,\varphi_{n})$ une base de $E^\star$, alors il existe une unique base $(e_{1},\dots,e_{n})$ de $E$, telle que : $$\forall i\in [\![1,n]\!],\; e_{i}^\star=\varphi_{i}$$Cette base est appelée **base ante-duale** de la base $(\varphi_{1},\dots,\varphi_{n})$
- C'est-à-dire, $E$ est identique avec $(E^{\star})^\star$
```
- Résumé : ![[截屏2023-03-04 22.01.48.png]]
