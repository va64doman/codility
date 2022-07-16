# Magnesium 2014
# AscendingPaths: Find the longest path in a weighted graph in which the weights are ascending.
from functools import cmp_to_key
def ascendingPaths(N, A, B, C):
    M = len(A)
    w = [0] * N
    updates = []
    ind = list(range(M))
    ind.sort(key=cmp_to_key(lambda i, j: C[j] - C[i]))
    for i in range(M):
        u = A[ind[i]]
        v = B[ind[i]]
        updates.append((u, max(w[u], w[v] + 1)))
        updates.append((v, max(w[v], w[u] + 1)))
        if i == M - 1 or C[ind[i]] > C[ind[i + 1]]:
            for v, val in updates:
                w[v] = max(w[v], val)
            updates = []
    return max(w)
    pass

# (N = 6, A = [0,1,1,2,3,4,5,3], B = [1,2,3,3,4,5,0,2], C = [4,3,2,5,6,6,8,7]) = 4
print("N = 6, A = [0,1,1,2,3,4,5,3], B = [1,2,3,3,4,5,0,2], C = [4,3,2,5,6,6,8,7], the length of longest path is", 
str(ascendingPaths(N = 6, A = [0,1,1,2,3,4,5,3], B = [1,2,3,3,4,5,0,2], C = [4,3,2,5,6,6,8,7])))