> Date : 2023-03-01 Matériaux : [[Assets/Thermochimie_Cours_CH1_Partie3.pdf]]

## Deux Réaction successives d'ordre 1
![[Assets/Drawing 2023-03-01 08.13.58.excalidraw]]
avec $v_{1}=k_{1}[A], \; v_{2}=k_{2}[B]$
Alors, les trois équations : $$\begin{align}
[A] &=[A]_{0}\cdot e^{-k_{1}t } \to 0 \\
[B] &= [A]_{0}\cdot\frac{k_{1}}{k_{2}-k_{1}}\cdot(e^{-k_{1}t }-e^{-k_{2} t})\to 0 \\
[C] &= [A]_{0} \cdot \left[ 1 - \frac{k_{2}}{k_{2}-k_{1}}e^{-k_{1}t }+ \frac{k_{1}}{k_{2}-k_{1}}e^{-k_{2}t} \right] \to [A]_{0}
\end{align}$$![[Assets/截屏2023-03-01 08.36.30.png]]
Lorsque $\tau _1 = 1 / k_{1} \gg 1 / k_{2}= \tau_{2}$, $$\begin{align}
[B](t) &\approx  \frac{k_{1}}{k_{2}}[A]_{0}e^{-k_{1}t}\ll[A](t) \text{ et } [C](t)\\
[C](t) &\approx [A]_{0}(1- e^{-k_{1}t})
\end{align}$$$[C](t)$ ne dépend que de $k_{1}$. 
- la réaction limite la vitesse globale et est donc dite « **cinétiquement déterminante** ».
- La concentration de B reste négligeable devant celles de A et B. Elle peut alors être considérée comme quasiment constante : elle est dite **quasi-stationnaire**.
Démonstration : ![[Assets/Pasted image 20230301083609.png]]
## Réaction équilibre
$$
A=B \iff A \underbrace{\to}_{k^+}B \text{ et } B \underbrace{\to}_{k^-} A
$$
à L'état final, $$\frac{[B]_{\infty}}{[A]_{\infty}}= \frac{k_{+}}{k_{-}}$$
## Réaction parallèles
$$
A \underbrace{\to}_{k_{1}}B \text{ et } A \underbrace{\to}_{k_{2}}C
$$
On peut établir en tout instant, $$\frac{[B](t)}{[C](t)}= \frac{k_{1}}{k_{2}}$$

