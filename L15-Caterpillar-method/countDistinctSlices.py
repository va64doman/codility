#CountDistinctSlices: Count the number of distinct slices (containing only unique numbers).
def countDistSlices(M, A):
    """Solution method implementation."""
    # initializing
    list_len = len(A)
    result, front, back = 0, 0, 0
    visited = [False] * (M + 1)
    # main processing loop
    while back < list_len:
        # advance front, update visited and result
        if front < list_len and not visited[A[front]]:
            result += front - back + 1
            visited[A[front]] = True
            front += 1
        # advance back and update visited
        else:
            visited[A[back]] = False
            back += 1
        if result > 1000000000:
            return 1000000000
    return result
    pass

#(M = 6, A = [3,4,5,5,2]) = 9
print("M = 6, A = [3,4,5,5,2], the number of distinct slices is", str(countDistSlices(6, [3,4,5,5,2])))
