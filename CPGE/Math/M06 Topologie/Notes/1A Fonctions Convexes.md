## Définitions
```ad-note
title: Convexe, Concave, Affine
- **Définition** : Soit $f:I\to \mathbb{R}$, $f$ est dite **convexe** si elle vérifie $$\forall(a,b) \in I^2,\; \forall t\in [0, 1],\;f((1-t)a+tb))\leq (1-t)f(a)+tf(b)$$
- $f$ est dite **concave** si elle vérifie $$-f \text{ est convexe}$$
- Si $f:I\to \mathbb{R}$ est à la fois **convexe** et **concave**, alors $f$ est **affine**.
- **Propriété** : *Sur l'intervalle* $[a,b]$, la courbe passe *en-dessous* de sa corde entre $a$ et $b$. *En-dehors de l'intervalle* $[a,b]$, elle passe *au-dessus* de cette corde. ![[截屏2023-03-14 10.22.12.png]]
- **Propriété** : la **midconvexité** - Soit $f$ est une fonction **continue** sur $I$, alors $$[f \text{ convexe}] \iff [\forall(x,y)] \in I^2,\; f\left( \frac{x+y}{2} \right) \leq \frac{f(x)+f(y)}{2}$$
```


```ad-note
title: Épigraphe
- **Définition** : Soit $f: I \to \mathbb{R}$, on appelle **épigraphe** de $f$ l'ensemble $$\mathcal{E}_{f}=\{(x,y)\in I \times \mathbb{R},\; y\geq f(x)\}$$![[截屏2023-03-14 10.29.59.png]]
- Soit $\mathcal{C}\subset \mathbb{R}^n$, On dit que $\mathcal{C}$ est **convexe** (c'est-à-dire **partie convexe**) si $$\forall(A,B) \in \mathcal{C}^2,\; \forall t\in [0, 1], \; \mathrm{Bar}((A,1-t),(B,t))\in \mathcal{C}$$
- **Propriété** : La fonction $f$ est convexe $\iff$ L'**épigraphe** $\mathcal{E}_{f}$ de $f$ est un ensemble convexe
```

```ad-note
title: Inégalité des pentes
- **Propriété** : **Inégalité des pentes** : On a que $f$ est **convexe** ssi : pour $\forall (x,y,z) \in I^3$, $$[x<z<y] \implies \left[ \frac{f(z)-f(x)}{z-x}\leq \frac{f(y)-f(x)}{y-x} \leq \frac{f(y)-f(z)}{y-z}\right]$$![[截屏2023-03-14 11.00.38.png]]
 ```
 
```ad-note
title: Taux d'accroissement d'une fonction convexe
- **Propriété** : L'application de $f$, $f$ est **convexe** ssi : $$\tau_{x}:\begin{cases}
I\backslash\{x\} &\to \mathbb{R}  \\
t&\mapsto \frac{f(t)-f(x)}{t-x}
\end{cases} \text{ est croissante}$$
```

```ad-warning
title: Si $f:I\to \mathbb{R}$ une fonction **convexe**, alors $f$ est **continue** sur $I^\circ$.
```
```ad-attention
title: Si la fonction est **continue** et **dérivable** : $$[f \text{ convexe sur } I] \iff [f' \text{ croissante sur }I^\circ]$$
```
```ad-attention
title: Si la fonction est **continue** et deux fois **dérivable** : $$[f \text{ convexe}] \iff [f''>0]$$
```


## Matériaux
- Cours : 2023-03-14 Matériaux : [[Slides_topologie_calcul_diff_rentiel_2022_2023-3.pdf]]