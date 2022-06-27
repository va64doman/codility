# Nu 2011
# DoubleMedian: Given two slices of sorted arrays, find the median. Repeat for many such slices, return the median of the results.
def doubleMedian(A,B,P,Q,R,S):
    n = len(A)
    m = len(B)
    k = len(P)
    medx = [0]*k
    for i in range(k):
        medx[i] = median(P[i], Q[i], R[i], S[i], A, B)
    medx.sort()
    return medx[k // 2]
    pass

def median(p, q, r, s, A, B):
    x = q-p+1
    y = s-r+1
    z = abs(x-y) // 2
    if x > y:
        if A[p+z] >= B[s]:
            return A[p+z]
        elif A[q-z] <= B[r]:
            return A[q-z]
        else:
            return med(p+z, q-z, r, s, A, B)
    else:
        if B[r+z] >= A[q]:
            return B[r+z]
        elif B[s-z] <= A[p]:
            return B[s-z]
        else:
            return med(p, q, r+z, s-z, A, B)
    pass

def med(p, q, r, s, A, B):
    x = q-p+1
    y = s-r+1
    if x + y < 5:
        medi = A[p:q+1]+B[r:s+1]
        medi.sort()
        return medi[(x+y)//2]
    else:
        d = (x+y) // 4
        if A[p+d] < B[s-d]:
            return med(p+d, q, r, s-d, A, B)
        else:
            return med(p, q-d, r+d, s, A, B)
    pass

# (A = [-2,4,10,13], B = [5,6,8,12,13], P = [2,1,0], Q = [3,2,3], R = [0,0,1], S = [4,0,3]) = 8
print("A = [-2,4,10,13], B = [5,6,8,12,13], P = [2,1,0], Q = [3,2,3], R = [0,0,1], S = [4,0,3], the median is",
str(doubleMedian(A = [-2,4,10,13], B = [5,6,8,12,13], P = [2,1,0], Q = [3,2,3], R = [0,0,1], S = [4,0,3])))