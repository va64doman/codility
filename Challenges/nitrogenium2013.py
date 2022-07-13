# Nitrogenium 2013
# FloodedIsland: Count the number of islands on consecutive days.
def floodedIsland(A,B):
    N = len(A)
    M = len(B)
    size = max(max(A), max(B))
    island = [0] * (size + 2)
    for i in range(1, N):
        if A[i - 1] > A[i]:
            island[A[i - 1]] += 1
            island[A[i]] -= 1
    island[A[N - 1]] += 1
    for i in range(size, -1, -1):
        island[i] += island[i + 1]
    result = [0] * M
    for i in range(M):
        result[i] = island[B[i] + 1]
    return result
    pass

# (A = [2,1,3,2,3], B = [0,1,2,3,1]) = [1,2,2,0,2]
print("A = [2,1,3,2,3], B = [0,1,2,3,1], the number of islands on consecutive days are", str(floodedIsland(A = [2,1,3,2,3], B = [0,1,2,3,1])))