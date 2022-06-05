# Cyclic rotation : the end element must be at the start position.
def cycRot(A, K):
    # The length of the array.
    N = len(A)
    B = [None] * N
    # Check every elements in the array and all of the elements are in B but in different positions.
    for i in range(0, N):
        # Place the value from A to the new position of B based on the number of cyclic rotation to the left-right K times.
        B[(i + K) % N] = A[i]
    return B
    pass

# [3,8,9,7,6] * 3 cyclic rotations = [9,7,6,3,8]
# [0,0,0] * 1 cyclic rotation = [0,0,0]
# [1,2,3,4] * 4 cyclic rotation = [1,2,3,4]
print("[3,8,9,7,6] cyclic rotated 3 times: " + str(cycRot([3,8,9,7,6], 3)))
print("[0,0,0] cyclic rotated 1 times: " + str(cycRot([0,0,0], 1)))
print("[1,2,3,4] cyclic rotated 4 times: " + str(cycRot([1,2,3,4], 4)))
