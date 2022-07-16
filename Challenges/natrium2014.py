# Natrium 2014
# MaxDistanceMonotonic: Find a pair (P, Q), such that A[P] <= A[Q] and the value Q - P is maximal.
def maxDistanceMonotonic(A):
    result = 0
    N = len(A)
    B = [0] * N
    for i in range(N - 1, -1, -1):
        B[i] = B[i + 1] if i + 1 < N and B[i + 1] > A[i] else A[i]
    i = 0
    j = 0
    while j < N:
        while j < N and B[j] >= A[i]:
            j += 1
        result = j - i - 1
        j += 1
        i += 1
    return result
    pass

# [5,3,6,3,4,2] = 3
print("[5,3,6,3,4,2], the value Q - P is maximal is", str(maxDistanceMonotonic([5,3,6,3,4,2])))