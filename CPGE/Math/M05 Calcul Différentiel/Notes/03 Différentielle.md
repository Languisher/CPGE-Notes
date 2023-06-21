
```ad-note 
title: Petit $o$
- La notation **petit $o$**$$o_{h \to 0_{\mathbb{R}^n}}(|h|)$$désigne une fonction $\phi$ définie au voisinage de $0_{\mathbb{R}^n}$ à valeurs dans $\mathbb{R}^p$ telle que $$\lim_{ h \to 0_{\mathbb{R}^n} } \frac{|\phi(h)|}{|h|}=0$$
- Exemple : Si $\alpha>1$ et la fonction $f: x \mapsto | |x | |^\alpha$
```

## Différentielle
```ad-note
title: Différentiable et Différentielle
- $f:O\to \mathbb{R}^p$ est **différentiable en** $x_{0}\in O$ s'il *existe une application linéaire* $df_{x_{0}}\in \mathscr{L}(\mathbb{R}^n,\mathbb{R}^p)$ telle que pour tout $h\in \mathbb{R}^n$ tel que $x+h \in O$, $$f(x_{0}+h)=\underbrace{f(x_{0})}_{\text{terme constante}}+\underbrace{\mathrm{d}f_{x_{0}}(h)}_{\text{terme linéaire en }h}+\underbrace{o_{h \to 0_{\mathbb{R}^n}}(| |h||)}_{\text{terme négligable}}$$et $\mathrm{d}f_{x_{0}}$ s'appelle la **différentielle de $f$ en $x_0$**, défini par : $$\mathrm{d}f_{x_{0}}(h) = \lim_{ t \to 0 } \frac{f(x_{0}+th)-f(x_{0})}{t}$$
	- Dire que $f$ est **différentiable en** $x_0$, c'est dire qu'elle admet *un développement limité d'ordre 1 au voisinage* $x_0$. 
	- Le terme $f (x_0) + \mathrm{d}f_{x_0} (h)$ est donc approximation *affine* locale de $f$ en $x_0$.
- $f: O \to \mathbb{R}^p$ est **différentiable sur $O$** si $f$ est *différentiable en tout $x \in O$*.
```

```ad-note
title: ==Lien avec la dérivée selon un vecteur==
$$
\partial_{v}f(x_{0}) = \mathrm{d}f_{x_{0}}(h)
$$
car $f(x_{0}+tv)-f(x_{0}) = \mathrm{d}f_{x_{0}}(tv) = t\mathrm{d}f_{x_{0}}(v)$, et on utilise les résultats dans [[02 Dérivées Partielles#Dérivée suivant un vecteur]]
```

```ad-attention
title: Si une fonction est différentiable en $a$, donc elle est continue en $a$.
```

```ad-note
title: Lien entre différentielle et dérivée (dimension 1, c'est-à-dire une seule variable)
- *Lien entre différentielle et dérivée (dimension 1, c'est-à-dire une seule variable)* : Soit $f : I → \mathbb{R}$. $f$ est **différentiable en** $x_0$ ssi *elle est dérivable en $x_{0}$*
- Si c’est le cas, pour tout $h ∈ \mathbb{R}$ tel que $x_0 + h ∈ I$, $$f (x_0 + h) = f(x_{0})+\underbrace{f'(x_{0})h}_{\mathrm{d}f_{x_{0}}(h)}+o(h)$$On en déduit que $df_{x_0} (h) = f'(x_{0})$ pour tout $h ∈ \mathbb{R}$.
```

```ad-note
title: Lien entre différentielle et dérivées partielles
- *Lien entre différentielle et dérivées partielles* : Soit $f : O \to \mathbb{R}^p$. Si $f$ est *différentiable en* $x_0$, alors elle **admet des dérivées partielles** en $x_0$ et $$\mathrm{d}f_{x_{0}}:h \mapsto \sum_{j=1}^n\partial_{j}f(x_{0})h_{j}$$
- Si c'est le cas, pour tout $h \in \mathbb{R}^n$ tel que $x_{0}+h \in O$, $$f(x_{0}+h)=f(x_{0})+\sum_{j=1}^n\partial_{j}f(x_{0})h_{j}+o_{h \to 0_{\mathbb{R}^n}}(|h|)$$```  

