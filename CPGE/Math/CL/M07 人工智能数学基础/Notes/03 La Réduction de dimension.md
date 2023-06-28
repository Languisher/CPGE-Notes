> Cours : 2023-02-27

Notations : Pour $x$ in $E$, avec $E$ un espace euclidien, lorsqu'on manipulera $x$ comme :
- $\vec{x} \in E$ : Un **vecteur**
- $X \in E$ : Un **point**

## SVD (Singular Value Decomposition)
### Theory
```ad-note
title: SVD
A rectangular matrix $A_{m\times n}$ can be broken down into the product of three matrices - an *orthogonal matrix* $U$, a *diagonal matrix* $\Sigma$, and the *transpose of an orthogonal matrix* $V$ with the equation : $$\underbrace{A}_{m\times n}=\underbrace{U}_{m\times m}\times \underbrace{\Sigma}_{m \times n}\times \underbrace{V^ T}_{n\times n} $$
- The columns of $U$ are *orthonormal eigenvectors* of $A A^ T$ (i.e. $U^ T U =I$)
- The columns of $V$ are *orthonormal eigenvectors* of $A^ T A$ (i.e. $Q^T Q + I$)
- $\Sigma$ is a *diagnoal matrix* containing the <u>square roots of eigenvalues</u> from $U$ or $V$, in *descending order*.
```

```ad-hint
title: Example
![[191679038131_.pic.jpg]]
```
### Code
```jupyter
import numpy as np

# Define your matrix A (you can replace this with your own matrix)
A = np.array([[1, 2], [3, 4], [5, 6]])

# Perform SVD
U, S, VT = np.linalg.svd(A)

print("Matrix U:")
print(U)
print("\nMatrix S (as a diagonal matrix):")
print(np.diag(S))
print("\nMatrix VT:")
print(VT)

# Note that the `S` returned by `np.linalg.svd` is a 1D array containing the singular values, 
# so you might want to convert it to a diagonal matrix with `np.diag(S)`.
```

### Reference
- Hervé Abdi, Lynne J. Williams (2010) - Principal component analysis [==*Read it now! See in Zotero*==](zotero://select/items/@abdiPrincipalComponentAnalysis2010a) **Web:** [Open online](https://onlinelibrary.wiley.com/doi/abs/10.1002/wics.101)


## PCA (L'analyse en composantes principales)


### Cas de la dimension 1
```ad-note
title: Droite de régression orthogonale
On appelle **droite de régression linéaire orthogonale** la droite $\Delta$ qui minimise $$\sum_{j=1}^nd(X_{j},\Delta)^2$$
```

- $\Delta$ est présentée par la donné d'un point $\Omega$ et d'un vecteur unitaire directeur $\vec{u}$
- **Distance à une droite affine** : Soit $\Delta$ est représentée par la donné d'un point $\Omega$ et d'un vecteur directeur $\vec{u}$, la distance est donc donné par : $$d(X, \Delta)^2= \Vert \vec{\Omega X}\Vert ^2-<\vec{\Omega X}, \vec{u}>^2$$![[Drawing 2023-02-27 16.22.23.excalidraw]]
- Proposition : La droite de régression est la droite défini par $\Omega$ et $\vec{u}$, avec $$\Omega =  \mathrm{Bar}(X_{1},\dots ,X_{n})$$et $\vec{u}$ est un *vecteur unitaire associé à la plus grande valeur propre de la matrice $B$ où $$B=\mathrm{Mat}(\vec{GX_{1}},\dots,\vec{GX_{n}})\in \mathrm{M}_{p,n}(\mathbb{R})$$Preuve : ![[Pasted image 20230227171730.png]]

## 参考资料
- Hervé Abdi, Lynne J. Williams (2010) - Principal component analysis
	[==*Read it now! See in Zotero*==](zotero://select/items/@abdiPrincipalComponentAnalysis2010a)
	**Web:** [Open online](https://onlinelibrary.wiley.com/doi/abs/10.1002/wics.101)


