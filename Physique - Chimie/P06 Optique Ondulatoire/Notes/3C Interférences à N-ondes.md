## Interférences à N-ondes
```ad-note
title: Réseau de diffraction, Pas du réseau
- Un **réseau de diffraction** est un objet plan présentant une structure périodique selon un
axe $(Ox)$ avec une période spatiale a de l’ordre de grandeur des longueurs d’onde de la
lumière visible qui est appelée pas du réseau. 
- Le dispositif est constitué d'un nombre quelconque $N$ de fontes ou de trous de Young. Les fentes sont réparties périodiquement avec une période $a$ appelée **pas du réseau**.
- $N$ est souvent dit le **nombre de traits par unité de longueur**
$$N = \frac{1}{a}$$![[截屏2023-03-08 22.36.46.png]]
```

```ad-note
title: Configuration de Fraunhofer
- **Configuration de Fraunhofer** : Source $S$ et Observateur $M$ sont à l'infini
![[截屏2023-03-02 10.12.47.png]]（注：图中 $T_{m+1}$ 和 $T_m$ 需要调换一下）
```

```ad-note
title: Déphasge entre deux ondes adjacentes
L’état d’interférences de ce type de dispositif est entièrement déterminé par le déphasage entre deux ondes passant par des trous voisins.
- **Déphasage** et **Différence de marche** entre deux ondes adjacentes : $$\boxed{\begin{align}
\delta(M) &= a(\sin \theta-\sin\theta_{0}) \\
\Delta \varphi(M) &= \frac{2\pi}{\lambda_{0}}a(\sin\theta-\sin\theta_{0})
\end{align}}$$(Rappel que $k_{0} = 2\pi / \lambda_{0}$ [[1A Modèle scalaire de la lumière]]) car $$\begin{align}
\delta _{(m+1) / m}(M) = (ST_{m+1}M)- (ST_{m}M) = (T_{m+1}K)-(HT_{m}) 
\end{align}$$
```

## Caractéristiques Générales de l'Éclairement

```ad-note
title: Relation des Réseaux, Maxima Principaux, Ordre de diffraction
- **Relation fondamentale des réseaux** : Les **maxima principaux** de l'intensité *(lexique : il n'y pas de s dans maxima*) est obtenue lorsque toutes les ondes sont en phase vérifiant $$\boxed{a[\sin \theta-\sin\theta_{0}]=m\lambda_{0}}$$avec $m$ appelé **ordre de diffraction** 
- Cette relation est indépenante du $N$
```

```ad-note
title: Amplitude Totale
D'après [[1A Modèle scalaire de la lumière]],
- L'amplitude de l'onde rayonné par la source $m$ est reliée à l'amplitude de l'ordre $m=1$ par :
- L'éclairement (intensité) maximale est atteinte lorsque $\Delta \varphi = m\times {2}\pi$, aussi donné par (c'est pris losrque la direction d'observation vérifie la **loi des réseaux**) : 
- L'éclairement (intensité) totale est donné par :
$$\begin{align}
\underline{s_{1}}(M,t) &=  \underbrace{[ae^{-j \varphi_{1}}]}_{\underline{A_{1}}(M_{\infty})}e^{j\omega t} \\
\underline{A_{m}}(M_\infty) &= \underline{A_{1}}(M_{\infty})e^{-j \Delta \varphi_{n / 1}} \\
&= \underline{A_{1}}(M_{\infty})e^{+j(n-1)\Delta\varphi} \text{ avec } \Delta\varphi = \varphi_{n}-\varphi_{n+1}\\
\underline{A_{\text{tot} }} &= \underline{A_{1}}\sum_{i=1}^N \exp[j(i-1)\Delta \varphi] \\
&= \underline{A_{1}} \exp\left( j \frac{N-1}{2}\Delta \varphi  \right) \frac{\sin \left( \frac{N}{2} \Delta \varphi \right)}{\sin \left(  \frac{1}{2} \Delta \varphi \right)} \\ 
I_{\text{max}} &= \sum_{n=1}^N\underbrace{|\underline{A_{\text{tot}}}(M_\infty) |^2}_{\Delta \varphi = m \times 2\pi} = N^2\underbrace{I_{0}}_{I_{0}=|\underline{A_{1}(M_{\infty})}|^2}\\
I_{\text{tot}} &= \boxed{I_{0}\times \frac{\sin^2\left( \frac{N}{2}\Delta \varphi \right)}{\sin^2\left( \frac{1}{2}\Delta\varphi \right)} }= \frac{I_{\text{max}}}{N^2} \frac{\sin^2\left( \frac{N}{2}\Delta\varphi \right)}{\sin^2\left( \frac{1}{2}\Delta\varphi \right)}
\end{align}$$
- La figure représent le résultat : ![[截屏2023-03-13 21.45.21.png]]
```

> Démonstration : ![[Pasted image 20230302115225.png]]

### Dérivation dans un ordre donné
On appelle **dérivation pour l'ordre $m$ la quantité** : $$D_{m}= \theta_{m}-i$$![[截屏2023-03-13 21.46.31.png]]![[Pasted image 20230309102359.png]]
La contrainte $-1 \leq \sin \theta_{m} \leq 1$ limite le *nombre de valeurs* de $m$ prossibles : $$-1\leq \sin \theta_{m} = \frac{m\lambda_{0}}{a} + \sin i\leq 1$$
![[Pasted image 20230309103227.png]]

- Propriété : La **dérivation minimale** vérifie $$\boxed{\sin\left( \frac{D_{m,\min{}}}{2} \right)=\frac{m\lambda_{0}}{2a}}$$Démonstration : ![[Pasted image 20230309104104.png]]
## Cas Différentes
### A - Trou de Young - général
![[截屏2023-03-08 22.09.24.png]]
### B - Trou de Young - Configuration en franges de Pohl
![[截屏2023-03-08 22.17.15.png]]![[截屏2023-03-08 22.11.07.png]]![[截屏2023-03-08 22.15.58.png]]
### C - Biprisme de Fresnel
![[截屏2023-03-08 22.17.43.png]]![[截屏2023-03-08 22.19.53.png]]
### D - Bilentilles de Billet
On prend une lentille simple et on coupe en deux son diamètre et qu'on l'écarte.
![[截屏2023-03-08 22.21.11.png]]![[截屏2023-03-08 22.24.08.png]]
### E
![[截屏2023-03-08 22.28.30.png]]

### F
![[截屏2023-03-08 22.30.54.png]]


