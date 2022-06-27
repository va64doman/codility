# Eta 2011
# HamiltonianRoutesCount: Check whether a given sequence is a valid traversal of some ternary undirected tree.

def hamiltonianRoutesCount(A):
    hamRoutesCnt = 3
    N = len(A)
    M = (N // 2) + 1
    townsOccur = [0] * M
    roadsTaken = [0] * M
    for i in range(M):
        roadsTaken[i] = [0] * 3
    i = 0
    while i < N and hamRoutesCnt == 3:
        townsOccur[A[i]] += 1
        roadBegin = A[i]
        roadDest = A[(i + 1) % N]
        if roadBegin == roadDest:
            hamRoutesCnt = -2
        else:
            if roadBegin > roadDest:
                roadBegin = roadDest
                roadDest = A[i]
            for j in range(3):
                if roadsTaken[roadBegin][j] == 0:
                    roadsTaken[roadBegin][j] = roadDest
                elif roadsTaken[roadBegin][j] == roadDest:
                    roadsTaken[roadBegin][j] = -roadDest
                elif roadsTaken[roadBegin][j] == -roadDest:
                    hamRoutesCnt = -2
                    break
        i += 1
    i = 0
    if hamRoutesCnt == 3:
        for i in range(M):
            if townsOccur[i] != 1 and townsOccur[i] != 3:
                hamRoutesCnt = -2
                break
            for j in range(3):
                if roadsTaken[i][j] > 0:
                    hamRoutesCnt = -2
                    break
    return hamRoutesCnt
    pass

# [4,0,4,3,4,1,5,1,7,6,7,2,7,1] = 3
cnt = hamiltonianRoutesCount([4,0,4,3,4,1,5,1,7,6,7,2,7,1])
print("[4,0,4,3,4,1,5,1,7,6,7,2,7,1], the number of hamiltonian routes:", "violated" if cnt == -2 else "over 100,000,000" if cnt == -1 else str(cnt))
# [4,4,0,3,4,1,5,1,7,6,7,2,7,1] = -2
cnt = hamiltonianRoutesCount([4,4,0,3,4,1,5,1,7,6,7,2,7,1])
print("[4,4,0,3,4,1,5,1,7,6,7,2,7,1], the number of hamiltonian routes:", "violated" if cnt == -2 else "over 100,000,000" if cnt == -1 else str(cnt))
# [3,6,3,1,5,1,0,1,3,7,3,2,3,4] = -2
cnt = hamiltonianRoutesCount([3,6,3,1,5,1,0,1,3,7,3,2,3,4])
print("[3,6,3,1,5,1,0,1,3,7,3,2,3,4], the number of hamiltonian routes:", "violated" if cnt == -2 else "over 100,000,000" if cnt == -1 else str(cnt))
# [4,0,5,0,3,0,1,3,2,3] = -2
cnt = hamiltonianRoutesCount([4,0,5,0,3,0,1,3,2,3])
print("[4,0,5,0,3,0,1,3,2,3], the number of hamiltonian routes:", "violated" if cnt == -2 else "over 100,000,000" if cnt == -1 else str(cnt))
