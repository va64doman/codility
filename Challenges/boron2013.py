# Boron 2013
#Flags: Find the maximum number of flags that can be set on mountain peaks.
#A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].
def flags(A):
    if len(A) < 3:
        return 0
    P = []
    for i in range(1, len(A) -1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            P.append(i)
    if len(P) == 0:
        return 0
    elif len(P) == 1:
        return 1

    c = 1
    m = 0

    for k in range(min(len(P), int(len(A)**0.5)) + 1, 0, -1):
        lastF = 0
        c = 1
        for i in range(1, len(P)):
            if P[i] - P[lastF] >= k and c < k:
                c += 1
                lastF = i
        if c < m:
            return m
        elif m < c:
            m = c
    return m
    pass

#[1,5,3,4,3,4,1,2,3,4,6,2] = 3
print("[1,5,3,4,3,4,1,2,3,4,6,2], the max number of flags is", str(flags([1,5,3,4,3,4,1,2,3,4,6,2])))
