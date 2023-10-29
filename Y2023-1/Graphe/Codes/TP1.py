def complet(n):
    M=[[1 for j in range(n)] for i in range(n)]
    for k in range(n):
        M[k][k]=0
    return M
    
def lineaire(n):
    M=[[0 for j in range(n)] for i in range(n)]
    for k in range(n-1):
        M[k][k+1]=1
        M[k+1][k]=1
    return M

def cyclique(n):
    M=lineaire(n)
    M[0][n-1]=1
    M[n-1][0]=1
    return M
    
def ordre(M):
    return len(M)
    
def taille(M):
    n=len(M)
    S=0
    for i in range(n):
        for j in range(n):
            S=S+M[i][j]
    return S/2
    
def est_voisin(M,i,j):
    if M[i-1][j-1]==0:
        return False
    else:
        return True
        
def degre(M,i):
    n=len(M)
    S=0
    for j in range(n):
        S=S+M[i-1][j]
    return S
    
def complet2(n):
    L=[]
    for i in range(1,n+1):
        Vi=[j for j in range(1,n+1)]
        Vi.remove(i)
        L.append(Vi)
    return L
    
def lineaire2(n):
    L=[[2]]
    for i in range(2,n):
        L.append([i-1,i+1])
    L.append([n-1])
    return L

def cyclique2(n):
    L=[[2,n]]
    for i in range(2,n):
        L.append([i-1,i+1])
    L.append([1,n-1])
    return L
    
def ordre2(L):
    return len(L)
    
def taille2(L):
    n=len(L)
    S=0
    for i in range(n):
        S=S+len(L[i])
    return S/2

def est_voisin2(L,i,j):
    if j in L[i-1]:
        return True
    else:
        return False
        
def degre2(L,i):
    return len(L[i-1])

def matrice_vers_liste(M):
    n=len(M)
    L=[]
    for i in range(n):
        Vi=[]
        for j in range(n):
            if M[i][j]!=0:
                Vi.append(j+1)
        L.append(Vi)
    return L
    
def liste_vers_matrice(L):
    n=len(L)
    M=[[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if j+1 in L[i]:
                M[i][j]=1
    return M

def parties(n,k):
    if k==1:
        return [[i] for i in range(1,n+1)]
    else:
        L=[]
        Lprecedent=parties(n,k-1)
        for partie in Lprecedent:
            for i in range(partie[k-2]+1,n+1):
                L.append(partie+[i])
        return L

def est_disjoint(partie1,partie2):
    for i in partie1:
        if i in partie2:
            return False
    return True

def matrice_kneser(n,k):
    sommets=parties(n,k)
    ordre=len(sommets)
    M=[[0 for j in range(ordre)] for i in range(ordre)]
    for i in range(ordre):
        for j in range(ordre):
            if est_disjoint(sommets[i],sommets[j]):
                M[i][j]=1
    return M
    
def liste_kneser(n,k):
    return matrice_vers_liste(matrice_kneser(n,k))

    
    
    
    
    
    