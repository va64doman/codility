#DiamondsCount: Given points on a plane, count the number of sets of four points that form regular diamonds.
from itertools import combinations

def diamondsCount(X, Y):
    l = len(X)
    
    points = []
    for i in range(l):
        points.append((X[i], Y[i]))

    by_mean_x = {}
    by_mean_y = {}
        
    for pair in combinations(points, 2):
        # compute mean_x and mean_y
        # if the pair items have the same x's or same y's then add them to a dict for those
        if pair[0][1] == pair[1][1]:
            mean_x = (pair[0][0] + pair[1][0])/2
            imean_x = int(mean_x)
            if mean_x != pair[0][0] and mean_x == imean_x:
                if imean_x not in by_mean_x:
                    by_mean_x[imean_x] = {}
                xp_y = pair[0][1]
                if xp_y not in by_mean_x[imean_x]:
                    by_mean_x[imean_x][xp_y] = 1
                else:
                    by_mean_x[imean_x][xp_y] += 1
        elif pair[0][0] == pair[1][0]:
            mean_y = (pair[0][1] + pair[1][1])/2
            imean_y = int(mean_y)
            if mean_y != pair[0][1] and mean_y == imean_y:
                if imean_y not in by_mean_y:
                    by_mean_y[imean_y] = {}
                yp_x = pair[0][0]
                if yp_x not in by_mean_y[imean_y]:
                    by_mean_y[imean_y][yp_x] = 1
                else:
                    by_mean_y[imean_y][yp_x] += 1

    d = 0

    for y in by_mean_y:
        for x in by_mean_y[y]:
            if x in by_mean_x and y in by_mean_x[x]:
                d += by_mean_x[x][y] * by_mean_y[y][x]

    return d
    pass

#(X = [1, 1, 2, 2, 2, 3, 3] and Y = [3, 4, 1, 3, 5, 3, 4]) = 2
print("(X = [1, 1, 2, 2, 2, 3, 3] and Y = [3, 4, 1, 3, 5, 3, 4]), the number of sets of 4 points that form regular diamonds:",
      str(diamondsCount(X = [1, 1, 2, 2, 2, 3, 3], Y = [3, 4, 1, 3, 5, 3, 4])))
#(X = [1, 2, 3, 3, 2, 1] and Y = [1, 1, 1, 2, 2, 2]) = 0
print("(X = [1, 2, 3, 3, 2, 1], Y = [1, 1, 1, 2, 2, 2]), the number of sets of 4 points that form regular diamonds:",
      str(diamondsCount(X = [1, 2, 3, 3, 2, 1], Y = [1, 1, 1, 2, 2, 2])))
