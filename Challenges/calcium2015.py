# Calcium 2015
# SpeedCameras: Position speed cameras so as to minimize the lengths of unmonitored paths.

from collections import deque

def speedCameras(A, B, K):   
    left = 0
    right= min(len(A), 1800)
    result = float("inf")
    
    nodes = [None for i in range(len(A) + 1)]
    for i in range(len(nodes)):
        nodes[i] = Node(i)
    
    for i in range(len(A)):
        p = nodes[A[i]]
        q = nodes[B[i]]
        p.children.append(q)
        q.children.append(p)
        
    root = nodes[0]
    while(left <= right):
        maxLength = (right - left) // 2 + left;
        cameras = [0]
        visited = [False for i in range(len(A)+1)]
        minCamerasNeeded(root, maxLength, cameras, visited)
        if(cameras[0] > K): left = maxLength+1
        else:
            result = maxLength 
            right = maxLength -1
    return result
    pass
        
        

def minCamerasNeeded(root, maxLength, cameras, visited):
    visited[root.id] = True
    children = root.children
    if(len(children) == 0): return 0
    
    valid = deque()
    for child in children:
        if visited[child.id]: continue
        result = minCamerasNeeded(child, maxLength, cameras, visited)
        if result + 1 > maxLength: cameras[0] += 1
        else: valid.append(result+1)
    
    if len(valid)!= 0:
        head = valid.popleft()
        for x in valid:
            if head + x > maxLength:
                cameras[0] += 1
                head = min(head, x)
            else: head = max(head, x)
        return head
    else: return 0
    pass

class Node:
    id = 0
    children = None
    def __init__(self,id):
        self.id = id;
        self.children = deque()
        pass
    pass

# (A = [5,1,0,2,7,0,6,6,1], B = [1,0,7,4,2,6,8,3,9], K = 2) = 2
print("The minimum lengths of unmonitored paths is", str(speedCameras(A = [5,1,0,2,7,0,6,6,1], B = [1,0,7,4,2,6,8,3,9], K = 2)))
