# Permcheck: Check whether array A is a permutation.
def permCheck(A):
    if len(A) == 0:
        return 0
    A.sort()
    for i in range(0, len(A)):
        if A[i] != (i+1):
            return 0
    return 1
    pass


#[4,1,3,2] = 1
#[4,1,3] = 0
print("[4,1,3,2] is " + str(permCheck([4,1,3,2])))
print("[4,1,3] is " + str(permCheck([4,1,3])))
