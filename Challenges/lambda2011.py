# Lambda 2011
# MinRouterPeripherality: For each node in a tree find the sum of distances to all other nodes.

def minRouterPeripherality(T):
    N = len(T)
    D = [0]*N
    for U in range(N):
        V = T[U]
        if V != U:
            D[V] = D[V] + 1
    O = [-1]*N
    M = 0
    for U in range(N):
        if D[U] == 0:
            O[M] = U
            M = M + 1
    for K in range(N-1):
        U = O[K]
        V = T[U]
        D[V] = D[V] - 1
        if D[V] == 0:
            O[M] = V
            M = M + 1
    P = [0]*N
    S = [1]*N
    for K in range(N-1):
        U = O[K]
        V = T[U]
        S[V] = S[V] + S[U]
        P[V] = P[V] + P[U] + S[U]
    for K in range(N-2, -1, -1):
        U = O[K]
        V = T[U]
        P[U] = P[V] - S[U] + N - S[U]
    C = 0
    for U in range(1, N):
        if P[U] < P[C]:
            C = U
    return C        
    pass

# [9,1,4,9,0,4,8,9,0,1] = 0
print("[9,1,4,9,0,4,8,9,0,1], the sum of distances to all other nodes is", str(minRouterPeripherality([9,1,4,9,0,4,8,9,0,1])))