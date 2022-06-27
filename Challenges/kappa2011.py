# Kappa 2011
# SpaceCrews: Find the number of different ways in which the space crew can be selected.
MOD = 1410000017
F = [1]

def extendedEuclidean(A,B):
    if B == 0:
        return A, 1, 0
    Q, R = divmod(A, B)
    D, K, L = extendedEuclidean(B, R)
    return D, L, K - Q * L
    pass

def modularMultiplicativeInverse(A):
    D, K, L = extendedEuclidean(A, MOD)
    return K

def factorial(N):
    global F
    K = len(F)
    while K <= N:
        F.append((K * F[-1]) % MOD)
        K += 1
    return F[N]

def binomialCoefficient(N, K):
    R = 1
    R = (R * factorial(N)) % MOD
    R = (R * modularMultiplicativeInverse(factorial(K))) % MOD
    R = (R * modularMultiplicativeInverse(factorial(N-K))) % MOD
    return R

def spaceCrews(T, D):
    N = len(T)
    R = 1
    for t, d in zip(T, D):
        R = (R * binomialCoefficient(t, d)) % MOD
    return R
    pass

# (T = [6,4,7], D = [1,3,4]) = 840
print("T = [6,4,7], D = [1,3,4], the number of different ways to select space crew is", str(spaceCrews(T = [6,4,7], D = [1,3,4])))