> Date : 2023-02-13

> [!note] Le problème de l'ajustement
> - Soit $(x_{i},y_{i})_{{i \in [\![1,n]\!]}}\in (I \times E)^{[\![1,n]\!]}$ des donnés expérimentales (ou autres), où $E$ est un espace vectoriel normé.
> - On veut trouver une fonction $$f:I \to E \text{ t.q. } \forall i\in [\![1,n]\!], \; y_i=f(x_i)$$ si possible de classe $\mathscr C^k$, où $k \geq 1$.


## L'interpolation

> [!note] L'interpolation 
> - Soit $f:[a,b] \to E$, alors il existe une unique fonction polynomiale $L$ de degré $<n$, appelée **fonction d'interpolation de Lagrange** qui vérifie $\forall k\in [\![1,n]\!],\; L(x_{k})=f(x_{k})$, sa formule est : (Introduction : [[06A Dualité#Famille Duale, Base Duale, Base Ante-duale]])$$
\forall x\in [\![a,b]\!],\;L(x) =\sum_{k=1}^n\left( \prod_{{j\in[\![1,n]\!],\;j \ne k}} \frac{x-x_{j}}{x_{k}-x_{j}}\right).y_{k}$$

- Python 实现：`scipy.interpolate.lagrange`
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# 创建拉格朗日插值函数
f = lagrange(x, y)

# 用拉格朗日插值函数计算在其他点的插值值
x_interp = np.linspace(0, 5, num=100)
y_interp = f(x_interp)

# 绘制数据点和插值函数
plt.plot(x, y, 'o', label='data points')
plt.plot(x_interp, y_interp, '-', label='interpolation')
plt.legend()
plt.show()
```
- 例子  ![[Assets/截屏2023-02-13 16.34.28.png]]

> [!warning] Le principal défaut de l’interpolation (et aussi de l’approximation qui sera abordée en année 3) est que le degré augmente quand la taille des données augmente.


## Utilisation d'un modèle

```ad-note
title: Principe du fitting - Utilisation d'un modèle
Le principe du **fitting** est de *fixer la forme de la fonction qu'on cherche* et ensuite de *trouver les meilleurs paramètres* :
1. On choisit un **modèle**, càd une famille de fonctions $(f_{\lambda})_{\lambda\in \Lambda}$ de $\mathbb{R}$ dans $E$ dépdendant d'un paramètre $\lambda$ dans un ensemble $\Lambda$, $\Lambda \subset \mathbb{R}^p$.
	- Exemple : $g(t) =\sin(2t)+\cos(3t)$ et on souhait de chercher des fonctions de la forme $g(t)=a\sin(bt)+c\cos(dt)$, où $a,b,c,d \in \mathbb{R}$.

1. On définit ensuite la **fonction d'erreur** par, pour $\lambda \in \Lambda$,
$$
\text{Err}(\lambda) = \sum_{k=1}^n \lvert \lvert y_{k}-f_{\lambda}(x_{k}) \rvert  \rvert ^2
$$
1. Puis on cherche une valeur $\lambda$ pour **minimiser** la fonction d'erreur. 
```

> Mais comment faire la **minimisation** ? 


```ad-note
title: Minimisation
Soit $f\in \mathscr C^1(O, \mathbb{R})$ de $E$ espace vectoriel normé de dimension finie, alors $$[x_{0} \text{ minimum de } f \text{ sur } O] \implies [\mathrm{d}f_{x_{0}}=0_{E^\star}]$$
- Démonstration : ![[Pasted image 20230305093502.png]]
```

```ad-note
title: Méthode de minisation ou Méthode du gradient
Soit $f \in \mathscr C^1(O, \mathbb{R})$ ayant un minimum $m\in O$
- On part d'une valeur $x_{0}\in O$ (condition : *pas trop éloginée de* $m$)
- On construit $(x_{k})_{k\in \mathbb{N}}\in O^\mathbb{N}$ par *itération* où : $$\forall k\in \mathbb{N},\; x_{k+1}=x_{k}- \alpha_{k}.\mathrm{grad}_{x_{k}}f$$
	- *pas constant* : $\forall k\in \mathbb{N}, \; \alpha _k = \alpha$
	- *gradient optimal* : Sachant que $g:\alpha \mapsto f(x_{k}-\alpha.\mathrm{grad}_{x_{k}}f)$ minimale en $\alpha_{k}$. On va encore une fois **minimiser** la fonction $g$. Donc, on cherche les points d'annulation de la *dérivée* par une méthode de Newton (ou autre)
- On s'arrête lorsque le gradient est suffisament petit
```

```ad-caution
title: Une chose à faire attention : L'**initialisation** doit être faite avec précaution. Sinon, on peut trouver de moins bonnes solutions.
```

- Python 实现：`scipy.optimize.minimize`
```python
from scipy.optimize import minimize

def linear_model(x, a, b):
	return a*x+b

def err(param):
	global x, y, model
	return np.sum((y-model(x, *param))**2)

x = np.array([1, 2, 3, 4, 5])
y = np.array([0.1, 0.3, 0.5, 0.7, 1.0])
res_init = [1, 1]
model = linear_model

res = minimize(err, res_init).x # 注意这里需要加.x，不然不对

t = np.linspace(1, 5, 1000)
plt.scatter(x, y)
plt.plot(t, model(t, *res))
```
![[Assets/截屏2023-03-05 10.23.19.png]]
- Python 实现：`scipy.optimize.curve_fit`
```python
from scipy.optimize import curve_fit
param, _ = curve_fit(model, x, y)
```

## Choix du modèle
En fait, la mesure de l’erreur n’est pas la seule information utile. En effet, l’interpolation nous donne une erreur nulle alors que le résultat n’est pas satisfaisant, car il ne nous donne que *peu d’informations sur ce qui se passe en dehors des points* $(x_{k})_{k \in [\![1,n]\!]}$.

```ad-note
title: Évaluer la qualité du modèle
Pour mesurer la qualité d’un modèle, on peut procéder comme ceci. 
1. On calcule les paramètres du modèle pour les premières valeurs de $k\in [\![1,n]\!]$
2. Puis on compare ce que *prédit le modèle avec les valeurs suivantes*
```

```ad-note
title: Choix parmi des modèles
1. On établit un catalogue de modèles. 
2. Pour chaque modèle, on *résout le problème du fitting* (en faisant très attention aux problèmes d’initialisation de la fonction de minimisation).
3. Parmi les modèles donnant une plus petite valeur de la fonction d’erreur, on vérifie leur *capacité de prédiction*.
```
