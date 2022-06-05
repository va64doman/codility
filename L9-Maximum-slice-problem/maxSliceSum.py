#MaxSliceSum: Find a maximum sum of a compact subsequence of array elements.
def maxSliceSum(A):
    m = A[0]
    s = 0
    for i in range(0, len(A)):
        s += A[i]
        m = max(m,s)
        if s < 0:
            s = 0
    return m
    pass

#[3,2,-6,4,0] = 5
print("[3,2,-6,4,0], the maximum sum of slice is", str(maxSliceSum([3,2,-6,4,0])))
