## Specetre de sources
- Cas idéal : Onde monochromatique
- Cas réal : Superposition

### Paramètres descriptifs d'une source monochromatique
- Sources à spectre discret vs Sources réelles à spectre continu

- On définit $B_{\omega}(\omega)$ ou $B_{\lambda}(\lambda)$ s'exprimant en Joules la **densité spectre de puissance** de la source telle que *la puissance émise par la source dans un intervalle de pulsation élémentaire ou en longueur d'onde élémentaire*$$\mathrm{d}\mathcal{P}= B_{\omega}(\omega)\mathrm{d}\omega \text{ ou } \mathrm{d}\mathcal{P}= B_{\lambda}(\lambda)\mathrm{d}\lambda$$
- On a donc les densité spectres en fréquence : $$\omega = 2\pi f \implies \mathrm{d}\omega = 2\pi \mathrm{d}f \implies B_{f}(f) = B_{\omega}(\omega) \frac{\mathrm{d}\omega}{\mathrm{d}f}=2\pi B_{\omega}(\omega)$$De même façon, avec $\sigma = 1 / \lambda$ le nombre d'onde, $$B_{\sigma}(\sigma) = 2\pi cB_{\omega}(\omega),\; B_{k}(k) = cB_{\omega}(\omega)$$
## Largeur Spectrale
$$
\left[ \frac{2}{3} \right]
$$
- On appelle $\Delta \omega$ la **largeur spectrale** du spectre à mi-hauteur ![[Assets/截屏2023-03-23 11.19.16.png]]
- L'intervalle d'émission en pulsation correspondà un intervalle en longueur d'onde : $$\omega\in\left[ \omega_{0}-\frac{\Delta\omega}{2}, \omega_{0}+ \frac{\Delta\omega}{2} \right] \iff \lambda\in\left[ \frac{2\pi c}{\omega_{0}+\Delta\omega /2}, \frac{2\pi c}{\omega_{0}- \Delta \omega / 2} \right]$$Dans ce cas, si $\Delta \omega \ll \omega_{0}$, $$\frac{\Delta \lambda}{\lambda_{0}} \approx \frac{\Delta \omega}{\omega_{0}}$$De même façon, en même temps, $$\frac{\Delta f}{f_{0}}=\frac{\Delta k}{k_{0}}= \frac{\Delta \sigma}{\sigma_{0}}= \frac{\Delta\omega}{\omega_{0}}$$
## Interférences à deux ondes en lumière non monochromatique
### Source à spectre discret
- Pour une source monochromatique, on a simplement : $$I(\delta) = 2I_{0}\left( 1+ \cos\left( \frac{\omega}{c}  \delta \right) \right)$$
- Double spectre : (Rappelons : Sources non cohérentes $\implies$ les éclairements s'additionnent) $$\begin{align}
I(\delta) &= \underbrace{I_{\omega_{1}}(\delta) }_{2I_{0}(1+ \cos(\omega_{1}\delta / c))}+ \underbrace{I_{\omega_{2}}(\delta) }_{2I_{0}(1+ \cos(\omega_{2}\delta / c)}\\
&=4 I_{0}\left( 1+ \cos\left( \underbrace{\frac{\omega_{1}+\omega_{2}}{2c}}_{\text{pulsation milieu }\omega_{m}}\delta  \right) \cos\left( \underbrace{ {\omega_{2}-\omega_{1}}}_{\text{largeur spectrale } \Delta \omega } \frac{\delta}{2c}\right)\right) \\
&=4I_{0}\left( 1+ \cos\left( \frac{\omega_{m}}{c}\delta \right) \cos(\frac{\Delta\omega}{2c}\delta)\right)
\end{align}$$
- Comme $\omega_{m}/c$ varie très vite avec $\delta$, l'éclairement est donc compris entre les deux courbes enveloppes : $$I_{+}= 4I_{0}\left( 1+ \cos\left( \frac{\Delta\omega}{2c}\delta \right) \right) \text{ et } I_{-}= 4I_{0}\left( 1-\cos\left( \frac{\Delta \omega}{2c}\delta \right) \right)$$Il s'agit d'un cas particulier du phénomène de **battement** : ![[Assets/截屏2023-03-23 11.36.32.png]]
- On peut déterminer graphiquement le rapport $\Delta \omega / \omega_{m}$ de la figure ![[Assets/截屏2023-03-23 11.39.16.png]]