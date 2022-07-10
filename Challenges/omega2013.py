# Omega 2013
# FallingDisks: Determine the number of disks that fit into the well.
def fallingDisks(A,B):
    N = len(A)
    M = len(B)
    for i in range(1,N):
        A[i] = min(A[i], A[i-1])
    i = 0
    while i < M and N > 0:
        while N > 0 and A[N-1] < B[i]:
            N -= 1
        if N > 0:
            N -= 1
            i += 1
    return i
    pass

# (A = [5,6,4,3,6,2,3], B = [2,3,5,2,4]) = 4
print("A = [5,6,4,3,6,2,3], B = [2,3,5,2,4], the number of disks that fit into the well is", str(fallingDisks(A = [5,6,4,3,6,2,3], B = [2,3,5,2,4])))