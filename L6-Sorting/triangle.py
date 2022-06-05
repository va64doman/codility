# Triangle: Determine whether a triangle can be built from a given set of edges.
# Return 1 if the array can make at least one triangle, otherwise 0.
# Since 0 <= P < Q < R < N, A[Q] + A[R] > A[P] and A[R] + A[P] > A[Q] is always true
# A[P] + A[Q] > A[R] is depends of P and Q
def triangle(A):
    if len(A) < 3:
        return 0
    A.sort()
    for i in range(0, len(A) - 2):
        if(A[i] + A[i+1] > A[i+2]):
            return 1
    return 0
    pass

#[10,2,5,1,8,20] = 1
#[10,50,5,1] = 0
print("[10,2,5,1,8,20] is", 'triangular' if triangle([10,2,5,1,8,20]) == 1 else 'not triangular')
print("[10,50,5,1] is", 'triangular' if triangle([10,50,5,1]) == 1 else 'not triangular')
