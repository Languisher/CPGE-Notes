## Montage de Fraunhofer
- Cas : Observation à l’infini

![[截屏2023-02-28 08.18.26.png]]
- **Différence de marche** : lentille convergente placée après les trous ($f'$ est la distance focal image de la lentille $\mathscr{L}_{2}$) $$\boxed{\delta(M)=(S_{2}M)-(S_{1}M)=n\times S_{2}H = na\sin\alpha\approx n \frac{ax}{f'}}$$Ici, $x=MF_{2}'$
- L’**interfrange** : $$i = \frac{\lambda_{0}f'}{a}$$Démonstration : ![[Pasted image 20230228083254.png]]
## Déplacement de la source
En ce cas, la distance entre la source et les trous n'est plus la même.
![[截屏2023-02-28 08.35.08.png]]
- **Différence de marche** : $$\delta(M)=[(ST_{2})-(ST_{1})]+[(T_{2}M)-(T_{1}M)] = \frac{aX}{D'}+ \frac{ax}{D}$$
- Déplacement des franges vers le bas : $$x_{0}=-X \frac{D}{D'}$$
- L'interfrange : $$i= \frac{\lambda_{0}D}{a}$$
## Fente incohérente éclairée
On remplace la source principale par *une fente* de dimension $H$ selon $Oy$ et de largeur $L$ selon $Ox$, éclairée de façon incohérente par une source extérieure : ![[截屏2023-03-02 00.45.31.png]]
- Sources cohérentes -> On ajoute leurs amplitude, $\underline{A}(M) = \sum A_{i}(M)$
- Sources incohérentes -> On additionne leurs intensifs. $I(M) = \sum I_{i}(M)$
- On note l'éclairement donné par un élément de source $$\mathrm{d}I_{0}= K\mathrm{d}x\mathrm{d}y$$
- Sur l'écran, en $M$, on a $$\mathrm{d}I = 2\mathrm{d}I_{0}\left[ 1+ \cos \left( k_{0}\left( \frac{aX}{D'}+\frac{ax}{D} \right) \right) \right]$$
- Donc : $$\begin{align}
I = \iint \mathrm{d}I&=2I_{0}\left[ 1+\text{sinc}\left( \frac{k_{0}aL}{2D'}  \right)  \cos\left( \frac{k_{0}aX}{D} \right)\right] \\
&=2I_{0}\left[ 1+\text{sinc}\left( \frac{\pi L}{L_{b}} \right) \cos\left( k_{0} \frac{aX}{D} \right) \right]
\end{align}$$Démonstration : ![[Pasted image 20230228092151.png]]
- On note $L_{b}$ et le **facteur de visibilité** $\nu$ : $$L_{b}= \frac{\lambda_{0}D'}{a},\quad v = \text{sinc}\left( \frac{\pi L}{L_{b}} \right)$$
- Cas $\nu = \text{sinc}(\pi L / L_{b})>0$, $I_{\mathrm{\max{}}}=2I_{0}(1+ \nu)$, $$x = \frac{m\lambda_{0}D }{a}$$
- Cas $\nu<0,\; I_{\mathrm{\min{}}}=2I_{0}(1- \nu)$, $$x = \frac{\left( m+ \frac{1}{2} \right)\lambda_{0} D }{a}$$
- Inversion de **contraste** : $$\gamma = \frac{I_{\mathrm{\max{}}}-I_{\min{}}}{I_{\mathrm{\max{}}}+I_{\min{}}}=|\text{sinc}\left( \frac{\pi L}{L_{b}} \right)| ,\; 0 \leq \gamma \leq 1$$
	- Le **constraste** est indépendant de la dimension selon $Oy$ ($H$)
