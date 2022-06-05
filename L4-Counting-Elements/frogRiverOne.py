# Frog River One: Find the earliest time when a frog can jump to the other side of a river.
def fro(X, A):
    B = [0] * X
    # Number of leaves
    s = 0
    for i in range(0,len(A)):
        # If there is no leaves at A[i] - 1 and if the position A[i] is before or at X.
        if(B[A[i] - 1] == 0 and A[i] <= X):
            # Increase the sum and mark the leaf at this position.
            s += 1
            B[A[i] - 1] = 1
        # If the number of leaves is X, then the earliest time is i.
        if(s == X):
            return i
    # If frog jumps is impossible.
    return -1
    pass

# (X = 5, A = [1,3,1,4,2,3,5,4]) = 6
print("Given the start is 0 and the bank is at 5, leaf at A[k] falls at k time. The earliest time the frog jump at " + str(fro(5, [1,2,1,4,2,3,5,4])))


