Introduction : On a deux formes linéaires $$\begin{cases}
\varphi_{1}:(x,y,z) \longmapsto 2x-3y+z \\
\varphi_{2}:(x,y,z) \longmapsto x+y-z
\end{cases}$$Donc la droite $D = \text{Ker}(\varphi_{1})\cap \text{Ker}(\varphi_{2})$ vérfie : $$\begin{cases}
2x-3y+z=0 \\
x+y-z=0
\end{cases}$$
## Hyperplan
```ad-note
title: Hyperplan
- $H$, un sous espace de $E$ est un **hyperplan** de $E$ s'il a l'un des propriétés (*équivalentes*) :
	- $H$ est le ==noyau d'une **forme linéaire** *non nulle*== : $$H = \mathrm{Ker}(\varphi), \; \varphi \in E^\star\backslash\{0_{E^\star}\}$$
	- Il existe une *droite* $D$ de $E$ telle que : $$E = H \oplus D$$
	- Pour tout *élément* $e$ de $E$ et $e \not\in H$ telle que : $$E = H \oplus \mathbb{K}.e$$
- Les **hyperplans** sont exactement le *noyaux* d'(au moins) une **forme linéaire** *non nulles*.
- Il admet souvent une forme comme : $$\lambda_{1}x_{1}+\dots+\lambda _{n}x_{n}=0$$
- Exemple : ![[截屏2023-03-04 20.02.10.png]]
- > Exemple : ![[截屏2023-03-12 10.14.44.png]] ![[截屏2023-03-12 10.15.17.png]]
- Proposition : Soit $\varphi$ et $\psi$ deux formes linéaires non nulles de $E$, ils sont *proportionnelles*. Alors, $$\mathrm{Ker}(\varphi)=\text{Ker}(\psi) \iff \exists \lambda \in \mathbb{K},\; \varphi = \lambda\psi$$Démonstration : ![[Pasted image 20230228133324.png]]
- Proposition : Il est en somme directe avec n'importe quelle droite non incluse dans $H$
```


## Hyperplans vectoriels et dimension finie

```ad-note
title: Codimension
Soit $E$ un $\mathbb{K}$-espace vectoriel, $F$ un sous-espace vectoriel de $E$, on dit que $F$ est de codimension finie, si $F$ possède un supplémentaire de dimension finie. La *dimension commune de tous les supplémentaires* de $F$ est appelée **codimension** de $F$ et notée (si $E = F \oplus G$).
- **Codimension** d'un sous-espace vectoriel $F$ : $$\text{codim } F = \text{dim }G \text{ où } E =F\oplus G$$
```

```ad-note
title: Dimension "-1" d'une hyperplan
- **Proposition** : Soit $E$ un espace vectoriel, $H$ sous-espace vectoriel de $E$, alors $$H \text{ hyperplan} \iff \text{codim }H = 1$$
- **Proposition** : Si $E$ est de dimension finie, donc les hyperplans de $E$ sont : $$\text{dim }H = \text{dim }E-1$$
	- Exemples : En dimension 2, les hyperplans sont les droites vectorielles ; En dimension 3, les hyperplans sont les plans vectoriels
- **Corollaire** : Une partie $H$ est un **hyperplan** ssi il existe une famille *non tous nuls* telle que $$\forall x\in E,\; (x\in H) \iff \sum_{i=1}^na_{i}x_{i}=0$$
	- Exemple : Un plan en dimension 3 : $ax+by+cz =0$ avec $(a,b,c) \ne 0$
```

## Faisceau d'hyperplans
```ad-note
title: Combinaison de plusieurs hyperplans
- **Théorème** : Mise en équation des sous-espaces de **codimensions** finies : Soit $E_1$ est un sous-espace vectoriel de $E$, on a : $$\text{codim }E_{1}= p \iff \exists(\varphi_{1},\dots,\varphi_{p})\in (E^{\star})^p,\; E_{1 } = \bigcap_{k=1}^p \text{Ker }\varphi_{k}$$(Toutes les $\varphi_{i}$ sont *indépendantes*), c'est-à-dire, pour $x\in E_{1}$, $$\begin{cases}
\varphi_{1}(x)=0 \\
\quad\quad\;\vdots \\
\varphi_{p}(x)=0
\end{cases}$$
```

