# Pi 2012
# ArrayClosestAscenders: For each element of an array of integers, find the closest larger element.
INF = 1000000123

def array_closest_ascenders(A):
    N = len(A)
    left = left_closest_ascenders(A)
    A.reverse()
    right = left_closest_ascenders(A)
    right.reverse()
    ret = [0] * N
    for I in range(N):
        ret[I] = min(left[I], right[I])
        if ret[I] == INF:
            ret[I] = 0
    return ret
    pass

def left_closest_ascenders(A):
    N = len(A)
    if (N == 0): return A
    ret = [0] * N
    stack = [0] * N
    stack_size = 0
    for I in range(N):
        while (stack_size > 0) and (A[stack[stack_size-1]] <= A[I]):
            stack_size -= 1
        if (stack_size == 0):
            ret[I] = INF
        else:
            ret[I] = I - stack[stack_size-1]
        stack[stack_size] = I
        stack_size += 1
    return ret
    pass
# [4,3,1,4,-1,2,1,5,7] = [7,1,1,4,1,2,1,1,0]
print("[4,3,1,4,-1,2,1,5,7], for each element, the closest larger element are", str(array_closest_ascenders([4,3,1,4,-1,2,1,5,7])))