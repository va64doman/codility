# PermMissingElem: Missing element in a given permutation
def permMissingElem(A):
    if(len(A) == 0):
        return 1
    A.sort()
    for i in range(0, len(A)):
        # If the current element is not the counting index, then the missing element is the counting index.
        if A[i] != i+1:
            return i + 1
    # If the given list is not missing, then the length of array is the missing element.
    return A[len(A) - 1] + 1
    pass

# [2,3,1,5] = 4
print("[2,3,1,5] the missing element is " + str(permMissingElem([2,3,1,5])))
