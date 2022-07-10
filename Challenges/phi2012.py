# Phi 2012
# TilingsCount: Count tilings of a narrow but long rectangle with tiles of size 1x1 or 2x2.
def feasible(x):
    ok= True
    while(x > 0):
        if x % 2 == 1:
            ok = not ok
        elif not ok:
            return False
        x = x//2
    return ok
    pass

def rowMatrix(M):
    mm=2**M
    A = [[0] * mm for i in range(mm)]
    for i in range(mm):
        if feasible(i):
            for j in range(mm):
                if feasible(j) and (i & j) == 0:
                    A[i][j] = 1
    return A
    pass

def ident(size):
    Id = [[0]*size for i in range(size)]
    for i in range(size):
        Id[i][i] = 1
    return Id
    pass

def matrixMult(A, B, ModRes):
    size = len(A)
    C = [[0]*size for i in range(size)]
    for i in range(size):
        for j in range(size):
            cc = 0
            for k in range(size):
                cc = (cc + (A[i][k] % ModRes) * (B[k][j] % ModRes))% ModRes
            C[i][j]= cc
    return C
    pass

def matrixExp(A, N, ModRes):
    size = len(A)
    B = ident(size)
    while N > 0:
        if N % 2 == 1:
            B = matrixMult(A, B, ModRes)
        A = matrixMult(A, A, ModRes)
        N = N//2
    return B
    pass

def tilingsCount(N, M):
    B = matrixExp (rowMatrix(M), N, 10000007)
    return B[0][0]
    pass
# (N = 4, M = 3) = 11
print("The board is 4 rows and 3 columns, the number of tilings is", str(tilingsCount(4,3)))