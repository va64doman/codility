# Aluminium 2014
# MaxSliceSwap: Find the maximum sum of a compact subsequence of array elements after performing a single swap operation.
def maxSliceSwap(A):
    answer = findMax(A)
    A.reverse()
    answer = max(answer, findMax(A))
    return answer
    pass

def findMax(A):
    N = len(A)
    F = [0] * N
    F[0] = A[0]
    now = A[0]
    for i in range(1, N):
        now = max(now, A[i])
        F[i] = max(A[i] + F[i - 1], now)
    G = [0] * N
    G[N - 1] = A[N - 1]
    answer = A[N - 1]
    for i in range(N-2, -1, -1):
        G[i] = max(G[i + 1], 0) + A[i]
        answer = max(answer, G[i])
    for i in range(1, N):
        answer = max(answer, G[i] - A[i] + F[i - 1])
    return answer
    pass

# [3,2,-6,3,1] = 9
print("[3,2,-6,3,1], the maximum possible sum of any slice after a single swap operation is", str(maxSliceSwap([3,2,-6,3,1])))