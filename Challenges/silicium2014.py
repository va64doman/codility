# Silicium 2014
# CuttingTheCake: Find the K-th piece of a cake in terms of size.
def cuttingTheCake(X, Y, K, A, B):
    N = len(A)
    width, height = calculateLengths(X,Y,A,B)
    width.sort()
    height.sort()
    beg = 1
    end = width[N] * height[N]
    result = 0
    while beg <= end:
        mid = (beg + end) // 2
        if greaterEq(X, Y, mid, width, height) >= K:
            beg = mid + 1
            result = mid
        else:
            end = mid - 1
    return result
    pass

def calculateLengths(X, Y, A, B):
    N = len(A)
    width = [0] * (N + 1)
    width[0] = A[0]
    for i in range(1, N):
        width[i] = A[i] - A[i-1]
    width[N] = X - A[N-1]
    height = [0] * (N + 1)
    height[0] = B[0]
    for i in range(1, N):
        height[i] = B[i] - B[i-1]
    height[N] = Y - B[N-1]
    return width, height
    pass

def greaterEq(X, Y, mid, width, height):
    N = len(width)
    result = 0
    j = N - 1
    for i in range(N):
        while j >= 0 and width[i] * height[j] >= mid:
            j -= 1
        result += N - 1 - j
    return result
    pass

# (X = 6, Y = 7, K = 3, A = [1,3], B = [1,5]) = 6
print("X = 6, Y = 7, K = 3, A = [1,3], B = [1,5], the K-th piece of a cake in terms of size is", str(cuttingTheCake(X = 6, Y = 7, K = 3, A = [1,3], B = [1,5])))