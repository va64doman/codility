#FloodDepth: Find the maximum depth of water in mountains after a huge rainfall.
def floodDepth(A):
    left = [0] * len(A)
    right = [0] * len(A)
    leftHeight = rightHeight = 0
    for i in range(len(A)):
        leftHeight = max(leftHeight, A[i])
        left[i] = leftHeight
        rightHeight = max(rightHeight, A[len(A) - 1 - i])
        right[len(A) - 1 - i] = rightHeight
    maxDepth = 0
    for i in range(len(A)):
        depth = min(left[i], right[i]) - A[i]
        maxDepth = max(maxDepth, depth)
    return maxDepth
    pass

# [1,3,2,1,2,1,5,3,3,4,2] = 2
print("[1,3,2,1,2,1,5,3,3,4,2], max depth is", str(floodDepth([1,3,2,1,2,1,5,3,3,4,2])))
# [5,8] = 0
print("[5,8], max depth is", str(floodDepth([5,8])))
