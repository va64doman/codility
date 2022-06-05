#EquiLeader: Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
def equiLeader(A):
    B = A.copy()
    B.sort()
    c = 1
    le = 0
    n = 0

    for i in range(1, len(B)):
        if B[i] != B[i-1]:
            c = 1
        else:
            c += 1
        if c > len(B) / 2:
            le = B[i]
            break
    for i in range(0, len(A)):
        if A[i] == le:
            n += 1

    EqL = 0
    c = 0
    for i in range(0, len(A)):
        if A[i] == le:
            c += 1
        if i + 1 < 2 * c and len(A) - i - 1 < 2 * (n-c):
            EqL += 1
    return EqL
    pass

#[4,3,4,4,4,2] = 2
print("[4,3,4,4,4,2], the number such that the leaders of the sequences are the same is", str(equiLeader([4,3,4,4,4,2])))
