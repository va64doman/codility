#NumberOfDiscIntersections: Compute the number of intersections in a sequence of discs.
def noOfDiscInter(A):
    if len(A) == 0:
        return 0
    S = [0] * len(A)
    E = [0] * len(A)
    CS = [0] * len(A)
    CE = [0] * len(A)

    for i in range(0, len(A)):
        if i - A[i] <= 0:
            S[i] = 0
        else:
            S[i] = i - A[i]
        if i + A[i] > len(A)-1:
            E[i] = len(A)-1
        else:
            E[i] = i + A[i]
        CS[S[i]] += 1
        CE[E[i]] += 1

    CCS = [0] * len(A)
    CCE = [0] * len(A)
    CCS[0] = CS[0]
    CCE[0] = CE[0]

    for i in range(1, len(A)):
        CCS[i] = CS[i] + CCS[i-1]
        CCE[i] = CE[i] + CCE[i-1]

    tot = 0
    for i in range(0, len(A)):
        if i == 0:
            tot += (CCS[i] - CS[i]) * CS[i] + CS[i] * (CS[i] - 1) / 2
        else:
            tot += (CCS[i] - CCE[i-1] - CS[i]) * CS[i] + CS[i] * (CS[i] - 1) / 2
    if tot > 10000000:
        return -1
    return int(tot)
    pass

#[1,5,2,1,4,0] = 11
print("[1,5,2,1,4,0], the number of intersections in the sequence of discs is ", str(noOfDiscInter([1,5,2,1,4,0])))
