#TieRopes: Tie adjacent ropes to achieve the maximum number of ropes of length >= K.
def tieRopes(K, A):
    currentLen = ropes = 0

    for i in range(len(A)):
        currentLen += A[i]
        if currentLen >= K:
            ropes += 1
            currentLen = 0
    return ropes
            
    pass

#(K = 4, A = [1,2,3,4,1,1,3]) =  3
print("K = 4, A = [1,2,3,4,1,1,3], the maximum number of ropes of length >= 4 is", str(tieRopes(K = 4, A = [1,2,3,4,1,1,3])))
