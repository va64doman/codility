# Odd occurences in array: Find element without a pair.
def ooia(A):
    # If there is only one element, then return this element.
    if len(A) == 1:
        return A[0]
    # Array sorted in ascending order.
    A.sort()
    # Group in pairs and check if there is a difference in pair.
    for i in range(0, len(A) - 1, 2):
        # If the two elements are different, then return the left element.
        if A[i] != A[i+1]:
            return A[i]
    # If the length of the array is even, then show that there is no odd occurences.
    # If reach to the end of the array and the length of array is odd, then the last element is odd occurence.
    if len(A) % 2 == 0:
        return -1
    else:
        return A[-1]
    pass

# [9,3,9,3,9,7,9] = 7
print("[9,3,9,3,9,7,9] odd occurences is " + str(ooia([9,3,9,3,9,7,9])))
