# Oxygenium 2014
#CountBoundedSlices: Calculate the number of slices in which (maximum - minimum <= K).
def countBoundedSlices(K, A):
    maxINT = 10 ** 9
    N = len(A)
    maxQ = [0] * (N + 1)
    posmaxQ = [0] * (N + 1)
    minQ = [0] * (N + 1)
    posminQ = [0] * (N + 1)

    firstMax, lastMax = 0, -1
    firstMin, lastMin = 0, -1
    j, result = 0, 0

    for i in range(N):
        while j < N:
            while lastMax >= firstMax and maxQ[lastMax] <= A[j]:
                lastMax -= 1
            lastMax += 1
            maxQ[lastMax] = A[j]
            posmaxQ[lastMax] = j
            while lastMin >= firstMin and minQ[lastMin] >= A[j]:
                lastMin -= 1
            lastMin += 1
            minQ[lastMin] = A[j]
            posminQ[lastMin] = j
            if maxQ[firstMax] - minQ[firstMin] <= K:
                j += 1
            else:
                break
        result += (j - i)
        if result == maxINT:
            return maxINT
        if posminQ[firstMin] == i:
            firstMin += 1
        if posmaxQ[firstMax] == i:
            firstMax += 1
    return result
    pass

#(K = 2, A = [3,5,7,6,3]) = 9
print("(K = 2, A = [3,5,7,6,3]), the number of slices in which max - min <= 2 is", str(countBoundedSlices(K = 2, A = [3,5,7,6,3])))
