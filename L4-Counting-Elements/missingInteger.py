# MissingInteger: Find the smallest positive integer that does not occur in a given sequence.
def missInt(A):
    A.sort()
    if A[len(A) - 1] <= 0:
        return 1
    # Check if there is any 1 in the array
    iso = False
    for i in range(0, len(A)):
        if A[i] == 1:
            iso = True
    if iso == False:
        return 1
    # Check if there is any missing integers between two elements.
    for i in range(0, len(A) - 1):
        # Get the smallest positive integer if it is missing.
        if A[i] > 0 and (A[i+1]-A[i]) > 1:
            return A[i] + 1
    # The last integer after the array is missing.
    return A[len(A) - 1] + 1
    pass


#[1, 3, 6, 4, 1, 2] = 5
#[1, 2, 3] = 4
#[−1, −3] = 1

print("[1,3,6,4,1,2] has missed " + str(missInt([1,3,6,4,1,2])))
print("[1,2,3] has missed " + str(missInt([1,2,3])))
print("[-1,-3] has missed " + str(missInt([-1,-3])))