```ad-note
title: Faisceau d'hyperplan
- **Théorème : Faisceau d'hyperplan**$$\forall \psi \in E^\star,\; \psi \in \mathrm{\text{Vect}}(\{\varphi_{1},\dots,\varphi_{n}\}) \iff \mathrm{Ker}(\psi)\supset\bigcap_{k=1}^n\mathrm{Ker}(\varphi_{k})$$
 - Cas $\text{dim }E = 3$, soit $H_{1}$ hyperplan passant par $A_{1}$ et $\text{Ker}(\varphi_{1})$, $H_{2}$ hyperplan passant par le point $A_{2}$ passant par $\text{Ker}(\varphi_{2})$, Ici $\varphi_{j}\in E^\star \backslash\{0_{E^\star}\}$
 - $H_{1}\cap H_{2}$
	 - $=H_1=H_2$ si les plans confondus
	 - $=\emptyset$ si plans parallèles
	 - de direction $\text{Ker}(\varphi_{1})\cap \text{Ker}(\varphi_{2})$, de dimension 1
 - Exemple : ![[Pasted image 20230304232536.png]]
```

## Affinité
Retour : [[01B Sous-espace Affines]]
```ad-note
title: Hyperplan Affine
Un **hyperplan affine** est le translaté d'un hyperplan vectoriel. 
- Il est de direction $\text{Ker}(\varphi)$ en même temps passant par un point $A \in \mathscr E$.
- Il admet une équation du type $$\lambda_{1}x_{1}+\dots+\lambda_{n}x_{n}=c$$
```

```ad-note
title: Sous-espace Affine
$A \subset \mathscr E$ est un **sous-espace affine** si :
- $A\ne \emptyset$, Soit $\Omega \in A$
- $\exists$ un sous-espace vectoriel $E_1$ tel que $$A = \Omega+E_{1}=\{\Omega+\vec{u},\; \vec{u}\in E_{1}\}$$C'est aussi la direction de la droite.
- Soit $(e_{i})_{i\in I}$ une base de $\mathscr E$, une origine $A \in \mathscr E$, on appelle **repère le donné** $(A;\;(e_{i})_{i\in I}))$
```
- Exemple : $(O;\;\vec{i},\vec{j},\vec{k})$ repère en physique

- Plus généralement : Un **sous-espace affine** est défini par le donné de:
	- un *point* $\Omega$
	- une direction $E_{1}$ où $E_{1}$ est un *sous-espace vectoriel* de $E$

```ad-note
title: Application Affine
Soit $\mathscr E$ et $\mathscr E'$ deux espace affine de direction respectivement $E$ et $E'$, donc $\phi$ est appelée une **application affine** de $\mathscr E$ dans $\mathscr E'$ s'il existe $\vec{\phi}\in \mathscr{L}(E, E')$ tel que $$\phi(B) = \phi(A+ \vec{AB}) = \phi(A)+ \vec{\phi}(\vec{AB}) $$
```
- Pour connaitre $\phi$, il faut : ![[截屏2023-03-04 23.41.17.png]]
- Proposition : Soit $\mathscr E$ un **espace affine** de direction $E$, $\mathscr H_{1},\dots,\mathscr H_{p}$ **hyperplan affine**,  on écrit : $$\mathscr H_{k}=A_{k}+ \text{Ker}(\varphi_{k})$$alors $$[\varphi_{1},\dots,\varphi_{p} \text{ indépendentes}] \implies [\bigcap_{k=1}^p\mathscr H_{k} \ne \emptyset]$$
> Preuve : Cas $p=2$, ensuite utiliser la récurrence. ![[Pasted image 20230227081523.png]]


### Faisceau d'hyperplans affine
Retour : [[#Faisceau d'hyperplans]]
- Exemple : ![[截屏2023-02-26 21.43.49.png]]Donc, en remplaçant $x$ par $x_{0}$ : $$(P) \quad\cos\theta(4x+y+z) + \sin\theta(2x+5y+3z+4) =0$$
## Références
### Cours
> Date : 2023-02-20 Matériaux : [[Lundi20fÃ©vrier-2.pdf]]
> Date : 2023-02-22 Matériaux : [[Mercredi22fevrier.pdf]]
> Date : 2023-02-27 Matériaux : [[Lundi27fÃ©vrier.pdf]]