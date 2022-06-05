# Tape equilibrium: Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
def tapeEq(A):
    if len(A) < 2:
        return 0
    # Sum of all array elements
    s = sum(A)
    # Each element range from -1000 to 1000
    minDiff = 2000
    # Sum of left sum, do not need to recalculate the right sum of the array
    sL = 0
    for i in range(0, len(A)-1):
        sL += A[i]
        diff = abs(2 * sL - s)
        # Check if the current difference is less than the minimum difference.
        minDiff = min(diff, minDiff)
    return minDiff
    pass

#[3,1,2,4,3] = 1
print("Tape [3,1,2,4,3], the tape equilibrium is " + str(tapeEq([3,1,2,4,3])))
