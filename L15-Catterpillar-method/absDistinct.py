#AbsDistinct: Compute number of distinct absolute values of sorted array elements.
def absDist(A):
    A = [a * a for a in A]
    A = list(set(A))
    return len(A)
    pass

#[-5,-3,-1,0,3,6] = 5
print("[-5,-3,-1,0,3,6], the number of distinct absolute values is", str(absDist([-5,-3,-1,0,3,6])))
