# Molybdenum 2019
# LeaderSliceInc: Given an array, find all its elements that can become a leader, after increasing by 1 all of the numbers in some segment of a given length.

def leaderSliceInc(K, M, A):
    N = len(A)
    for k in range(K):
        A[k] += 1            
    rec = [0]*(M+2)
    for a in A:
        rec[a] += 1    
    res = set()
    for i in range(1, M+2):
        if rec[i] > N//2:
            res.add(i)    
    for j in range(1, N-K+1):
        L, R = A[j-1], A[j+K-1]
        rec[L] -= 1
        rec[L-1] += 1
        rec[R] -= 1
        rec[R+1] += 1
        if rec[L-1] > N//2:
            res.add(L-1)
        if rec[R+1] > N//2:
            res.add(R+1)
        A[j-1] -= 1
        A[j+K-1] += 1    
    res = list(res)
    res.sort()
    return res
    pass

# (K = 3, M = 5, A = [2,1,3,1,2,2,3]) = [2,3]
print("K = 3, M = 5, A = [2,1,3,1,2,2,3], the elements that can become a leader is", str(leaderSliceInc(K = 3, M = 5, A = [2,1,3,1,2,2,3])))
# (K = 4, M = 2, A = [1,2,2,1,2]) = [2,3]
print("K = 4, M = 2, A = [1,2,2,1,2], the elements that can become a leader is", str(leaderSliceInc(K = 4, M = 2, A = [1,2,2,1,2])))
