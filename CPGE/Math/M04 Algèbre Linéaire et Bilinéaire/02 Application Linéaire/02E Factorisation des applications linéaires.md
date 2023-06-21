## Restriction et Co-restriction
```ad-note
title: Restriction d'une application linéaire
- Soit $F$ un sous-espace vectoriel de $E$, la **restriction** de $f \in \mathscr{L}(E, E')$ est notée et définie par : $$\forall x\in F,\;f_{|F}(x)=f(x)$$Elle est de $F$ (pas $E$) dans $E'$
```

```ad-note
title: Co-restriction d'une application linéaire
- Soit $F'$ un sous-espace vectoriel de $E'$, et plus importante, ==$f(E) \subset F'$==, alors la **co-restriction** de $f\in \mathscr{L}(E, E')$ est notée et définie par : $$\forall x\in E, f^{|F'}=f(x) \in F'$$Elle est de $E$ dans $F'$
```

- Notation : Soit $F$ un sous-espace vectoriel de $E$; Soit $F'$ un sous-espace vectoriel de $E'$, ==$f(F) \subset F'$==, nous noterons : $$f|_{F}^{F'}=(f_{|F})^{F'}$$
- Propriété : réstriction du noyau $$\text{Ker}(f_{|F})=F \cap \text{Ker}(f)$$
```ad-note
title: Inclusion canonique
- Soit $F$ un sous-espace vectoriel de $E$, l'**inclusion canonique de $F$ dans $E$** par : $$i_{F\subset E}=(\mathrm{id}_{E})_{|F}:\begin{cases}
F &\to E \\
x &\mapsto x
\end{cases}$$
```

- Propriété : Si on connaît $E = \bigoplus E_{i}$, il faut et il suffit d'en connaître ses *restrictions à chaque sous-espace vectoriel* : $$\mathscr{L}(E,E') \text{ est isomorphe à  }\prod_{i\in I}\mathscr{L}(E_{i},E')$$
- Exemple : $f\in \mathscr{L}(E)$, On construit $f_{|F=\text{Ker}(f)}=0_{\mathscr{L}(F,E)}$, $f_{|G=\text{Im}(f)}=(\text{id}_{E})_{|G}$, où $E=F \oplus G$
```ad-note
title: Factorisation des applications linéaires
Soit $E$ et $E'$ deux $\mathbb{K}$-espaces vectoriels, $f \in \mathscr{L}(E, E')$, $F$ suffit $E = \text{Ker}(f) \oplus F$, alors : $$\hat{f}=f|_{F}^{\text{Im}(f)} \text{ est un isomorphisme entre } F \text{ et } \text{Im}(f)$$
```
- Pourquoi ? Car $\text{Ker}(\hat{f})=\text{Ker}(f)\cap F$, et ils ont en somme directe.

## Résumé
![[截屏2023-03-04 22.58.01.png]]