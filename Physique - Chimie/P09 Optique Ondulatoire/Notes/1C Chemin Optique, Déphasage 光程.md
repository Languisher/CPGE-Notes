## Définition

```ad-note
title: Chemin Optique
![[Drawing 2023-02-14 09.19.12.excalidraw]]
- Définition : le **chemin optique** entre 𝑆 à 𝑀, noté 𝑆𝑀 , est égale à la <u>distance</u> que parcourrait la lumière dans le vide (à la célérité $c$), pendant la durée $𝜏_{𝑆𝑀}$ nécessaire au parcours 𝑆𝑀 dans le milieu considéré d’indice de réfraction $n$. (Cas d’un milieu homogène : (unité : mètre($m$)) 
$$
\boxed{(SM) = c\times \tau_{SM} = n \times SM}
$$
- Le chemin optique le long d’un rayon lumineux est égal à *la longueur du rayon multipliée par l’indice* du milieu transparent qu’il traverse. (在均勻介質中，光程可認為是在相等時間內光在真空中的路程))
```

- Cas où la lumière traverse plusieurs milieux homogènes :  ![[Assets/截屏2023-02-26 12.49.17.png]]$$\begin{align}
(MN) &= (MI)+(IJ)+(JN)  \\
&= n_{1} \times MI+n_{2}\times IJ+n_{3}\times JN
\end{align}$$
- Cas général : $$(SM) = \int _{S\to M} n(P) \, \mathrm{d}l $$

## Déphasage d'une onde lumineuse
![[Assets/Drawing 2023-02-14 09.19.12.excalidraw]]
```ad-note 
title: Retard de phase en $M$
$$\boxed{\varphi(M)-\varphi(S) = \frac{2\pi}{\lambda_{0}}(SM)}$$
Si dans un milieu homogène, d'après [[1A Modèle scalaire de la lumière#Lumière monochromatique]] alors : $$\lambda = \frac{\lambda_{0}}{n},\;k=nk_{0}$$
```
Preuve : ![[Assets/Pasted image 20230226130101.png]]

- On dit deux points sont **en phase** si : $$\varphi(M) = \varphi(N)+ 2m\pi \implies\frac{2\pi}{\lambda_{0}}(NM) = m.2\pi \implies (NM) = m\lambda_{0}$$
- De même façon, on dit deux points sont **en opposition de phase** si : $$\frac{2\pi}{\lambda_{0}}(NM)=m.2\pi+\pi \implies(NM)= \left( m+\frac{1}{2} \right)\lambda_{0}$$
### Géneralisation 
Pour les points A et B appartenant au même rayon, on a $$\varphi_{AB}= \frac{2\pi}{\lambda_{0}}+ \varphi_{\text{sup}}$$
- $\varphi_{\mathrm{sup}}= + \pi$ si :
	- *réflexion* sur un milieu plus réfringent ($𝑛_1$ < $𝑛_2$)
	- *réflexion* sur une surface métallique
	- passage par un point de convergence

- $\varphi_{\mathrm{sup}}= + \frac{1}{2}\pi$ si :
	- passage au travers d’un trou diffractant

## Stigmatisme et chemin optique
- Le chemin optique qui *relie deux points conjugués* est indépendant du rayon considéré. Les quatre chemins optiques sont identiques : ![[Assets/截屏2023-02-16 10.41.05.png]]
- Exemple : déterminer le chemin optique en fonction de $A A'$, l'épaisseur$e$ et de $n$ : ![[Drawing 2023-02-16 10.42.48.excalidraw]] $$(A A')=(AB)+(B B')+(B ' A')= n_{\text{air}}[A A ' - e]+ n_{v}e$$
