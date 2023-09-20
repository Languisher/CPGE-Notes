
## Vibration Lumineuse
- La lumière est une onde électromagnétique, donc il se compose de deux champs de vecteurs couplés, subit $\vec{E}(M,t)$ et $\vec{B}(M,t)$, $B$ est très petite devant $E$ car $B = \frac{E}{c}$, avec $c=3 \times 10^8 \text{ m.s}^{-1}$. 

```ad-note
title: Signal Lumineux
- On appelle **vibration lumineuse** une composante quelconque du champ électrique par
rapport à un axe perpendiculaire à la direction de propagation, notée $s(M,t)$.
```

- **Détecteur**, exemple : l’œil 
- **Superposition** des signaux 波的叠加原理: $s(M,t) = s_{1}(M,t) + s_{2}(M,t)$ ![[Assets/截屏2023-02-25 15.10.51.png]]

## Intensité et Éclairement

```ad-note
title: Intensité ou Éclairement $I$
- Les détecteurs optiques ne sont sensibles qu’à la <u>valeur moyenne temporelle</u> de la **puissance rayonnée instantanée** $$<\mathrm{d}\mathcal{P}(M,t)> = <Ks^2(M,t)dS> \text{ avec } K=2$$
	- Rappelle : $<f(t)> = \lim_{ T \to \infty } \frac{1}{T}\int _{t_{0}}^{t_{0}+T} f(t)\, dt$ 
- On appelle **Intensité** ou **Éclairement** d'une surface, exprimée en $W.m^{-2}$, la puissance lumineuse moyenne reçue par unité de surface : $$I = \frac{<d\mathcal{P}>}{dS}$$On a aussi $$I(M)=K<s^2(M,t)>, \text{ avec } K = 2$$
```
> Date : 2023-02-16 Matérial : [[Assets/Chapitre1.pdf]]



## Lumière monochromatique
```ad-note
title: Lumière Monochromatique
![[Drawing 2023-02-14 09.19.12.excalidraw]]
- On appelle **lumière monochromatique** une vibration idéale *purement sinusoïdale* donc de la forme : $$\boxed{s(M,t) = a(M)\cos(\omega t- \varphi(M))}$$
- $a(M)$ est l'**amplitude optique** au point $M$
- $\varphi(M)$ est le **retard de phase** de l'onde au point $M$
```

- $n$ est l'**indice optique** du milieu $$n= \frac{c}{v}$$
- $\lambda_{0}$ est le **longueur d'onde dans le vide** $$\boxed{\lambda_{0}= cT= \frac{2\pi c}{\omega}=n \underbrace{\lambda}_{v \cdot T}}$$
- $\lambda$ est le **longueur d'onde dans le milieu** $$\lambda= \frac{\lambda_{0}}{n}$$
- $k_{0}$ **pulsation spatiale dans le vide** est $$\boxed{k_{0}= \frac{2\pi}{\lambda_{0}}= \frac{\omega}{c}}$$
- $k$ **Pulsation spatiale dans le milieu** est $$k = \frac{2\pi}{\lambda} = nk_{0}$$

```ad-caution
title: C'est une convention de retard. Change la signe $-$ à $+$ signifie que ce sera une convention d'avance.
```

### Notation complexe
- Signal sinusoïdal 
$$
\boxed{\begin{align}
\underline{s}(M,t) &=a(M).e^{j(\omega t- \varphi_{M} )} \\
&=\underbrace{\underline{A}(M)}_{a(M)\exp(-j \varphi_{M})}\cdot e^{jwt}
\end{align}}
$$
$$
\begin{align}
s(M,t) &= \mathrm{Re}(\underline{s}(M,t))  \\
&=a(M)\cos(\omega t- \varphi(M))
\end{align}
$$
Donc, on a :
$$
a(M)=|\underline{A}(M)|,\; \varphi_{M}= -\text{arg }\underline{A}(M)
$$

```ad-note
title: Éclairement d'une Onde Monochromatique
$$
\boxed{\begin{align}
I &= 2<s^2(M,t)> \\ &= a^2(M) = |\underline{A}(M)|^2\\ 
&= |\underline{s}(M,t)|^2=\underline{s}(M,t) \times \underline{s}^*(M,t)
\end{align}}
$$
- Démonstrations :
	- $<s^2(M,t)> = <a^2(M).\cos^2(\omega t- \varphi_{M})>$ avec $<\cos^2> =\frac{1}{2}$.
	- On a aussi $|\underline{A}(M)|^2 = a^2(M)|e^{-j\omega t}|^2=a^2(M)$.
	- $|\underline{s}(M,t)|^2=|\underline{A}(M)|^2|e^{j\omega t}|^2=a^2(M)$
	- $\underline{s}(M,t) \times \underline{s}^*(M,t)=a(M).e^{j(\omega t-\varphi_{M})}.a(M).e^{-j(\omega t - \varphi_{M})}=a^2(M)$

```
