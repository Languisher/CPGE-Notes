## Inégalité de convexité discrète
```ad-note
title: Inégalité de convexité *discrète*
Soit $f:I \to \mathbb{R}$ *convexe*, tq $(\lambda_{1},\dots,\lambda_{n})\in(\mathbb{R}_{+})^n$, alors $$f\left( \frac{1}{\sum_{k=1}^n \lambda_{k}}\sum_{k=1}^n\lambda_{k}x_{k} \right) \leq \frac{1}{\sum_{k=1}^n\lambda_{k}}\left( \sum_{k=1}^n\lambda_{k}f(x_{k}) \right)$$Autrement dit :  *L'image du barycentre à coefficients positifs est inférieure ou égale au barycentre des images*.
```
```ad-note
title: Inégalité de Cauchy-Schwarz *discrète*
- Retour vers l'**inégalité de Cauchy-Schwarz** : $$<x,y> \leq |x| |y| \iff \left( \sum a_{i}b_{i} \right)^2\leq \sum a_{i}^2 \sum b_{i}^2 $$![[截屏2023-03-21 10.26.34.png]]
```

```ad-note
title: Inégalité de Hölder *discrète*
Soit $p$ et $q$ deux nombres réels de $]1, +\infty[$ tels que $$\frac{1}{p}+\frac{1}{q}=1$$Soit $(a_{1},\dots,a_{n},b_{1},\dots,b_{n})\in \mathbb{R}_{+}^{2n}$. Alors, $$\sum_{k=1}^na_{k}b_{k }\leq\left( \sum_{k=1}^na_{k}^p \right)^{\frac{1}{p}}\left( \sum_{k=1} ^nb_{k}^p\right)^{\frac{1}{q}}$$
```

## Inégalité de Jensen
```ad-note
title: Inégalité de Jensen ou Inégalité de convexité *continue*
Soit $I$ un intervalle de $\mathbb{R}$, soit $f$ et $h$ définis, continues par morceaux sur $I$ avec $h \geq 0$, et telles que $$\int _{a}^b h(t) \, \mathrm{d}t \text{ et } \int _{a}^b f(t)h(t) \, \mathrm{d}t \text{  existent et } \int _{a}^b h(t) \, \mathrm{d}t>0 $$
Soit $\phi$ une fonction *convexe* définie sur un intervalle ouvert $J$ contenant $f(I)$ et telle que $$\int _{a}^b \phi(f(t))h(t) \, \mathrm{d}t \text{  existe}$$Alors, $$\boxed{\phi\left( \frac{1}{\int _{a}^b h(t) \, \mathrm{d}t }\int _{a}^b f(t)h(t) \, \mathrm{d}t  \right)\leq \frac{1}{\int _{a}^b h(t) \, \mathrm{d}t } \int _{a}^b \phi(f(t))h(t) \, \mathrm{d}t }$$
> Démonstration : considérer $\forall x\in I,\;\phi(m) \geq ax+ b$, ![[截屏2023-03-21 10.45.49.png]]
- Cas spécial : $$\phi\left(  \frac{1}{b-a}\int _{a}^b f(t) \, \mathrm{d}t \right) \leq \frac{1}{b-a}\int _{a}^b \phi(f(t)) \, \mathrm{d}t $$
```

```ad-note
title: Inégalité de Cauchy-Schwarz *continue*
En justifiant que tous les choses existents, on a : $$|\int _{a}^b f(t)g(t) \, \mathrm{d}t | \leq \sqrt{ \int _{a}^b f(t)^2 \, \mathrm{d}t  }\;\sqrt{ \int _{a}^b g(t)^2 \, \mathrm{d}t  }$$
```

```ad-note
title: Inégalité de Hölder
En justifiant que tous les choses existents, on a : $$\boxed{ | \int _{a}^b f(t)g(t) \, \mathrm{d}t| \leq \left( \int _{a}^b |f(t) |^p\, \mathrm{d}t  \right)^{1/p} \left( \int _{a}^b |g(t) |^q\, \mathrm{d}t  \right)^{1/q}} $$
```



