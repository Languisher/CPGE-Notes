> Date: 2023-02-21 Matériaux : [[Assets/Chapitre2.pdf]]

## Terme d'Intérference, Ondes (In)Cohérentes
- Les ondes parfaitement **monochromatiques** 单色的，单频的
- **Éclairement** des deux ondes : Soient $s_{1}(M,t)$ et $s_{2}(M, t)$, Donc la résultat : $$\begin{align}
I(M) &= 2 <s^2(M,t)>  \\
&= 2<(s_{1}(M,t) +s_{2}(M, t))^2> \\
&=2<s_{1}^2(M,t)>+2<s_{2}^2(M,t)>+4<s_{1}(M,t)\cdot s_{2}(M,t)> \\
&= I_{1}(M)+I_{2}(M) + \underbrace{4<s_{1}(M,t) \cdot s_{2}(M,t)>}_{\text{terme d'interferences}}
\end{align}$$
- l’éclairement résultant est *différent* de la somme des éclairements *de chacune des ondes* : c’est le phénomène d’**interférences**. 

```ad-note
title: Terme d'Intérference, Ondes (In)Cohérentes
- Le terme supplémentaire $4<s_{1}(M,t)s_{2}(M,t)>$ dite : la **terme d'intérference**
- Deux **ondes incohérentes** 不相关波, si $$\forall M,\;<s_{1}(M,t)s_{2}(M,t)> =0$$En ce cas, $I = I_{1}+I_{2}$
- Deux ondes monochromatiques de *pulsations différentes* n’**interfèrent** pas.
- Si $\omega_{1}=\omega_{2}$, on dite les deux ondes **cohérentes** 相关性, on a : $$<s_{1}(M,t) \cdot s_{2}(M,t)> = \frac{\sqrt{ I_{1} }\sqrt{ I_{2} }}{2} \cos ( \Delta \varphi_{ 2 / 1}(M))$$
```

- Démonstration de deux *pulsations différentes* : ![[Assets/Pasted image 20230221081719.png]]
## La Formule de Fresnel
```ad-note
title: La Formule de Fresnel
- Lorsque $\omega_{1}=\omega_{2}$, on dite les deux ondes **cohérentes** 相关性, on a : $$<s_{1}(M,t) \cdot s_{2}(M,t)> = \frac{\sqrt{ I_{1} }\sqrt{ I_{2} }}{2} \cos ( \Delta \varphi_{ 2 / 1}(M))$$
- On peut en déduire **la formule de Fresnel** : $$\boxed{I = I_{1}+I_{2}+2 \sqrt{ I_{1} }\sqrt{ I_{2} }\cos( \Delta \varphi_{2 / 1}(M))}$$
- Cas particulier où les deux ondes ont *même éclairement* $I_{1}=I_{2}=I_{0}$, **la formule de Fresnel (simplifiée)** s'écrit : $$I = 2I_{0}(1+ \cos (\Delta \varphi _{2 / 1}(M)))$$![[截屏2023-03-01 23.20.19.png]]
- La valeur moyenne $I_{\text{moy}}$ est $I_{1}+I_{2}$, 
- $I$ maximal si $\cos\Delta \varphi(M) =1$, c'est-à-dire $\Delta \varphi = 2m \pi$
- $I$ minimal si $\cos\Delta \varphi(M)=-1$, c'est-à-dire $\Delta \varphi = (2m+1)\pi$
```
- Démonstration : ![[Assets/Pasted image 20230221082550.png]]
```ad-note
title: Interférences Constructives et Destructives
- **Interférences constructives** 相长干涉：L'*éclairement* est *maximal*. $$I_{\text{max}}=I_{1}+I_{2}+2 \sqrt{ I_{1} }\sqrt{ I_2 } = (\sqrt{ I_{1} }+\sqrt{ I_{2} })^2$$ Lorsque $\cos(\Delta \varphi_{ 2 / 1}(M))=+1$ et $\Delta \varphi_{2 / 1}(M) = m \times 2 \pi$
- **Interférences destructives** 相消干涉: L’éclairement est minimal $$I_{\text{max}}=I_{1}+I_{2}-2 \sqrt{ I_{1} }\sqrt{ I_2 } = (\sqrt{ I_{1} }-\sqrt{ I_{2} })^2$$ Lorsque $\cos(\Delta\varphi_{2 / 1} (M)) =-1$ et $\Delta\varphi_{2 / 1}(M) = (m+ 1 / 2)\times 2\pi$

```

## Différence de marche et ordre d'interférences
```ad-note
title: Différence de marche
La différence des chemins optiques $(S_2M)−(S_1M)$ est appelée différence de marche au point $M$. On la note $δ(M)$ :
$$δ(M) = (S_2M)−(S_1M)$$
```
```ad-note
title: Ordre d'Interférence
- **Ordre d' interférence** 干涉级次: (D'après [[1C Chemin Optique 光程#Déphasage d'une onde lumineuse]]) : $$p_{2 / 1}(M) = \frac{\Delta\varphi_{ 2 / 1}(M)}{2\pi} = \frac{\delta(M)}{\lambda_{0}}$$ Ici, $p$ *entier* si c'est interférences *constructives*; *demi-entier* si c'est *destructives*.
```
- Interprétation en terme d'amplitudes complexes : ![[Assets/截屏2023-02-21 08.40.25.png]]
## Franges d'interférences, Franges brillantes, Franges sombres
![[Assets/Drawing 2023-02-21 08.59.38.excalidraw]]
$$
\begin{align}
\varphi_{1}(M) &= \varphi _{1}(S_{1})+k_{0}(S_{1}M)  \\
\varphi_{2}(M) &= \varphi_{1}(S_{2})+k_{0}(S_{2}M)
\end{align}
$$
- pour des **ondes synchrones** $\varphi_{1}(S_{1}) = \varphi_{2}(S_{2})$, donc $$\Delta \varphi_{2 / 1}(M) = k_{0}[(S_{2}M)-(S_{1}M)] \text{ avec } k_{0}=\frac{2\pi}{\lambda_{0}}$$
```ad-note
title: Franges d'interférences, Franges Brillantes, Franges Sombres
- Le lieu des points pour lesquels $Δ𝜑 _{2/1}(𝑀)$ est uniforme et $p(M)=\text{constante}$ est appelé **franges d’interférences** 干涉条纹 (courbe sur un écran)
- Il s'agit de surfaces sur lesquelles on a : $$S_{2}M-S_{1}M = \text{constante}$$
- **Franges brillantes** 亮条纹 sont les franges où l’éclairement est *maximal* : $$p(M)=m\implies S_{2}M-S_{1}M = m\lambda$$,
- De même façon, les **franges sombres** 暗条纹: $$p(M) = m + \frac{1}{2}\implies S_{2}M-S_{1}M = (m+1 / 2) \lambda$$.

```

- Géométriquement, **hyperboloïde** de révolution : ![[Assets/截屏2023-02-23 10.07.32.png]]
## Contraste du phénomène d'interférence
```ad-note
title: Contraste, Visibilité
On définit le **contraste** 可见度 ou **visibilité** d'une figure d'interférences par (d'après [[#La Formule de Fresnel]])
$$\boxed{\gamma = \frac{I_{\text{max}}-I_{\text{min}}}{I_{\text{max}}+I_{\text{min}}}= \frac{2\sqrt{ I_{1}I_{2} }}{I_{1}+I_{2}} \in \;]0, 1[}$$
![[截屏2023-03-01 23.48.31.png]]
```
- Démonstration : ![[Assets/Pasted image 20230221084727.png]]
- Le phéonomène d'interférences est observable si les deux signaux sont d'intensités comparables ![[Assets/截屏2023-02-21 08.58.46.png]]Visible à l’œil si $\gamma>0.1$


### Systèmes optiques stigamatiques et interférences

N'importe quel système stigmatique n'introduit aucune modification dans l'état d'interférences
- ![[Assets/截屏2023-02-23 10.11.37.png]]
- Les points $M$ et $M'$ est dite **conjugés** pour la lentille s'il verifie la relation de conjugaison : $$\frac{1}{\overline{OM'}}- \frac{1}{\overline{OM}} = \frac{1}{f'}$$
- On peut prouver $$\Delta\varphi_{ 2 / 1}(M')= \Delta{\varphi_{2 / 1}}(M)$$
- Application : oberservation dans le plan focal image d'une lentille convergente : ![[Assets/截屏2023-02-21 09.26.04.png]] $$\delta = S_{2}M_{\infty}-S_{1}M_{\infty} = a \times \sin i$$