```ad-note
title: Noyau et Image d'une application linéare
Soit $u \in \mathscr{L}(E,F)$, On appelle :
- **noyau** de $u$, notant $\text{Ker }u$, le sous-espace vectoriel de $E$ : $$\text{Ker } u=u^{-1}(\{0\})=\{x\in E, \; u(x)=0\}$$
- **image** de $u$, notant $\text{Im }u$, le sous-espace vectoriel de $F$ : $$\text{Im } u=u(E) = \{u(x),\; x \in E\}$$
- Exemple : ![[截屏2023-03-11 14.44.54.png]]
```

```ad-note
title: Injectivité et Noyau
- **Théorème** : Une application est **injective** ssi $\text{Ker }u=\{0\}$
- Exemple : ![[截屏2023-03-11 14.47.02.png]]
```

```ad-hint
title: Pour montrer qu'une application est **injective**
Pour démontrer qu’une application linéaire est injective, systématiquement prouver $\text{Ker }u = \{0\}$ ou plus simplement (puisque $\{0\} ⊂ \text{Ker }u$) : $$∀x ∈ E,\; u(x) = 0 ⇒ x = 0$$Évidemment, il faut savoir que $u$ est une application linéaire
```
