#CountDiv: Compute number of integers divisible by k in range [a..b].
def countDiv(A,B,K):
    c = int(B/K) - int(A/K)
    if A % K == 0:
        c += 1
    return c
    pass

# (A = 6, B = 11, K = 2) = 3
print("[6..11], the number of integers divisible by 2 is " + str(countDiv(6,11,2)))
