# Hydrogenium 2013
# GroceryStore: Find the shortest path in a weighted graph
def groceryStore(A,B,C,D):
    MAXINT = 10**9
    M = len(A)
    N = len(D)
    G = [[]] * N
    for i in range(M):
        G[A[i]] = G[A[i]] + [(B[i], C[i])]
        G[B[i]] = G[B[i]] + [(A[i], C[i])]
    dist = [MAXINT] * N
    visit = [False] * N
    dist[0] = 0
    for k in range(N):
        s = MAXINT
        for j in range(N):
            if dist[j] < s and visit[j] == False:
                s = dist[j]
                i = j
            visit[i] = True
            if s <= D[i]:
                return s
            for (j,t) in G[i]:
                dist[j] = min(dist[j], s + t)
    return -1
    pass
# (A = [0,1,3,1,2,2], B = [1,2,2,3,0,1], C = [2,3,4,5,7,5], D = [-1,1,3,8]) = 7
print("A = [0,1,3,1,2,2], B = [1,2,2,3,0,1], C = [2,3,4,5,7,5], D = [-1,1,3,8], the shortest time to reach an open store is",
str(groceryStore(A = [0,1,3,1,2,2], B = [1,2,2,3,0,1], C = [2,3,4,5,7,5], D = [-1,1,3,8])))
# (A = [0], B = [1], C = [10], D = [-1,6,8]) = -1
print("A = [0], B = [1], C = [10], D = [-1,6,8], the shortest time to reach an open store is",
str(groceryStore(A = [0], B = [1], C = [10], D = [-1,6,8])))