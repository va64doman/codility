# Mu 2011
# NumberOfZeros: Compute total number of zeros in decimal representation of 1, ...., N.
def numberOfZeros(S):
    P = 1410000017
    Z = 0
    N = 0
    F = 0
    for j in range(len(S)):
        F = (10 * F + N + P - Z * (9 - int(S[j])) ) % P
        if S[j] == '0':
            Z += 1
        N = (10 * N + int(S[j])) % P
    return ((1 + F) % P)
    pass

# 100 = 12
print("100, the number of zeros is", str(numberOfZeros("100")))
# 219 = 42
print("219, the number of zeros is", str(numberOfZeros("219")))