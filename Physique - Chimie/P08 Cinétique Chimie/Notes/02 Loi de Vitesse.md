## Définitions

```ad-note
title: Loi de Vitesse
- **Notion de loi de vitesse** : La **vitesse de réaction** [[01 Vitesses et temps dans un système réactionnel#Définitions]] en fonction des **concentrations** $$v = f([C_{1}],[C_{2}],\dots,[C_{n}])$$
```
```ad-note
title: Réaction avec ordre, ordres partiel et global
- **Réaction avec ordre :** $$v = k[C_{1}]^{p_{1}}[C_{2}]^{p_{2}}\dots[C_{n}]^{p_{n}}$$
	- $v$ dépend des $[C_{i}]$
	- $p_{i}$ est l'**ordre partiel** associé à $C_{i}$ (entier ou fractionnaire)
	- L'**ordre global** de la réaction est la *somme des ordres partiels* : $$p=p_{1}+p_{2}+\dots+p_{n}$$.
```

- Exemple de réaction avec ordre : $$CO_{(g)}+Cl_{2(g)}=COCl_{2(g)}$$ ici $v = k[Cl_{2}][CO]^{3 / 2}$, donc $p_{Cl_{2}}=1,\;p_{CO}=\frac{3}{2}$.

## Cas d'une réaction d'ordre 0
![[Assets/Pasted image 20230222084950.png]]

- Ici, $\forall i,\; p_{i }=0$, alors $v = k = \text{constante}$, On a $$v = k=- \frac{1}{\alpha} \frac{\mathrm{d}[A]}{\mathrm{d}t} \text{ donc } [A] = [A]_{0} - k \alpha t$$
- Si la réaction est totale, et $A$ est limitant, $$\frac{[A]_{0}}{2}=[A](t=t_{1 / 2})= [A]_{0}-k\alpha t_{1 / 2} \text{ donc } t_{1 / 2} = \frac{[A]_{0}}{2 k \alpha}$$ ![[Assets/Pasted image 20230222085453.png]]

## Cas d'une réaction d'ordre 1
- Ici $v = k[A]$, On a $$v = k[A] = - \frac{1}{\alpha} \frac{\mathrm{d}[A]}{\mathrm{d}t} \text{ donc } [A](t)=[A]_{0}e^{-\alpha kt }$$
- Si la réaction est totale et $A$ est limitant, $$\frac{[A]_{0}}{2}=[A](t=t _{1 / 2})= [A]_{0}e^{-\alpha k t_{ 1/ 2}} \text{ donc } t_{1 / 2}=\frac{\ln 2}{\alpha k}$$
## Cas d'une réaction d'ordre 2
- Ici, $v = k[A]^2$. On a (après une simple intégration) $$v = k[A]^2=-\frac{1}{\alpha} \frac{\mathrm{d}[A]}{\mathrm{d}t} \text{ donc } [A](t) = \frac{[A]_{0}}{1+[A]_{0}k\alpha t}$$
- Si la réaction est totale et $A$ est limitant, $$\frac{1}{[A]_{0} / 2}- \frac{1}{[A]_{0}}= k \alpha t_{1 / 2} \text{ donc } t_{1 / 2} = \frac{1}{k \alpha [A]_{0}}$$

## Simplification d'une loi de vitesse
$$
\forall t, \;\frac{n_{1}}{\alpha_{1}}= \frac{n_{2}}{\alpha_{2}} = \dots \implies\frac{[A_{1}]}{\alpha_{1}}= \frac{[A_{2}]}{\alpha_{2}} = \dots
$$
D'où
$$
v= k'[A_{1}]^{p} \text{ avec } k'=\frac{\alpha_{2}^{p_{2}}}{\alpha_{1}^{p_{2}}} \times \dots \times \frac{\alpha_{n}^{p_{n}}}{\alpha_{1}^{p_{n}}}\times k
$$
## Dégénérescene de l'ordre
$$
\frac{n_{1,0}}{|\nu_{1}|} \ll \frac{n_{i,0}}{|\nu_{i}|}, \; \forall i \in [\![2,n]\!]
$$
La loi de vitesse se simplifie sous la forme : $$v = k_{\text{app}}[A_{1}]^{p_{1}}$$
Une **constante de vitesse apparente** : $$k_{\text{app}} = k[A_{2}]^{p_{2}}\dots[A_{n}]^{p_{n}}$$
## Détermination expérimentale d'une loi de vitesse
*Principe* : 
- Hypothèse d'un modèle mathématique
- Déduction de l'évolution de la concentration d'une ou plusieurs espèces
- Comparaison avec les résultats expérimentaux

On suppose $$v = k[A]^p$$
### Méthode différentielle pour trouver un ordre
Il faut mesurer $\mathrm{d}[A] / \mathrm{d}t$ et $[A]$ en fonction de $t$.
On trouve $$\ln \left( -\frac{\mathrm{d}[A]}{\mathrm{d}t} \right)=\ln\alpha k+p\ln[A]$$
Une régéneration linéaire donne $p$ et $k$ (avec l'origine donne la valeur en connaisant $\alpha$)

> Date : 2023-03-01 Matériaux : [[Assets/Thermochimie_Cours_CH1_Partie3.pdf]]

### Méthode intégrale pour confirmer un ordre supposé
Il faut mesurer $t$ et $[A]$ en fonction de $t$.
On cherche alors une fonction de $[A]$ affine avec $t$, validée par une régression linéaire.
- Si $p=0$, $[A](t)=[A]_{0}-k\alpha t$
- Si $p=1$, $\ln [A](t) = \ln[A]_{0}-k\alpha t$
- Si $p=2$, $1 / [A](t) = 1 / [A]_{0}+ k\alpha t$

### Méthode du temps de demi-réaction
On détermine $t_{1 / 2}$ pour différentes valeurs de $[A]_{0}$
- Si $p=0$, $t_{1 / 2}= [A]_{0} / 2k \alpha$, proportionnel à $[A]_{0}$
- Si $p=1$, $t_{1 / 2}= \ln 2 / \alpha k$, indépendant de $[A]_{0}$
- Si $p=2$, $t_{1 / 2 }= 1 / [A]_{0}\alpha k$, proportionnel à $1 / [A]_{0}$

(Plus généralement, $t_{1 / 2}$ est proportionnel à $[A]_{0}^{1-p}$)

