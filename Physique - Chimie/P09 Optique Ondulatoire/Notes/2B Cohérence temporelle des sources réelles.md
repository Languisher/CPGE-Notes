
> Date : 2023-02-23 Matériaux : [[Assets/Chapitre2.pdf]]
### Modèle des trains d'onde
- Le signal s'écrit : $$s(S,t)=A\cos(\omega t-\varphi(S,t))$$Ici, $\varphi(S,t)$ est une phase *aléatoire* et *différente* pour chaque train d'onde émis ![[Assets/截屏2023-02-23 10.20.16.png]]
- (Rappel) **Cohérence** : On suppose que $\varphi(S,t)$ reste constante pendant des intervalles de temps.
- On suppose $\tau_{c}$ la **durée de cohérence** moyenne de la source.
```ad-note
title: Longueur de cohérence
- On appelle **longueur de cohérence** de la source $$l_{c}=c\tau_{c}$$
- Il s'agit de la distance parcourue par l'onde
```

```ad-note
title: Élargissement Spectral
- **Élargissement spectral** 拓宽 : d'après l'analyse de Fourier, $$\Delta\nu \approx \frac{1}{\tau_{c}}$$![[截屏2023-02-23 10.16.32.png]]
```

### Sources Distincte
- Entre deux sources $S_{1}$ et $S_{2}$ avec des trains d'onde décorrélés $$I = I_{1}+I_{2}+2 \sqrt{ I_{1}I_{2} }<\cos(\Delta \varphi_{2 / 1}(M,t))> \implies I=I_{1}+I_{2}$$ puisque $\Delta \varphi$ varie totalement aléatoirement du temps.
- En conclusion : Il n'y a pas d'intérférences.
==干涉发生条件之一：必须从同一个发光源产生==
### Interférences entre ondes issues d'une source uniques
- 2 Types de dispositifs interférentiels ![[Assets/截屏2023-02-23 10.28.21.png]]
	- division du **Front d'onde** (deux rayons *différentes*)
	- division d'**amplitude** (un *même* rayon) 
- **Différence de marche** en $M$ $$\boxed{\delta_{2 / 1}= (SM)_{2}-(SM)_{1}}$$donc $$\Delta \varphi_{2 / 1}(M) = k_{0} \delta_{2 / 1} + \Delta \varphi_{\text{sup}}$$D'après [[2A Interférences lumineuses 光的干涉#Franges d'interférences, Franges brillantes, Franges sombres]] $\delta_{2 / 1} = m \text{ ou } (m+ 1 / 2) \lambda_{0}$ car ![[Assets/Pasted image 20230223103410.png]]
- Lorsque $\Delta_{\text{sup}}=0$, on a :
	- Interférences **constructives** $$\Delta \varphi_{2 / 1}(M) = m\times 2\pi,\;\delta_{2 / 1} = m \times\lambda_{0}$$
	- Interférences **destructives** $$\Delta\varphi_{2 / 1}(M) = \left( m+\frac{1}{2} \right)\times 2\pi,\;\delta_{2 / 1}=\left( m+\frac{1}{2} \right)\times\lambda_{0}$$
- On ne peut observer des interférences qu'entre deux ondes *provenant d'un même train d'onde* : $$|\delta_{2 / 1}| <l_{c}$$==干涉发生条件之一：两波光程差小于列波长度==
![[Assets/截屏2023-03-02 00.14.31.png]]
### Conclusion

Pour observer le phénomène d'interférences, il faut : 
1. des signaux issus d’une *source unique*
2. des signaux d’*intensités comparables* 
3. une <u>différence de marche plus faible que la longueur de cohérence</u> de la source