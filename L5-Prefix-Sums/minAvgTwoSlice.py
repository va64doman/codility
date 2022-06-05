#MinAvgTwoSlice: Find the minimal average of any slice containing at least two elements.
def minAvgTwoSlice(A):
    # Minimum value
    mn = max(A) * 2
    # Index of current slice
    mi = 0
    for i in range(0, len(A) - 2):
        # Calculate average for 3-element slice
        v1 = (A[i] + A[i+1] + A[i+2]) / 3
        # Calculate average for 2-element slice
        v2 = (A[i] + A[i+1]) / 2
        # Check if current minimum value is higher than v1 or v2
        if mn > v1 or mn > v2:
            # Replace minimum value by either v1 or v2
            mn = min(v1, v2)
            # Index of the starting minimum slice
            mi = i
    # Test to see if minimum value is higher than the last two element average, if so, the index of the starting min slice is the second-last index.
    if mn > (A[-1] + A[-2]) / 2:
        return len(A) - 2
    return mi
    pass

# [4,2,2,5,1,5,8] = 1
print("[4,2,2,5,1,5,8], the minimal average of any slice at least two elements is " + str(minAvgTwoSlice([4,2,2,5,1,5,8])))
