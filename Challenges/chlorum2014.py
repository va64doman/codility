# Chlorum 2014
# TreeTrip: Given a network of cities, plan a trip to the most attractive ones.

import functools

class City:
    def __init__(self, id, a):
        self.id = id
        self.a = a
        self.max = a
        self.parent = None
        self.children = []
        pass
    pass

class PriorityQueue:
    def __init__(self):
        self.queue = []
        pass

    def add(self, val):
        self.queue.append(val)
        sorted(self.queue, key=functools.cmp_to_key(compare))
        pass

    def remove(self):
        val = self.queue[0]
        self.queue = self.queue[1:]
        return val
        pass

    def peek(self):
        return self.queue[0]
        pass

    def isEmpty(self):
        return len(self.queue) == 0
        pass
    pass

def compare(arg0, arg1):
    if arg1.a != arg0.a: return arg1.a - arg0.a
    else: return arg1.max - arg0.max
    pass

def largestCluster1(maxValue, cityMap):
    largest = None
    visited = [False for i in range(len(cityMap))]
    maxSize = 0
    for i in range(len(cityMap)):
        current = cityMap[i]
        if not visited[current.id] and current.a == maxValue:
            size = largestCluster2(maxValue, current, visited)
            if size > maxSize:
                maxSize = size
                largest = current
    return largest
    pass

def largestCluster2(maxValue, current, visited):
    visited[current.id] = True
    count = 1
    if current.a != maxValue: return 0
    children = current.children
    for city in children:
        if not visited[city.id]: count += largestCluster2(maxValue, city, visited)
    return count
    pass

def find(X, included, explored, unexplored, maximum):
    minimum = X.a
    count = 1
    if count > maximum: return -1
    needed = []
    included[X.id] = True
    needed.append(X)
    while unexplored.isEmpty() and unexplored.peek().a > minimum:
        current = unexplored.remove()
        while not included[current.id]:
            included[current.id] = True
            needed.append(current)
            current = current.parent
            minimum = min(minimum, current.a)
            count += 1
            if count > maximum: return -1
    for c in needed:
        children = c.children
        for child in children:
            if not included[child.id]: explored.add(child)
    return count
    pass

def buildTree1(root, visited):
    stack = []
    stack.append(root)
    while stack:
        if visited[stack[-1].id]:
            current = stack.pop()
            for city in current.children:
                if city != current.parent: current.max = max(current.max, city.max)
        else:
            current = stack[-1]
            visited[current.id] = True
            for city in current.children:
                if visited[city.id] == False:
                    city.parent = current
                    stack.append(city)
    pass

def buildTree2(root, parent, visited):
    visited[current.id] = True
    current.parent = parent
    maximum = current.a
    children = current.children
    for child in children:
        if not visited[child.id]:
            a = buildTree2(child, current, visited)
            maximum = max(maximum, a)
    current.max = maximum
    return maximum
    pass

def treeTrip(K, C, D):
    cityMap = [None for i in range(len(C))]
    explored = PriorityQueue()
    unexplored = PriorityQueue()
    maxCity = None
    for i in range(len(C)):
        if cityMap[i] == None:
            cityMap[i] = City(i, D[i])
            if maxCity == None: maxCity = cityMap[i]
            else: maxCity = cityMap[i] if cityMap[i].a > maxCity.a else maxCity
        if C[i] == i: continue
        if cityMap[C[i]] == None:
            cityMap[C[i]] = City(C[i], D[C[i]])
            if maxCity == None: maxCity = cityMap[C[i]]
            else: maxCity = cityMap[C[i]] if cityMap[C[i]].a > maxCity.a else maxCity
        cityMap[i].children.append(cityMap[C[i]])
        cityMap[C[i]].children.append(cityMap[i])
    largest = largestCluster1(maxCity.a, cityMap)
    buildTree1(largest, [False for i in range(len(C))])
    count = 0
    included = [False for i in range(len(C))]
    for c in cityMap:
        unexplored.add(c)
    explored.add(largest)
    while not explored.isEmpty():
        current = explored.remove()
        if included[current.id]: continue
        result = find(current, included, explored, unexplored, K - count)
        if result == -1: break
        else: count += result
    return count
    pass
 
# (K = 2, C = [1,3,0,3,2,4,4], D = [6,2,7,5,6,5,2]) = 2
print("K = 2, C = [1,3,0,3,2,4,4], D = [6,2,7,5,6,5,2], the maximum number of cities that can be included in a valid trip plan is",
str(treeTrip(K = 2, C = [1,3,0,3,2,4,4], D = [6,2,7,5,6,5,2])))
# TODO: This is a problem where the return result is 5 and not 4.
# (K = 5, C = [1,3,0,3,2,4,4], D = [6,2,7,5,6,5,2]) = 4
print("K = 5, C = [1,3,0,3,2,4,4], D = [6,2,7,5,6,5,2], the maximum number of cities that can be included in a valid trip plan is",
str(treeTrip(K = 5, C = [1,3,0,3,2,4,4], D = [6,2,7,5,6,5,2])))

