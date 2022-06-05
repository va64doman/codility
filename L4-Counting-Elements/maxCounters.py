# Maxcounters: Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
def maxCounters(N, A):
    # Result list
    R = [0] * N
    # Maximum
    m = 0
    b = 0
    for i in range(0, len(A)):
        if A[i] <= N:
            # Increment the counter over the max of b or current counter by 1.
            R[A[i]-1] = max(b, R[A[i] - 1]) + 1
            m = max(m, R[A[i] - 1])
        else:
            b = m
    # If any result element is less than b, then reset to b.
    for i in range(0, len(R)):
        if R[i] < b:
            R[i] = b
    return R
    pass

# (N = [3,4,4,6,1,4,4], A = 5) = [3,2,2,4,2]
print("[3,4,4,6,1,4,4] where max counter is 5, the array is " + str(maxCounters(5, [3,4,4,6,1,4,4])))
