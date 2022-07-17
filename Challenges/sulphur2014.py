# Sulphur 2014
# BreakTheRope: Find the maximum number of ropes that can be attached in order, without breaking any of the ropes.
def breakTheRope(A, B, C):
    max = 0;
    if len(A) == 0:
        return max    
    left = 0
    right = len(A) - 1
    nodes = [[] for i in range(len(A) + 1)] 
    for i in range(0, len(C), 1): 
        parent = C[i]
        children = nodes[parent + 1]
        children.append(i + 1)
    while (left <= right):
        mid = (right - left) // 2 + left;
        if isValid(mid, A, B, nodes):
            max = mid + 1
            left = mid + 1
        else:
            right = mid - 1  
    return max
    pass
 

def isValid(lastIndex, A, B, nodes):
    sum = getSumStack(lastIndex +1, A, B, nodes)
    return sum != -1
    pass

def getSumStack(last, A, B, nodes):
    visited = [False for i in range(len(A) + 1)]
    total = [0 for i in range(len(A) + 1)] 
    stack = []
    stack.append(0)
    while(len(stack) != 0):
        current = stack.pop()
        if (visited[current] == False):
            visited[current] = True
            stack.append(current)
            children = nodes[current]
            for child in children:
                if(child > last):
                    break;
                stack.append(child)           
        else:
            if (current == 0):
                pass
            else:
                total[current] = B[current - 1]
                children = nodes[current]
                for child in children:
                    if(child > last):
                        break
                    if(total[child] == -1):
                        return -1
                    total[current] += total[child]                
                if(total[current] > A[current - 1]):
                    return -1
    pass

# (A = [5,3,6,3,3], B = [2,3,1,1,2], C = [-1,0,-1,0,3]) = 3
print("A = [5,3,6,3,3], B = [2,3,1,1,2], C = [-1,0,-1,0,3], the maximum number of ropes without breaking is", 
str(breakTheRope(A = [5,3,6,3,3], B = [2,3,1,1,2], C = [-1,0,-1,0,3])))