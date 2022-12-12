# National Coding Week 2022
# OddNetwork: Given a tree graph, find the number of pairs of vertices whose distance is odd.

maxLevel = 0
connected = None
Level = None

def updateLevel(fromNode, N, level):
    global maxLevel
    global connected
    global Level
    
    maxLevel = max(level, maxLevel)
    for i in range(len(connected[N])):
        c = connected[N][i]
        if c != fromNode: updateLevel(N, c, level + 1)
        else: Level[level] += 1
    pass

def oddNetwork(A, B):
    global maxLevel
    global connected
    global Level
        
    maxLevel = 0
    connected = None
    R = 0
    N = len(A) + 1
    connected = [[] for i in range(N)] * N
    Level = [0 for i in range(N)]
    for i in range(len(A)):
        a = A[i]
        b = B[i]
        connected[a].append(b)
        connected[b].append(a)
    Level[0] += 1
    updateLevel(-1, 0, 0)
    for i in range(maxLevel, 0, -1):
        for j in range(i-1, -1, -2): R += (Level[i] * Level[j])
    return R
    pass

# (A = [0,3,4,2,6,3], B = [3,1,3,3,3,5]) = 6
print("A = [0,3,4,2,6,3], B = [3,1,3,3,3,5], the number of pairs of nodes X and Y, such that 0 <= X < Y <= N, and X and Y are connected via an odd number of links is",
      str(oddNetwork(A = [0,3,4,2,6,3], B = [3,1,3,3,3,5])))
# (A = [0,4,2,2,4], B = [1,3,1,3,5]) = 9
print("A = [0,4,2,2,4], B = [1,3,1,3,5], the number of pairs of nodes X and Y, such that 0 <= X < Y <= N, and X and Y are connected via an odd number of links is",
      str(oddNetwork(A = [0,4,2,2,4], B = [1,3,1,3,5])))
# (A = [0,4,4,2,7,6,3], B = [3,5,1,3,4,3,4]) = 16
print("A = [0,4,4,2,7,6,3], B = [3,5,1,3,4,3,4], the number of pairs of nodes X and Y, such that 0 <= X < Y <= N, and X and Y are connected via an odd number of links is",
      str(oddNetwork(A = [0,4,4,2,7,6,3], B = [3,5,1,3,4,3,4])))
