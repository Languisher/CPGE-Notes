## Limite
```ad-note
title: Limite
Soit $f:A \to F$ une application, on dit que **$f$ tend vers $l\in F$ en $a$ (adhérent à $A$)** si : $$\forall \varepsilon >0, \; \exists \eta >0,\; \forall x \in A,\; \Vert x-a\Vert  \leq \eta\implies \Vert f(x)-l\Vert  \leq \varepsilon$$
**Notation** : $$f(x) \underset{x \to a}{\to}l$$
```
## Continuité
```ad-note
title: Contiunité
- Une fonction $f:]a,b[ \to \mathbb{R}$ est **continue** **en** $x \in ]a,b[$ si : $$\begin{align}
\forall \epsilon >0,\; \exists \eta>0,\;\forall y\in]a,b[,\; |x-y|< \eta \implies |f(x)-f(y)|< \epsilon
\end{align}$$
- Soit $f:O \to \mathbb{R}^p$, une fonction $f$ est dite **continue** **en** $x \in O$ si : $$\begin{align}
\forall\varepsilon >0, \; \exists \eta>0,\; \forall y\in \underbrace{BO(x,\eta)}_{\Vert x-y \Vert < \eta}  \implies \underbrace{f(y) \in BO(f(x), \varepsilon}_{\Vert f(x)-f(y)\Vert < \varepsilon})
\end{align}$$
- La fonction $f$ est **continue en** $x\in O$ ssi $f_{j}$ est continue en $x\in O$ pour tout $j \in \{1,\dots,p\}$
- La fonction $f$ est dite **continue sur** $O$ si elle est continue en tout $x \in O$.
- *L'ensemble des fonctions continues sur $O$ à valeurs dans $\mathbb{R}^p$* est noté : $$\mathcal{C}^0(O,\mathbb{R}^p)$$
	- L'ensemble est stable par addition, multiplication, division (si le dénominateur ne s'annule pas)
	- > Exemple : Fonction polynomiale, $(x,y,z) \mapsto x^2+y^2x + 3xyz$
```

```ad-attention
title: $f$ est continue, alors toutes les application partielles $f_{j}$ sont continues. La réciproque est FAUSSE.
Exemple : $$f(x,y) = \begin{cases}
\frac{xy}{x^2+y^2} &\text{ si } (x,y) \ne (0,0) \\
0 &\text{ sinon}
\end{cases}$$
```


```ad-hint
title: Pour prouver $f$ est continue en $a \in A$
Pour prouver $f$ est continue en $a \in A$, on prouvera que 
- $f$ est un composé des fonctions de classe $\mathcal C^0$
- $f$ admet une limite en $a$ ([[01 Limite et Continuité#Limite]])
```

```ad-hint
title: Pour établir l’existence d’une limite en 0
Pour établir l’existence d’une limite en 0, il est parfois utile d’évaluer $f(r\cos θ, r \sin θ)$ et de considérer son comportement lorsque $r$ tend vers 0.
Exemple : ![[截屏2023-03-11 09.29.15.png]]![[截屏2023-03-11 09.29.49.png]]
```

```ad-question
- Montrer qu'une fonction est continue en un point (spécial) : TD2-5-2
```
