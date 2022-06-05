# MaxDoubleSliceSum: Find the maximal sum of any double slice.
# A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.
# The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].
def maxDoubleSliceSum(A):
    n = len(A)
    if n <= 3:
        return 0
    LR = n * [0]
    RL = n * [0]
    
    s = 0
    for i in range(1, n-1):
        s += A[i]
        if s < 0:
            s = 0
        LR[i] = s

    s = 0
    for i in range(n-2, 0, -1):
        s += A[i]
        if s < 0:
            s = 0
        RL[i] = s

    m = 0
    for i in range(0, n-2):
        m = max(m, LR[i] + RL[i+2])

    return m
    pass

#[3,2,6,-1,4,5,-1,2] = 17
print("[3,2,6,-1,4,5,-1,2], maxmimal sum of double slice is", str(maxDoubleSliceSum([3,2,6,-1,4,5,-1,2])))
