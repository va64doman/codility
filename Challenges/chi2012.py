# Chi 2012
# Cannonballs: Simulate a cannon shooting and heaps of falling cannonballs
def cannonballs(A,B):
    M = len(A)
    N = len(B)
    H = max(B)
    T = [-1] * (H + 1)
    i = 0
    for j in range(H + 1):
        while i < M and A[i] < j:
            i += 1
        T[j] = i
    for j in B:
        i = T[j]
        if 0 < i < M:
            A[i-1] += 1
            if T[A[i-1]] > i - 1:
                T[A[i-1]] = i - 1
    return A
    pass
# (A = [1,2,0,4,3,2,1,5,7], B = [2,8,0,7,6,5,3,4,5,6,5]) = [2,2,2,4,3,3,5,6,7]
print("A = [1,2,0,4,3,2,1,5,7], B = [2,8,0,7,6,5,3,4,5,6,5], the final contents of A is", str(cannonballs(A = [1,2,0,4,3,2,1,5,7], B = [2,8,0,7,6,5,3,4,5,6,5])))