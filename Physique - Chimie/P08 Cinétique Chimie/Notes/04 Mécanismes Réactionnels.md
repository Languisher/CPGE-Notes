> Date : 2023-03-01 Matériaux : [[Thermochimie_Cours_CH1_Partie3-3.pdf]]

## Notions fondamentales 
Une équation bilan ne donne aucune information sur les mécanismes microscopiques qui se déroulent par étapes (selon le nombre de réactifs impliqués) appelés actes élémentaires.

```ad-note
title: Acte Élémentaire
- **Acte élémentaire** :  
Processus dans lequel peu d’entités (1, 2 ou 3 molécules, ions ou atomes) interagissent et produisent aussi peu de nouvelles entités. 
- La **molécularité** est le nombre de réactifs impliqués.  
- Un **acte élémentaire** 用单个箭头表示。
- Les **coefficients stœchiométriques** sont les nombres réels d’entités interagissant.
```

```ad-note
title: IR
- **Intermédiaires réactionnels** (IR) :  
	- Produit peu stable d’un **acte élémentaire**, se transforme rapidement en une autre espèce.  
	- Les IR *ne figurent pas dans le bilan global* de réaction et existent en *très petite quantité* dans le mélange réactionnel. Ces espèces peu stables sont de différentes natures (radicaux libres, carbocations notamment).
```

## Loi de Van't Hoff

```ad-note
title: Loi de Van't Hoff
- **Loi de Van't Hoff** : un acte élémentaire possède une loi de vitesse avec ordre, dont *les ordres partiels sont les coefficients stœchiométriques*. *L’ordre global est égal à la molécularité*.
```

## AEQS
```ad-note
title: AEQS
- **Approximation de l’étape cinétiquement déterminante** (AEQS) 
	- Cette approximation concerne *une succession de réactions élémentaires* dont l’une a une constante de vitesse beaucoup plus faible que les autres. 
	- *En première approximation*, la vitesse de la réaction est égale à la vitesse de l’étape cinétiquement déterminante, qui est celle ayant la constante de vitesse *la plus faible*
- Si $A^\cdot$ est un **IR**, en **AEQS** on peut écrire : $$\frac{\mathrm{d}[A^\cdot]}{\mathrm{d}t}\approx 0=\sum_{i=1}^n v_{i}$$
```

- 似乎分解反应没有配平并不影响反应速率，即不需要乘以系数（需要验证）
## Exemple 
1. Cas la molécularité trop grande donc impossibilité d'un acte élémentaire : ![[Assets/截屏2023-03-01 09.24.01.png]]
2. Cas des actes élémentaire : $R=(1)+(2)+2(3)$ avec $IR: HBrOO \text{ et } HBrO$ ![[Assets/截屏2023-03-01 09.25.40.png]]
3. La loi de vitesse, montrer que c'est d'ordre 1 : $$n_{HBr} = n_{HBr,0} - \xi_{1}-\xi_{2}-\xi_{3} \implies v = - \frac{1}{4} \frac{\mathrm{d}[HBr]}{\mathrm{d}t} = \frac{1}{4}(v_{1}+v_{2}+v_{3})$$
	- D'après la **loi de Van't Hoff** : $v_{1}=k_{1}[HBr][O_{2}], v_{2}=k_{2}[HBrOO][HBr], \; v_{3}= k_{3}[HBrO][HBr]$
		Si d'après l'AEQS, $$0 = \frac{\mathrm{d}{[HBrOO]}}{\mathrm{d}t}= v_{1}-v_{2} \implies v_{1}=v_{2}$$ et $$0 = \frac{\mathrm{d}[HBrO]}{\mathrm{d}t}=2v_{2}-v_{3}\implies v_{3}=2v_{2}=2v_{1}$$
	- Donc, $$v = v_{1}= k_{1}[HBr][O_{2}]$$
4. Pourquoi dit-on que l’étape (1) est cinétiquement déterminante ?
	- Par nos calculs, $v=v_1$ mais en fait l'AEQS suppose que $k_{2}\gg k_{1}$. Donc la réaction totale est limitée par $(1)$

## Influence de la température
En générale, la vitesse de réaction augmente lorsque la température augmente.
```ad-note
title: Loi d'Arrhenius
**Theorème:  Loi d'Arrhenius** (Loi semi-empirique)
Pours les réactions avec ordre, la **constante de vitesse** $k$ varie généralement selon $$k=Ae^{- \frac{E_{a}}{RT}}(A>0)$$C'est-à-dire $k$ augmente lorsque $T$ augmente. Ici, $E_{a}$ appelle l’**énergie d’activation**.
```

L’évolution d’une transformation peut-être représenté par un **chemin réactionnel** (abstrait ou non). 
La **coordonnée de réaction** $u$ (variable abstraite) positionne *l’état du système sur ce chemin*.
Le tracé de l'énergie en fonction de la coordonnée de réaction est appelé **diagramme de réaction**.

- **Modèle du complexe activé**
- La loi d’Arrhenius s’interprète simplement dans le cas d’un acte élémentaire bimoléculaire : $$A+B →C$$
- Quand $u= 0$, $A$ et $B$ sont bien séparés. 
- Quand $u= 1$, $A$ et $B$ ont formé l’entité stable C. 

Entre les deux, le système doit passer par un état d’énergie potentielle $E_p(𝑢)$ élevée et donc très **instable**, appelé état de transition correspondant à un **complexe activé** de durée de vie très courte.
- Entre les deux, le système doit passer par un état très instable, appelé **état de transition**, d’énergie potentielle plus élevée que les états $A + B$ ou $C$.
![[Assets/截屏2023-03-01 09.42.37.png]]

```ad-note
title: Catalyse
- Un **catalyseur** est une espèce qui augment la vitesse d'une réaction sans apparaître dans l'équation bilan. ![[截屏2023-03-08 08.12.33.png]]
- L'*équilibre final* n'est pas modifié mais est atteint plus rapidement.
- Type : **Catalyse Homogène** ![[截屏2023-03-08 08.16.19.png]]
- Type : **Catalyse Hétérogène** ![[截屏2023-03-08 08.16.42.png]]
- Type : **Catalyse enzymatique**
```
