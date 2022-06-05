#CountTriangles: Count the number of triangles that can be built from a given set of edges.
def countTri(A):
    """Solution method implementation."""
    # initialize vars
    list_len, srt = len(A), sorted(A)
    result = 0
    # main loop
    for i in range(list_len - 1, 0, -1):
        # caterpillar (re)defining
        back, front = 0, i - 1
        # caterpillar shrinking loop
        while back < front:
            if srt[back] + srt[front] > srt[i]:
                result += front - back
                front -= 1
            else:
                back += 1
    return result
    pass

# [10,2,5,1,8,12] = 4
print("[10,2,5,1,8,12], the number of triangles by the given set of edges is", str(countTri([10,2,5,1,8,12])))
