#Distinct: Compute number of distinct values in an array.
def distinct(A):
    # Non-ordered containers where each element are unique.
    A = set(A)
    return len(A)
    pass

#[2,1,1,2,3,1] = 3
print("[2,1,1,2,3,1], there are " + str(distinct([2,1,1,2,3,1])) + " distinct values.")
