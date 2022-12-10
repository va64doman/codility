# Digital Gold
# DividingTheKingdom: In how many ways can you split a kingdom into two parts, so that the parts contain equal number of gold mines?

def dividingTheKingdom(N, M, X, Y):
    if len(X) % 2 != 0: return 0
    X.sort()
    Y.sort()
    left = X[len(X) // 2 - 1]
    right = X[len(X) // 2]
    resultX = right - left
    left = Y[len(Y) // 2 - 1]
    right = Y[len(Y) // 2]
    resultY = right - left
    return resultX + resultY
    pass

# (N = 5, M = 5, X = [0, 4, 2, 0], Y = [0, 0, 1, 4]) = 3
print("N = 5, M = 5, X = [0, 4, 2, 0], Y = [0, 0, 1, 4], the number of ways can be split a kingdom into two parts, so that the parts contain equal number of gold mines is",
      str(dividingTheKingdom(N = 5, M = 5, X = [0, 4, 2, 0], Y = [0, 0, 1, 4])))
