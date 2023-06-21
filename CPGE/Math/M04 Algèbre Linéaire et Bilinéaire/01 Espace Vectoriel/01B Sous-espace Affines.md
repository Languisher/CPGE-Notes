## Translations
```ad-note
title: Translation
- **Définition** : L'application de $E$ dans $E$ définite par et notant par $t_{a}$ est appelée **translation** de vecteur $a$ (un élément d'un ev $E$) : $$t_{a}: x \mapsto a+x$$
- **Propositions** : 
	- $t_{a}\circ t_{b} = t_{b}\circ t_{a}$
	- $t_{a}$ est bijective, aussi $t_{a}^{-1}=t_{-a}$
```

## Sous-espace Affine
```ad-note
title: Sous-espace Affine
- Une partie $\mathcal{F}$ de $E$ est un **sous-espace affine de $E$** si l'on peut trouver $a\in E$ et un sous-ev $F \in E$ qui suffit : $$\mathcal{F}= a+F$$![[截屏2023-03-11 15.07.02.png]]
- On a $$\mathcal{F}= a+F=a'+F' \text{ ssi } F=F' \text{ et } a'-a\in F$$
- On dit $\mathcal{F}$ est **passant** par $a$ et **dirigé** par $F$. Le sous-espace vectoriel $F$ est appelé la **direction de $\mathcal{F}$**.
```ad-hint
title: Pour prouver une partie $\mathcal{F}$ est un **sous-espace affine** passant par $a$ et dirigé par $F$
Essayer de prouver que $$x\in \mathcal{F} \iff x-a \in F$$ 
```



```ad-note
title: Droite Affine
Lorsque la direction $F$ de $\mathcal{F}$ est une droite vectorielle, c'est-à-dire $F = \text{Vect}\{a\}$, le **sous-espace affine** est appelé **droite affine**.
```

## Ensemble des solutions d'une équation linéaire
- Soit $u \in \mathscr{L}(E,F)$, et $b\in F$. Si l'ensemble $$\mathcal{F}_{b} \text{ des solutions de l'equation } u(x)=b$$Alors : C'est un **sous-espace affine** de $E$ de direction $\text{Ker }u$
- > Démonstration : ![[截屏2023-03-12 09.16.54.png]]
- Utilisation : On a déjà rencontré le résultat précédent dans divers contextes ; il était alors énoncé sous la forme : « pour *obtenir toutes les solutions* de l’équation linéaire $u(x) = b$, il suffit d’*en connaître une* (alors appelée solution particulière), et de lui ajouter *toutes les solutions* (ou encore la solution générale) de l’**équation homogène associée**, $u(x) = 0$ »