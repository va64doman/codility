#TreeProduct: Remove at most two edges from a tree graph to maximize the product of the components' sizes.
def setUnion(a, b):
    return set(a).union(set(b))
    pass

def setIntersection(a, b):
    return set(a) & set(b)
    pass

def setDifference(a, b):
    diff1 = set(a).difference(set(b))
    diff2 = set(b).difference(set(a))
    return diff1.union(diff2)
    pass

def highestDegree(A, B):
    N = len(A)
    dictionary = {}
    def addElt(dic, n0, n1):
        if n0 not in dic:
            dic[n0] = {n1}
        else:
            dic[n0].add(n1)
        pass
    for i in range(N):
        n0 = A[i]
        n1 = B[i]
        addElt(dictionary, n0, n1)
        addElt(dictionary, n1, n0)
    res = None
    maxDegree = 0
    for node, (curNode, curNodeNeighbourhood) in enumerate(dictionary.items()):
        currentDegree = len(curNodeNeighbourhood)
        if maxDegree < currentDegree:
            maxDegree = currentDegree
            res = int(node)
    return [res, N, dictionary]
    pass

def graphFromNode(rootNode, dic):
    graph = {}
    rootNeighbourhood = dic[rootNode]
    for node in rootNeighbourhood:
        graph[node] = {node}
    for node, (kNode, curNeighbourhood) in enumerate(graph.items()):
        seedNode = int(kNode)
        nodeToVisited = [seedNode]
        alreadyVisited = set()
        while len(nodeToVisited) != 0:
            curNode = nodeToVisited[0]
            if len(nodeToVisited) < 2:
                nodeToVisited = []
            else:
                nodeToVisited = nodeToVisited[1:]
            accessibleNode = dic[curNode]
            for node in accessibleNode:
                if node != rootNode and node not in alreadyVisited:
                    curNeighbourhood.add(node)
                    nodeToVisited.append(node)
            alreadyVisited.add(curNode)            
    return graph
    pass

def cut1Bridge(A, B, graphsFromNode):
    maxProd = 0
    for i in range(len(A)):
        nCut0 = A[i]
        nCut1 = B[i]
        curGraph = graphsFromNode[nCut0]
        comp0Size = 1
        for node, (kNode, neighbourhood) in enumerate(curGraph.items()):
            iNode = int(kNode)
            if iNode != nCut1:
                comp0Size += len(curGraph[kNode])
        comp1Size = len(curGraph[nCut1])
        prod = comp0Size * comp1Size
        if maxProd < prod:
            maxProd = prod
    return maxProd
    pass

def cut2Bridge(A, B, graphsFromNode):
    maxProd = 0
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            nCut00 = A[i]
            nCut01 = B[i]
            nCut10 = A[j]
            nCut11 = B[j]
            curGraph0 = graphsFromNode[nCut00]
            curGraph1 = graphsFromNode[nCut10]
            setNCut00 = {nCut00}
            for node, (kNode, neighbourhood) in enumerate(curGraph0.items()):
                iNode = int(kNode)
                if iNode != nCut01:
                    setNCut00 = setUnion(setNCut00, curGraph0[kNode])
            setNCut01 = curGraph0[nCut01]
            setNCut10 = {nCut10}
            for node, (kNode, neighbourhood) in enumerate(curGraph1.items()):
                iNode = int(kNode)
                if iNode != nCut11:
                    setNCut10 = setUnion(setNCut10, curGraph1[kNode])
            setNCut11 = curGraph1[nCut11]
            electedSet0 = None
            electedSet1 = None
            comp0Size = 0
            comp1Size = 0
            if nCut10 in setNCut00 and nCut11 in setNCut00:
                electedSet0 = setNCut00
                comp0Size = len(setNCut01)
            else:
                electedSet0 =setNCut01
                comp0Size = len(setNCut00)
            if nCut00 in setNCut10 and nCut01 in setNCut10:
                electedSet1 = setNCut10
                comp1Size = len(setNCut11)
            else:
                electedSet1 = setNCut11
                comp1Size = len(setNCut10)
            intersectionSet = setIntersection(electedSet0, electedSet1)
            comp2Size = len(intersectionSet)
            prod = comp0Size * comp1Size * comp2Size
            if maxProd < prod:
                maxProd = prod
    return maxProd
    pass

def treeProduct(A, B):
    # rootNode = the node with the highest degree
    # N = the number of nodes
    # dictionary = the graph connection using A and B (A -> B)
    [rootNode, N, dictionary] = highestDegree(A,B)
    if N < 3:
        res = N + 1
        return res
    # Fix graphFromNode
    graph = graphFromNode(rootNode, dictionary)
    # Don't cut bridge
    case0Prod = 0
    for node, (curNode, curNeighbourhood) in enumerate(graph.items()):
        case0Prod += len(curNeighbourhood)
    case0Prod += 1
    maxProd = case0Prod
    # Cut 1 bridge
    graphsFromNode = {}
    for node in range(N + 1):
        graphsFromNode[node] = graphFromNode(node, dictionary)
    prodCut1 = cut1Bridge(A, B, graphsFromNode)
    if maxProd < prodCut1:
        maxProd = prodCut1
    # Cut 2 bridge
    prodCut2 = cut2Bridge(A, B, graphsFromNode)
    if maxProd < prodCut2:
        maxProd = prodCut2
    return maxProd
    pass

#(A = [0,1,1,3,3,6,7], B = [1,2,3,4,5,3,5]) = 18
#(A = [0,1], B = [1,2]) = 3

print("A = [0,1,1,3,3,6,7], B = [1,2,3,4,5,3,5], the maximum product to remove at most two posts is", str(treeProduct(A = [0,1,1,3,3,6,7], B = [1,2,3,4,5,3,5])))
print("A = [0,1], B = [1,2], the maximum product to remove at most two posts is", str(treeProduct(A = [0,1], B = [1,2])))
