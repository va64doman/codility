# Lithium 2013
# Clocks: Find the maximal number of clocks with hands that look identical when rotated.
def clocks(A, P):
    # P is unnecessary because the solution does not have P.
    for i in range(len(A)):
        B = A[i]
        B.sort()
        A[i] = B
    for i in range(len(A)):
        K = A[i][0]
        for j in range(len(A[0])):
            A[i][j] -= K
    strings = []
    for i in range(len(A)):
        s = ""
        for j in range(len(A[0])):
            s = s + str(A[i][j]) + ","
        strings.append(s)
    strings.sort()
    result = 0
    pair = 0
    for i in range(1, len(A)):
        if strings[i] == strings[i-1]:
            pair += 1
            result += pair
        else:
            pair = 0
    return result
    pass

# (A = [[1,2],[2,4],[4,3],[2,3],[1,3]], P = 4) = 4
print("A = [[1,2],[2,4],[4,3],[2,3],[1,3]], P = 4, the maximal number of clocks with hands that look identical when rotated is", 
str(clocks(A = [[1,2],[2,4],[4,3],[2,3],[1,3]], P = 4)))