# Fluorum 2014
# TripPlanning: Plan trips to destination cities so as to visit a maximal number of other unvisited cities en route.
import collections, queue

class Node:
    def __init__(self, id):
        self.id = id
        self.children = []
        pass
    pass

def tripPlanning(K, T):
    n = len(T)
    if n == 1:
        return [0]

    adj = [[] for i in range(n)]
    for a, b in enumerate(T):
        if a == b: continue
        adj[a].append(b)
        adj[b].append(a)
    
    # build the tree rooted at K
    nodes = [Node(i) for i in range(n)]
    q = collections.deque([K])
    visited = [0]*n
    while q:
        i = q.popleft()
        visited[i] = 1
        for j in adj[i]:
            if not visited[j]:
                nodes[i].children.append(nodes[j])
                q.append(j)
    
    # Find deepest leaf for every node
    # Note: the recursive version may cause stack overflow for large input
    findDeepestNonRecursive(nodes[K])

    # Cut the tree into forest along the longest path
    result = [K]
    q = queue.PriorityQueue()
    q.put((-nodes[K].cities, nodes[K].target, K))
    while q.qsize() > 0:
        c, target, i = q.get()
        result.append(target)
        splitTree(nodes[i], target, q)
        
    return result
    pass
        
def splitTree(root, target, q):
    while root:
        if root.id == target:
            return
        for child in root.children:
            if child.target != target:
                q.put((-child.cities, child.target, child.id))
            else:
                nextRoot = child
        root = nextRoot
    pass

def findDeepest(root):
    if not root.children:
        root.target = root.id
        root.cities = 1
        return

    target, cities = None, 0
    for child in root.children:
        findDeepest(child)
        if ((child.cities > cities) or 
            (child.cities == cities and child.target < target)):
            target, cities = child.target, child.cities
    root.target = target
    root.cities = cities + 1
    pass
    
def findDeepestNonRecursive(root):
    callStack = [root]
    resultStack = []
    while callStack:
        root = callStack.pop()
        resultStack.append(root)
        if not root.children:
            root.target = root.id
            root.cities = 1
        else:
            root.cities = 0
            for child in root.children:
                callStack.append(child)

    for node in reversed(resultStack):
        if node.cities > 0:
            continue
        target, cities = None, 0
        for child in node.children:
            if ((child.cities > cities) or 
                (child.cities == cities and child.target < target)):
                target, cities = child.target, child.cities
        node.target = target
        node.cities = cities + 1
    pass

# (K = 2, T = [1,2,3,3,2,1,4]) = [2, 0, 6, 3, 5]
print("K = 2, T = [1,2,3,3,2,1,4], the sequence of travel targets is", str(tripPlanning(K = 2, T = [1,2,3,3,2,1,4])))
