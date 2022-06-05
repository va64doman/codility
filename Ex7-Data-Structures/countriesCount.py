#CountriesCount:Count the number of different countries that a map contains.
def countriesCount(A):
    M = len(A)
    N = len(A[0])
    countries = 0;
    for i in range(M):
        for j in range(N):
            neighbors = findNeighbours(A, i, j)
            currentValue = A[i][j]
            if neighbors[1] == currentValue and neighbors[2] == currentValue and neighbors[0] != currentValue:
                countries -= 1
            if neighbors[1] != currentValue and neighbors[2] != currentValue:
                countries += 1
    return countries
    pass

def isSafeMove(x,y):
    return x >= 0 and y >= 0
    pass

def findNeighbours(A,x,y):
    # Movement
    row = [-1,-1,0]
    col = [-1,0,-1]
    neighbours = [-1] * 3
    for i in range(len(neighbours)):
        if isSafeMove(x + row[i], y + col[i]):
            neighbours[i] = A[x + row[i]][y + col[i]]
    return neighbours
                
"""
(A) Row x column

5,4,4
4,3,4
3,2,4
2,2,2
3,3,4
1,4,4
4,1,1

returns 11

"""

A = [[5,4,4],[4,3,4],[3,2,4],[2,2,2],[3,3,4],[1,4,4],[4,1,1]]
print("[[5,4,4],[4,3,4],[3,2,4],[2,2,2],[3,3,4],[1,4,4],[4,1,1]], the number of different countries is", str(countriesCount(A)))
