## Définition
- Pour une application linéaire $u \in\mathscr{L}(E,F)$, si $u$ est *bijective*, il s'appelle **isomorphisme entre $E$ et $F$**.
- $E$ et $F$ sont **isomorphismes** ss'il existe une fonction *bijective* entre les deux.
- Exemple : Toutes les *supplémentaires* dans $E$ d'un même sous-espace vectoriel de $E$ sont **isomorphes**.
```ad-important
title: Pour montrer que en dimension infinie, deux espace vectoriels sont isomorphismes, il faut trouver une application linéaire et montrer que c'est un isomorphisme.
```

- Exemple : Soit $u \in \mathscr{L}(E, F)$. Tout supplémentaire de $\text{Ker } u$ est **isomorphe** à $\text{Im } u$.

## Caractérisation des bases
- Soit $(x_{1},\dots x_{n})$ une famille de vecteurs dans $E$. On lui assoice l'application linéaire $\phi$ tel que : $$\phi:\begin{cases}
\mathbb{K}^p &\to E \\
(\lambda_{1},\dots,\lambda_{n}) &\mapsto \sum_{k=1}^p\lambda_{k}x_{k}
\end{cases}$$
- $(x_{1},\dots,x_{n})$ est une base de $E$ ssi $\phi$ est un **isomorphisme**.

## Théorème d'isomorphisme
- Deux espace vectoriels de dimension finie sont **isomorphisme** ssi ils ont la même dimension.