```ad-attention
title: Pour montrer que $f$ est **différentiable**, essayer de prouver que :
- Ses **dérivées partielles** existent à ce point
- Montrer que $$\lim_{ h \to 0 } \frac{f(x_{0}+h)-f(x_{0})- O(\Vert h\Vert )}{\Vert h\Vert }\to 0$$ou de trouver une cas contraire
```
### Différentielle Seconde
```ad-note
title: Différentiable Seconde
- Un fonction admet une **différentielle seconde** au point $x$ si sa *différentielle est différentiable*. On l'écrit $\mathrm{d}f_{x_{0}+h}$ : $$\mathrm{d}_{x_{0}+h}f=\underbrace{\mathrm{d}_{x_{0}}f}_{\text{terme constant}}+ \underbrace{\mathrm{d}_{x_{0}}^2f(h)}_{\text{terme linéaire en }h} + \underbrace{o(\Vert h\Vert )}_{\text{terme négligable}}$$
```

### Opérations sur les fonctions différentiables
#### Linéarité
```ad-note
title: Linéarité de la Différentielle
- Si deux fonction est différentiable, donc leur combinasion linéaire est aussi différentiable.
- Si $f$ et $g$ sont différentiables, donc $$\lambda f+ \mu g \text{ est différentiable, et } \mathrm{d}(\lambda f+\mu g) = \lambda \mathrm{d}f+\mu \mathrm{d}g$$
```

#### Produit
```ad-note
title: Produit de fonctions réelles
- Si $f$ et $g$ sont différentiables, alors : $$\mathrm{d}(fg) = g\mathrm{d}f + f\mathrm{d}g$$
```

#### Composition
```ad-note
title: ==Le cas des fonctions composées==
Soit $f:O \to \mathbb{R}^p$ et $g:O\to \mathbb{R}^q$. $g \circ f$ est **différentiable** en $x_0$ si $f$ est différentiable en $x_0$ et $g$ est différentiable en $f(x_{0})$, et : $$\mathrm{d}(g \circ f)_{x_{0}}=\mathrm{d}g_{f(x_{0})}\circ\mathrm{d}f_{x_{0}}$$
> Démonstration : ![[Pasted image 20230315130417.png]]
```

#### Application Bilinéaires

```ad-note
title: ==Différentielle d'une application bilinéaire==
- $B(f,g):\mathbb{R}^{p_{1}} \times \mathbb{R}^{p_{2}} \to \mathbb{R}^q$ est **bilinéaire**, $f$ et $g$ deux fonctions **différentiables en $x_{0}$**, alors $B(f,g)$ est différentiable en $x_{0}$ et : $$\mathrm{d}(B(f,g))_{x_{0}} : h \longmapsto B(\mathrm{d}f_{x_{0}}(h),g(x_{0})) + B(f(x_{0}), \mathrm{d}g_{x_{0}}(h))$$
> Démonstration et exemple d'un produit scalaire : ![[Pasted image 20230315132102.png]]
```

```ad-question
Montrer qu'une fonction est différentiable ou deux fois différentiable (point spécial): TD 1-2, TD 1-3, TD 1-4, TD 1-7, TD 1-8
Calculer la différentielle : TD 1-1, TD 1-2
Calculer la différentielle seconde : TD 1-1, TD 1-2
```

## De Classe $\mathscr C^1$
```ad-note
title: De classe $\mathscr C^1$
- On dit que $f$ est de classe $\mathscr C ^1$ sur O si elle vérifie les conditions équivalentes : Équivalence de la **continuité de la différentielle** et des **dérivées partielles** : 
	- $f$ admet des dérivées partielles sur $O$ et ces *dérivées partielles sont continues* sur $O$ ; 
	- $f$ est **différentiable** sur $O$ et $\mathrm{d}f$ est *continue* sur $O$.
```

```ad-attention
title: Pour montrer que une fonction est de classe $\mathscr C^1$, on doit montrer que la différentielle est *continue*, ou les *dérivées partielles* sont *continues*.
```

```ad-question
- Montrer que la fonction $f$ est de classe $\mathscr{C}^1$ (et un point spécial): TD1-3, TD1-8, TD2-5-1, TD2-5-4
```