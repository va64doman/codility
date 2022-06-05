#Dominator: Find an index of an array such that its value occurs at more than half of indices in the array.
def dominator(A):
    if len(A) == 0:
        return -1
    elif len(A) == 1:
        return 0
    B = A.copy()
    B.sort()

    c = 1
    n = len(B)
    for i in range(1,n):
        if B[i] != B[i-1]:
            c = 1
        else:
            c += 1
        if c > int(n/2):
            return A.index(B[i])
    return -1
    pass

#[3,4,3,2,3,-1,3,3] = 0,2,4,6 or 7
print("[3,4,3,2,3,-1,3,3], dominatior is at index", str(dominator([3,4,3,2,3,-1,3,3])))
