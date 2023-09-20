> Date : 2023-02-15 Matérial : [[Assets/Thermochimie_Cours_CH1_Partie1.pdf]]


## Définitions
- Un système réactionnel *fermé* de *volume* $V$ *constant*, constitué d'un certain nombre d'*espèces physico-chimiques* notée $C_i$ 
- On note $n_{i}$ la **quantité de matière** de $C_{i}$
- On note $[C_{i}]$ la **concentration** de $C_{i}$, la *quantité rapportée au volume total* du mélange qui contient cette espèce. Elle est exprimée en moles par unité de volume.
```ad-note
title: Vitesses Volumiques de Formation, Vitesses Volumiques de Disparition
- **Vitesses volumiques de formation** de l'espèce $C_i$ $$v_{f} (C_{i})= \frac{1}{V} \frac{dn_{i}}{dt}=\frac{d[C_{i}]}{dt}$$
- **Vitesses volumiques de disparition** $$v_{d}(C_{i}) = -\frac{1}{V} \frac{dn_{i}}{dt}= - \frac{d[C_{i}]}{dt}$$
```

- Elles s'expriment en $\text{mol}.L^{-1}.s^{-1}$
- Unité courante :
	- $C_{i}$ est un produit, on considère plutôt $v_{f}(C_{i})\geq 0$
	- $C_{i}$ est un réactif, on considère plutôt $v_{d}(C_{i})\geq 0$
```ad-note
title: Vitesse Volumique de Réaction
- Rappel : **Avancement de la réaction** : $\xi$, D'après $$n_{i}=n_{i,o}+ \nu_{i}\xi$$ [[00 Notations Basiques]], donc$$\frac{dn_{i}}{dt}= \nu_{i} \frac{d\xi}{dt} \implies \frac{1}{V} \frac{d\xi}{dt}= \frac{1}{\nu_{i}V} \frac{dn_{i}}{dt}$$
- Cela nous implique la définition de la **vitesse volumique de réaction** : $$v= \frac{1}{V} \frac{d \xi}{dt}= \frac{1}{\nu_{i}} \frac{d[C_{i}]}{dt}$$
```

- Si $C_{i}$ est un produit, $\nu_{i}>0$, et $v_{f}(C_{i})=\nu_{i}v \geq 0$, si $C_{i}$ est un réactif, $v_{d}>0$, $v_{d}(C_{i}) = -\nu_{i}v \leq 0$.

```ad-note
title: Temps de Demi-Réaction
- **Temps de demi-réaction** : $t_{1 /  2}$ qui suffit : $$\xi\left( t=t_{1 / 2} \right) = \frac{\xi_{f}}{2}$$durée au bout de laquelle *la moitié de l'avancement final est atteinte*.
	- Analogie : temps de demi-vie (ou période radioactive) d'un nucléide radioactif.
```

- **Facteur cinétique** : Il s'agit de tout élément qui peut influencer la vitesse d'une réaction.
	- température
	- concentration des réactifs
	- présence d'un catalyseur
	- autres : pression (réactif gazeux), nature des solvants, rayonnement

## Déterminations expérimentales
### Principe Général
- Considérons une réaction unique et un réactif noté $A$.
- Pour déterminer $v_{d}(A)$ et en déduire la vitesse de réaction $v$, ainsi que le temps de demi-réaction $t_{1/2}$ , on mesure $[A]$ au cours du temps pour obtenir la courbe $[A](t)$.
- Pour déterminer $t_{1 / 2}$, il faut mesurer $[A]$ jusqu'à valeur d'équilibre $[A]_{\infty}$. On a : $$[A]_{1 / 2} = \frac{1}{2}([A]_{0}+[A]_{\infty})$$![[Assets/截屏2023-02-15 09.11.33.png]]
### Déterminer la concentration
- Méthodes physiques de mésure de la concentration : en utilisant en continu et ne perturbent pas la réaction :
	- Conductimétrie : suivre l'évolution de la **conductance** $G$ (en $S$) ou de la **conductivité** $\sigma$ (en $S.m^{-1}$). On écrite : 
		- $G = k_{\text{cell}}\sigma$, où $k$ la **constante de cellule** en $m$ 
		- $\sigma=\sum_{i, \text{ ionique}}\lambda_{i}[c_{i}]$ où $\lambda_i$ est la conductivité ionique molaire de l’ion i (en $S·m^2 · mol^{-1}$) et $c_i$ sa concentration molaire (en mol·m3).
	- Spectrophotométrie : mesurer l'**absorance** $A$ du mélange à une longueur d'onde donnée.
		- obéit à la loi de Beer-Lambert : $A = \varepsilon_{\lambda}\times l\times c$
	- PH-métrie : mesurer de $\text{pH}= -\frac{\log[H_{3}O^+]}{c}$ donc de $[H_{3}O^+]$ ou de $[OH^-]$
	- Mesure de pression : $P = \frac{n_{\text{tot, gaz}}RT}{V}= \sum_{i,\text{ gaz}}[C_{i}]RT$ dans un cadre de $V$ et $T$ constantes.