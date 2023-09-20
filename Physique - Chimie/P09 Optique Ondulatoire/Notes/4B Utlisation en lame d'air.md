```ad-note
title: L'interféromètre est configué en lame d'air, localisation à l'infini, position des deux sources secondaires
- On dit que l’interféromètre est configuré en **lame d’air** lorsque les deux miroirs (M1) et (M2) sont perpendiculaires aux axes (Ox) et (Oy) respectivement.
- Pour l’interféromètre de Michelson, réglé en lame d’air, et éclairé par une source spatialement étendue, les franges d’interférences sont *localisées à l’infini*. Montage équivalent : Les interférences sont localisées à l'infini ![[截屏2023-03-14 08.59.26.png]]
- Schéma du dispostif : Position des deux sources secondaires ![[截屏2023-03-20 22.16.51.png]]On appelle **épaisseur de la lame d’air** la distance entre ($M_{2}$) et ($M_{1}'$). On la note e. On peut alors montrer que la distance entre S1 et S2 est : $$\boxed{S_{1}S_{2} = 2e}$$
```

```ad-note
title: Marche des rayons lumineux jusqu’au point d’observation, Différence de marche, Différence de phase, ordre d'interférences
![[截屏2023-03-20 22.24.57.png]]
- **Différence de mache** : $$\begin{align}
\delta(M) = nS_{1}H = 2ne\cos i
\end{align}$$
- **Différence de phase** : $$\Delta \varphi = \frac{2\pi}{\lambda_{0}}2ne\cos i = \frac{4\pi ne\cos i}{\lambda_{0}}$$
- **Ordre d'interférences** : $$p(M) = \frac{\Delta \varphi}{2\pi}= \frac{2ne\cos i}{\lambda_{0}}$$
- **Intensité vibratoire** : $$I(M) = \frac{I_{0}}{2}\left( 1+ \cos\left( \frac{4\pi ne\cos i}{\lambda_{0}} \right) \right)$$
- Since the order of interference at M depends only on the position of point M, all these systems of interference fringes coincide exactly, *regardless of the spatial extension of the primary source*.
- La surface de localisation est constituée de l’ensemble des points M qui correspondent à l’intersection des deux rayons émergents de l’interféromètre qui sont issus d’un seul et même rayon émergent de la source. En ces points, le dispositif interférentiel fonctionne par **division d’amplitude**.
```

## Figure d'interférences : Anneaux de Haidinger
### Franges d'égale inclinaison
```ad-note
title: Anneaux de Haidinger
Le **rayon $\rho_{m}$ de la frange brillante d’ordre** $m$ : Pour un point $M$ donné, situé à la distance $\rho$ de l'axe est atteint par des rayons d'incidence $i$ telle que $$i \approx \tan i= \frac{\rho}{f'}$$![[截屏2023-03-14 09.23.13.png]]On peut en déduire que $$\boxed{\begin{align}
\delta_{1 / 2}(M) &= 2e\cos i \\
&\approx 2e \left( 1 - \frac{1}{2}\left( \frac{\rho}{f'} \right)^2 \right)
\end{align}}$$
Sachant que la frange brillante d'ordre $m$ a donc un rayon $\rho_{m}$ tel que $m\lambda_{0}=\delta_{1 / 2}(M)$, $$\boxed{\rho_{m}= f' \sqrt{ 2 }\sqrt{ 1- \frac{m\lambda_{0}}{2e} }}$$On peut numéroter les franges à partir du centre, le centre $p_{0}$, et le second $p_{0}-1$, ...
La figure d'interférences ou les **anneaux de Haidinger** : ![[截屏2023-03-14 09.36.47.png]]
- Lorsqu’on *diminue l’épaisseur* $e$ de la lame d’air, un anneau donné *rétrécit et finit par disparaître* au centre de la figure d’interférences. ![[截屏2023-03-20 23.09.14.png]]
L'**Éclairement sur l'écran**, d'après la formule de Fresnel, on a : $$I= 2I_{0}\left( 1+ \cos\left( k_{0}2e\left( 1-\frac{\rho^2}{2f'^2} \right) \right) \right)$$
```

## Elargissement de la source et localisation
- Les ondes émises par les différents points de la source sont *incohérentes* entre elles, les éclairements s’ajoutent. Mais, les figures d’interférences associées à chaque point P de la source sont exactement confondus. Cela implique que : On peut élargir la source sans perdre de contraste. ![[Assets/截屏2023-03-20 23.06.25.png]]
