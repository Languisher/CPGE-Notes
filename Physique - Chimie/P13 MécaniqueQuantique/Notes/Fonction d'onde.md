## Définitions

### Densité 
Amplitude de probabilité : $\psi(M,t)$
**Densité de probabilité de présence** au point $M$ à l'instant $t$ :
$$
\boxed{\rho(M,t) = |\psi(M,t)|^{2} = \psi^{*}(M,t) \psi(M,t)}
$$
#### Dimension de la fonction d'onde
$\mathrm{dim} (\rho) = \mathrm{L} ^{-3}$, donc 
- Dimension 3D : $\mathrm{dim} (\psi) = \mathrm{L} ^{-3 / 2}$. 
- Dans le cas unidimensionnel, $\mathrm{dim}(\psi) = \mathrm{L} ^{-1}$
#### Probabilité de trouver la particule dans un volume élémentaire
Probabilité de trouver la particule dans $\mathrm{d} V_M$ à $t$ : $$ \mathrm{d} P_{M,t, \mathrm{d} V_m}  = \rho(M,t) \times \mathrm{d} V_M $$
Probabilité de trouver la particule dans $V$ : $$ P_{t,V} = \iiint_V \rho(M,t) \mathrm{d} V_M  = \iiint_V |\psi(M,t)|^2 \mathrm{d}V_M = \iiint_V \psi ^* (M,t) \psi(M,t) \mathrm{d} V_M $$
Cas unidimensionnel
$$
\mathrm{d}P_{x,t, \mathrm{d}x} = \rho(x, t) \times \mathrm{d}x, \; P _{t,L} = \int _ L \rho(x,t) \mathrm{d}x = \int_L |\psi(x,t)|^2 \mathrm{d}x
$$
### Condition de normalisation
On peut toujours trouver l'électron qu'on cherche dans tout l'espace, donc :
$$
\boxed{\iiint_{\text{tout l'espace}} \rho(M,t)\mathrm{d} V_M = \iiint_{\text{tout l'espace}} |\psi(M,t)|^{2}\mathrm{d} V_M = \iiint_{\text{tout l'espace}} \psi ^* (M,t) \psi(M,t)\mathrm{d} V_M = 1}
$$
Cas unidimensionel :
$$
        \int_{-\infty}^{+\infty} |\psi(M,t)|^{2}\mathrm{d} x = 1
$$
### Notation de Dirac
#### Produit scalaire et Norme
*Produit scalaire de fonction d'onde* : Produit scalaire (hermitien) s'écrit sous la **notation de Dirac** : 
$$
\langle \psi_1 | \psi_2 \rangle = \int _{- \infty} ^{+ \infty} \psi_1^{*}(M,t) \psi_2(M,t) \mathrm{d} V_M
$$

*Norme d'une fonction d'onde* : 
$$
\Vert \psi  \Vert ^{2}  = \langle \psi | \psi \rangle
$$

#### Propriétés
$$
\begin{gather}
\langle \psi_1 | \psi_2 \rangle = \langle \psi_2 | \psi_1 \rangle ^{*}  \\
\langle \psi_1 | \lambda \psi_2 \rangle = \lambda \langle \psi_1 | \psi_2 \rangle \\
\langle \lambda \psi_1 | \psi_2 \rangle = \lambda^{*} \langle \psi_1 | \psi_2 \rangle \\
\langle \psi_1 | \psi_2 + \psi_3 \rangle = \langle \psi_1 | \psi_2 \rangle + \langle \psi_1 | \psi_3 \rangle
\end{gather}
$$

#### Orthogonalité
$\psi_1$ et $\psi_2$ sont **orthogonaux** si $$\langle \psi_1 | \psi_2 \rangle =0$$
- Si $\psi$ est normalisé, écrire la relation vérifiée de $\alpha_1$ et $\alpha_2$, la condition de normalisation de $\psi = \alpha _1\psi_1 + \alpha _2 \psi_2$ su $\psi_1$ et $\psi_2$ sont normalisées et orthogonaux : 
	$$
	\begin{align*}
	    \langle \psi | \psi \rangle = 1 &\implies \int( \alpha _1\psi_1 + \alpha _2\psi_2)^{*}( \alpha _1 \psi_1 + \alpha _2\psi_2 )\mathrm{d} V \\ 
	                                    &\implies |\alpha_1|^2 \int \psi_1 ^* \psi_1 + \alpha_1 ^* \alpha_2 \int \psi_1 ^* \psi_2 + \alpha_2 ^* \alpha_1 \int \psi_2 ^* \psi_1 + | \alpha_2| ^2 \int \psi_2 ^* \psi_2 = 1 \\
	                                    &\implies |\alpha_1|^2 \langle \psi_1 | \psi_1 \rangle + \alpha_1 ^* \alpha_2 \langle \psi_1 ^* \psi_2 \rangle + \alpha_2 ^* \alpha_1 \langle \psi_2 | \psi_1 \rangle + | \alpha_2 | ^2 \langle \psi_2 | \psi_1 \rangle = 1 \\
	                                    &\implies |\alpha_1|^2 + |\alpha_2| ^2 = 1
	\end{align*}
	$$
 
### Position moyenne
**Position moyenne** :
- 1D : 
		$$
		\langle x \rangle = \int_{-\infty}^{+\infty} x \rho(x,t) \mathrm{d}x = \displaystyle\int_{-\infty}^{+\infty} \varphi ^{*} (x,t) x \varphi(x, t) \mathrm{d}x
	$$
- 3D : 
	$$
	\langle \overrightarrow{OM} \rangle = \iiint _{\text{Tout l'espace}} \psi ^* (M,t)\; \overrightarrow{OM} \;\psi(M,t) \mathrm{d}V _M
	$$
- De distribution $f(M,t)$ :
	$$
  \langle f(M,t) \rangle = \iiint \psi ^*(M,t) f(M,t) \psi(M,t) \mathrm{d}V
	$$
### Largeur de distribution
**Largeur de distribution**, notée $\Delta x$ est définie par :
$$
  \Delta x = \sqrt{ \langle x ^2 \rangle - \langle x \rangle ^2}
$$
De distribution $f(M,t)$ : 
$$
\Delta f = \sqrt{ \langle f ^2(M,t) \rangle - \langle f(M,t) \rangle ^2}
$$



## Utilisation

### Distribution Gaussienne

Distribution de Gauss 1D : 
$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp (-\frac{(x-\mu)^2}{2 \sigma ^2})
$$

vérifiant $\langle x \rangle = \mu$, $\langle x ^2 \rangle = \sigma ^2 + \mu ^2$, $\Delta x = \sigma$

Fonction d'onde sous forme Gaussienne : Comme $|\psi_L(x)|^2$ est une distribution de Gauss 1D, on remplace $\sigma$ par $L$ et $\mu$ par $x_0$,

$$
\psi_L(x) = \frac{1}{(2 \pi L ^2)^{\color{red}{1 / 4}}} \exp( - \frac{(x-x_0) ^2}{{\color{red}{4}} L ^2})
$$
vérifiant $\langle x \rangle = x_0$ et $\Delta x = L$

### Distribution de Dirac

À partir de l'exemple précédent, lorsque $L \to 0$, toutes les mesures de position donneront la même valeur $x_0$. Donc, 

**Distribution de Dirac** : 
$$
\delta(x-x_0) =  \underset{L \to 0}{\mathrm{lim}} \psi_L ^2(x)
$$

#### Propriétés
- Normalisé
- Échantillonnage : 
	$$
	\int _{- \infty}^{+ \infty}f(x) \delta(x-x_0) \mathrm{d}x = f(x_0)
	$$
- Relation importante :
	$$
	\boxed{\delta(x) = \frac{1}{2 \pi} \int _{- \infty}^{+ \infty}\exp{ikx} \mathrm{d}k}
	$$
	Utilisé pour décrire une distribution ponctuelle.

### Ondes de de Broglie
$$
\begin{align*}
f(x) &= \frac{1}{\sqrt{2 \pi \hbar}} \int_{- \infty} ^{+ \infty} g(p) e ^{ipx / \hbar} \mathrm{d}p \\
g(p) &= \frac{1}{\sqrt{2 \pi \hbar}} \int_{- \infty} ^{+ \infty} f(x)e ^{ipx / \hbar} \mathrm{d}x
\end{align*}
$$
