# Alpha 2010
# PrefixSet: Given a table A of N integers from 0 to N-1 calculate the smallest such index P, that that {A[0],...,A[N-1]} = {A[0],...,A[P]}.

def prefixSet(A):
    result = -1
    n = len(A)
    occur = [False] * n
    for i in range(n):
        if occur[A[i]] == False:
            occur[A[i]] = True
            result = i
    return result
    pass


# [2,2,1,0,1] = 3
print("[2,2,1,0,1], the smallest such index P, that that {A[0],...,A[N-1]} = {A[0],...,A[P]}, is", str(prefixSet([2,2,1,0,1])))