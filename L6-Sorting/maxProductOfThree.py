#MaxProductOfThree: Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).
def maxProductOfThree(A):
    A.sort()
    N = len(A)
    # If the first two sorted elements are negative, then it becomes positive and might have the max product using the largest element.
    P1 = A[N-1] * A[0] * A[1]
    # It could be the 3 largest element that contains the largest product.
    P2 = A[N-1] * A[N-2] * A[N-3]
    return max(P1, P2)
    pass

#[-3,1,2,-2,5,6] = 60
print("[-3,1,2,-2,5,6], the largest product of three is " + str(maxProductOfThree([-3,1,2,-2,5,6])))
