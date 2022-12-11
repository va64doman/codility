# Bug Wars: The Last Hope
# Refueling: Given the locations of cities and the amount of fuel at
# each of them, compute the maximum number of cities that can be visited.

def refueling(A, X):
    def updateFuel(i, j, fuelBefore, distance, newFuel):
        if (fuelBefore >= distance):
            fuel[i][j] = max(fuel[i][j], fuelBefore - distance + newFuel)
        pass
    R = 1
    N = len(A)
    fuel = [[-1 for j in range(N)] for i in range(N)]
    for i in range(N): fuel[i][i] = A[i]
    
    for i in range(N - 2, -1, -1):
        for j in range(i + 1, N):
            updateFuel(i, j, fuel[i][j - 1], X[j] - X[j - 1], A[j])
            updateFuel(i, j, fuel[j - 1][i], X[j] - X[i], A[j])
            updateFuel(j, i, fuel[j][i + 1], X[i + 1] - X[i], A[i])
            updateFuel(j, i, fuel[i + 1][j], X[j] - X[i], A[i])
            if fuel[i][j] >= 0 or fuel[j][i] >= 0:
                R = max(R, j-i+1)
    return R
    pass

# (A = [4, 1, 4, 3, 3], X = [8, 10, 11, 13, 100]) = 4
print("A = [4, 1, 4, 3, 3], X = [8, 10, 11, 13, 100], the maximum number of different cities that Tom can visit is", str(refueling(A = [4, 1, 4, 3, 3], X = [8, 10, 11, 13, 100])))
# (A = [0, 10, 0], X = [1, 2, 3]) = 3
print("A = [0, 10, 0], X = [1, 2, 3], the maximum number of different cities that Tom can visit is", str(refueling(A = [0, 10, 0], X = [1, 2, 3])))
# (A = [0, 1, 0, 1, 1, 1, 0], X = [1, 2, 3, 4, 5, 6, 7]) = 4
print("A = [0, 1, 0, 1, 1, 1, 0], X = [1, 2, 3, 4, 5, 6, 7], the maximum number of different cities that Tom can visit is", str(refueling(A = [0, 1, 0, 1, 1, 1, 0], X = [1, 2, 3, 4, 5, 6, 7])))



