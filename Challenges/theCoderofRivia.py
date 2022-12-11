# The Coder of Rivia
# AlmostMagicSquare: Given a 3x3 matrix, find the nearest matrix, the sum of whose elements in each row and column is equal.

def almostMagicSquare(A):
    N = 3
    def rowSum(i):
        return sum(A[i*3 + j] for j in range(N))
        pass
    def colSum(i):
        return sum(A[j*3 + i] for j in range(N))
        pass
    M = 0
    for i in range(N): M = max(M, rowSum(i), colSum(i))
    for i in range(N):
        for j in range(N):
            inc = M - max(rowSum(i), colSum(j))
            A[i*3 + j] += inc
    return A
    pass

# [0, 2, 3, 4, 1, 1, 1, 3, 1] = [1, 2, 3, 4, 1, 1, 1, 3, 2]
print("[0, 2, 3, 4, 1, 1, 1, 3, 1], the sum of whose elements in each row and column is equal is", str(almostMagicSquare([0, 2, 3, 4, 1, 1, 1, 3, 1])))
# [1, 1, 1, 2, 2, 1, 2, 2, 1] = [1, 1, 3, 2, 2, 1, 2, 2, 1]
print("[1, 1, 1, 2, 2, 1, 2, 2, 1], the sum of whose elements in each row and column is equal is", str(almostMagicSquare([1, 1, 1, 2, 2, 1, 2, 2, 1])))
