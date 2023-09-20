
## Ondes Sphériques
```ad-note
title: Onde Sphérique

- **Ondes sphérique 球面波**, plaçons la sourse à l'origine $O$. ![[Drawing 2023-02-16 11.03.21.excalidraw]]
- Une onde sphérique est une onde ayant l’une des caractéristiques suivantes :
	- les rayons lumineux sont des droites concourantes en un point $S$,
	- les surfaces d’onde sont des sphères centrées sur $S$.
```

-  On a : $$\varphi(M)-\varphi(O)=k_{0}(OM)=k\times OM$$ et donc $$\underline{s}(M,t) =a(M) \exp (j( \omega t-k\times OM-\varphi(O)))$$
- Phase de l'OSPM (Onde Sphérique Progressive Monochromatique) :
	- Onde divergente $\varphi(M)-\varphi(O) = k_{0}\times(OM)$
	- Onde convergente $\varphi(O)-\varphi(M) = k_{0}\times(MO)$
	- On pose $\vec{k}= +k \vec{e_{r}}$ en cas divergente, et $\vec{k}=-k \vec{e_{r}}$ convergente, donc : $$\varphi(M)-\varphi(O)=\vec{k}.\vec{OM}$$
- **Amplitude** d'une OSPM : dans un milieu *non absorbant* : $$\begin{align}
&\mathscr P (r) =\mathscr  P(O) \implies a(r) = \frac{\alpha}{r}
\end{align}$$
```ad-note
title: Expression d'une OSPM
- Cela implique la expression d'une OSPM dans un milieu homogène : $$s(M,t) = \frac{\alpha}{r}\exp(j(\omega t-\vec{k}.\vec{r})$$
```
- À grand distance, l'OSPM peut être assimilée à une onde plane

## Ondes Planes
```ad-note
title: Onde Plane
- Une onde plane est une onde ayant l’une des caractéristiques suivantes :
	• les rayons lumineux sont des droites parallèles entre elles,
	• les surfaces d’onde sont des plans parallèles entre eux appelés p
- **Onde plane 平面波** de direction $\vec{u}$ : les surfaces d'onde sont des plans perpendiculaires à $\vec{u}$ ![[截屏2023-02-26 16.28.44.png]]
```

- Exemple : ![[Assets/截屏2023-02-16 11.14.04.png]] $$\begin{align}
\varphi(M)-\varphi(P) &= \varphi(M) - \varphi(H)  \\
&=k \times HM  \\
&= k \times \vec{HM} \times \vec{u}  \\
&= k \times(\vec{PM}- \vec{PH}) \times \vec{u}  \\
&=k \vec{u} . \vec{PM}
\end{align}$$
- Expression d'une OPPM (Onde Plane Progressive Monochromatique) dans un milieu homogène (si origine des phases en $O$): $$\underline{s}(M,t) = a(M) \exp(j( \omega t-\vec{k}.\vec{OM}))$$