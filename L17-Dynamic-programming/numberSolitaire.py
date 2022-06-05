#NumberSolitaire: In a given array, find the subset of maximal sum in which the distance between consecutive elements is at most 6.
def numSol(A):
    R = [0] * len(A)
    for i in range(len(R)):
        if i == 0:
            R[i] = A[i]
        else:
            maxOnSquare = -10001
            for j in range(1, 7):
                if i - j >= 0:
                    maxOnSquare = max(maxOnSquare, R[i-j] + A[i])
            R[i] = maxOnSquare
    return R[len(R) - 1]        
    pass

#[1,-2,0,9,-1,-2] = 8
print("[1,-2,0,9,-1,-2], the subset of maximal sum in which the distance between consecutive elements is at most 6 is", str(numSol([1,-2,0,9,-1,-2])))
