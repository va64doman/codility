#MaxNonoverlappingSegments: Find a maximal set of non-overlapping segments.
def mnos(A, B):
    currentPos = -1
    segCount = 0
    for i in range(len(A)):
        if A[i] > currentPos:
            currentPos = B[i]
            segCount += 1
    return segCount
    pass

#(A = [1,3,7,9,9], B = [5,6,8,9,10]) = 3
print("A = [1,3,7,9,9], B = [5,6,8,9,10], the maximal set of non-overlapping segments is", str(mnos([1,3,7,9,9], [5,6,8,9,10])))
