# Phosphorus 2014
# PrisonEscape: Place the minimum number of guards needed to prevent prisoners from escaping.
SIZE = 200002
VISITED = [False] * SIZE
NODES = [None] * SIZE
ISPRISONER = [0] * SIZE
GUARDS = 0

class Node:
    def __init__(self):
        self.canEscapeRoot = False
        self.canEscapeLeaf = True
        self.neighbours = []
        pass
    pass

def prisonEscape(A, B, C):
    global GUARDS
    global VISITED
    global NODES

    for i in range(len(A) + 1):
        NODES[i] = Node()
    for i in range(len(A)):
        NODES[A[i]].neighbours.append(B[i])
        NODES[B[i]].neighbours.append(A[i])
    for i in range(len(C)):
        ISPRISONER[C[i]] = 1
        if len(NODES[C[i]].neighbours) == 1: return -1
    depthFirstSearch(0,0)
    if len(NODES[0].neighbours) == 1 and NODES[NODES[0].neighbours[0]].canEscapeRoot: GUARDS += 1
    return GUARDS
    pass

def depthFirstSearch(index, parent):
    global GUARDS
    global VISITED
    global NODES
    global ISPRISONER

    node = NODES[index]
    VISITED[index] = True
    N = 0
    escapeRoot = 0
    escapeLeaf = 0
    for i in range(len(node.neighbours)):
        if not VISITED[node.neighbours[i]]:
            depthFirstSearch(node.neighbours[i], index)
        if node.neighbours[i] != parent:
            N += 1
            if NODES[node.neighbours[i]].canEscapeRoot: escapeRoot += 1
            if NODES[node.neighbours[i]].canEscapeLeaf: escapeLeaf += 1
    if len(node.neighbours) == 1: return
    if ISPRISONER[index] == 1:
        node.canEscapeRoot = True
        node.canEscapeLeaf = False
        GUARDS += escapeLeaf
    else:
        if escapeLeaf == 0:
            node.canEscapeLeaf = False
            if escapeRoot > 0:
                node.canEscapeRoot = True
        elif escapeLeaf < N:
            if escapeRoot > 0:
                GUARDS += 1
                node.canEscapeLeaf = False
    pass

# (A = [0,1,2,3,3,2,6,6], B = [1,2,3,4,5,6,8,7], C = [1,6]) = 4
print("A = [0,1,2,3,3,2,6,6], B = [1,2,3,4,5,6,8,7], C = [1,6], the minimum number of guards is", 
str(prisonEscape(A = [0,1,2,3,3,2,6,6], B = [1,2,3,4,5,6,8,7], C = [1,6])))
