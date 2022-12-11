# Jurassic Code
# LargestBalancedRadius: Given a set of points on a plane, find the largest number of points that can be enclosed within a circle centered on the origin,
# such that the number of red points and green points inside it is equal.

def largestBalancedRadius(X, Y, colors):
    N = len(X)
    ans = 0
    tab = []
    for i in range(N):
        r2 = X[i]**2 + Y[i]**2
        tab.append((r2, colors[i] == 'R'))
    tab.sort()
    cnt = red = 0
    for i in range(N):
        cnt += 1
        red += tab[i][1]
        if red * 2 == cnt and (i == N-1 or tab[i][0] != tab[i+1][0]): ans = max(ans, cnt)
    return ans
    pass

# (X = [4, 0, 2, −2], Y = [4, 1, 2, −3], colors = "RGRR") = 2
print("X = [4, 0, 2, −2], Y = [4, 1, 2, −3], colors = ""RGRR"", ",
      "the maximum number of points inside a circle containing an equal number of red points and green points is",
      str(largestBalancedRadius(X = [4, 0, 2, -2], Y = [4, 1, 2, -3], colors = "RGRR")))
# (X = [1, 1, −1, −1], Y = [1, −1, 1, −1], colors = "RGRG") = 4
print("X = [1, 1, −1, −1], Y = [1, −1, 1, −1], colors = ""RGRG"", ",
      "the maximum number of points inside a circle containing an equal number of red points and green points is",
      str(largestBalancedRadius(X = [1, 1, -1, -1], Y = [1, -1, 1, -1], colors = "RGRG")))
# (X = [1, 0, 0], Y = [0, 1, −1], colors = "GGR") = 0
print("X = [1, 0, 0], Y = [0, 1, −1], colors = ""GGR"", the maximum number of points inside a circle containing an equal number of red points and green points is",
      str(largestBalancedRadius(X = [1, 0, 0], Y = [0, 1, -1], colors = "GGR")))
# (X = [5, −5, 5], Y = [1, −1, −3], colors = "GRG") = 2
print("X = [5, −5, 5], Y = [1, −1, −3], colors = ""GRG"", the maximum number of points inside a circle containing an equal number of red points and green points is",
      str(largestBalancedRadius(X = [5, -5, 5], Y = [1, -1, -3], colors = "GRG")))
# (X = [3000, −3000, 4100, −4100, −3000], Y = [5000, −5000, 4100, −4100, 5000], colors = "RRGRG") = 2
print("X = [3000, −3000, 4100, −4100, −3000], Y = [5000, −5000, 4100, −4100, 5000], colors = ""RRGRG"", ",
      "the maximum number of points inside a circle containing an equal number of red points and green points is",
      str(largestBalancedRadius(X = [3000, -3000, 4100, -4100, -3000], Y = [5000, -5000, 4100, -4100, 5000], colors = "RRGRG")))
