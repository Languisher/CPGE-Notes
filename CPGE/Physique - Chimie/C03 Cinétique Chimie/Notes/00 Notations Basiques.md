> Date : 2023-02-22 Matériaux : [[Thermochimie_Cours_reaction_rappels.pdf]]

## Notations Basiques
```ad-note
title: Équation Bilan
$$
\alpha_{1}A_{1}+ \dots+\alpha_{n}A_{n}=\beta_{1}B_{1}+\dots+\beta_{p}B_{p}
$$
- Elle doit *conserver la charge totale* et *conserver la quantité de chaque élément chimique*
- $A_{i}$ est dit **réactifs** et $B_i$ est dit **produits**
- $\alpha$ et $\beta$ est dit **coefficients stoechiométriques**

Cette équation est équivalente à $$0 = \sum_{i}\nu_{i}C_{i}$$ avec $\nu_{i}$ les **coefiicients stoechiométriques algébriques**, $$\nu_{i}=\begin{cases}
-\alpha_{i}<0 \text{ pour les réactifs}  \\\beta _{i}>0 \text{ pour les produits}\end{cases}$$ 

- On note $n_{i}$ la **quantité de matière** de $C_{i}$ à un instant quelconque
- L'**avancement** de réaction $\xi$, nul au début de la réaction, est défini par $$\mathrm{d}\xi= \frac{\mathrm{d}n_{i}}{\nu_{i}}$$ pour tout $i$, et on a $$n_{i}=n_{i,0}+\nu_{i}\xi$$ C’est une grandeur homogène à une quantité de matière (en $\mathrm{mol}$).
- Lorsque $\xi$ augmente, le système évolue dans le **sens direct** (symbolisé par →). 
- Lorsque $\xi$ diminue , le système évolue dans le **sens indirect**, ou sens inverse (symbolisé par ←)
```

- Quelle est l'**avancement final** $\xi_{f}$ ?

```ad-note
title: Tableau d'avancement et état final
![[Pasted image 20230222081831.png]]
- La réaction est **totale** si $\xi_{f}=\xi_{\mathrm{\max{}}}$, **réactif limitant** est le réactif qui a déjà disparu.
- La réaction est **limitée** lorsque $\xi_{f}<\xi_{\mathrm{\max{}}}$
- Les réactifs sont introduits en **proportions stoéchiométriques** quand $$\frac{n_{i,0}}{|\nu_{i}|}=k \text{ (constante)}$$ Ils sont tous limitants et disparaissent tous si la réaction est totale.
```

- Exemple : ![[Pasted image 20230222083814.png]]
