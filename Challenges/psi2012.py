# Psi 2012
# WireBurnouts: While removing edges from a mesh grid, find the moment when there ceases to be a connection between opposite corners.
def wireBurnouts(N, A, B, C):
    global vertices, rank
    M = len(A)
    vertices = [[(x,y) for y in range(N)] for x in range(N)]
    rank = [[0] * N] * N
    vEdges = [[True for y in range(N-1)] for x in range(N)]
    hEdges = [[True for y in range(N)] for x in range(N-1)]
    for i in range(M):
        if C[i] == 0:
            vEdges[A[i]][B[i]] = False
        else:
            hEdges[A[i]][B[i]] = False
    for i in range(N):
        for j in range(N):
            if i < N - 1 and hEdges[i][j]:
                union((i,j), (i+1,j))
            if j < N - 1 and vEdges[i][j]:
                union((i,j), (i, j+1))
    if find((0,0)) == find((N-1, N-1)):
        return -1
    for i in range(M-1, -1, -1):
        if C[i] == 0:
            union((A[i], B[i]), (A[i], B[i] + 1))
        else:
            union((A[i], B[i]), (A[i] + 1, B[i]))
        if find((0,0)) == find((N-1, N-1)):
            return i + 1
    return -1
    pass

def find(tup):
    (a,b) = tup
    global vertices, rank
    (c,d) = (a,b)
    while vertices[a][b] != (a,b):
        (a,b) = vertices[a][b]
    while vertices[c][d] != (a,b):
        (e,f) = vertices[c][d]
        vertices[c][d] = (a,b)
        (c,d) = (e,f)
    return (a,b)
    pass

def union(tup1, tup2):
    (a,b) = tup1
    (c,d) = tup2
    global vertices, rank
    (a,b) = find((a,b))
    (c,d) = find((c,d))
    if rank[a][b] < rank[c][d]:
        vertices[a][b] = vertices[c][d]
    else:
        vertices[c][d] = vertices[a][b]
        if rank[a][b] == rank[c][d]:
            rank[c][d] += 1
    pass
# (N = 4, A = [0,1,1,2,3,2,1,0,0], B = [0,1,1,1,2,2,3,1,0], C = [0,1,0,0,0,1,1,0,1]) = 8
print("N = 4, A = [0,1,1,2,3,2,1,0,0], B = [0,1,1,1,2,2,3,1,0], C = [0,1,0,0,0,1,1,0,1], the wire burnout is at position", 
str(wireBurnouts(N = 4, A = [0,1,1,2,3,2,1,0,0], B = [0,1,1,1,2,2,3,1,0], C = [0,1,0,0,0,1,1,0,1])))
# (N = 4, A = [0], B = [0], C = [0]) = -1
print("N = 4, A = [0], B = [0], C = [0], the wire burnout is at position", 
str(wireBurnouts(N = 4, A = [0], B = [0], C = [0])))