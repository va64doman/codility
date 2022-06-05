import math
#ParityDegree: Find the highest power of 2 that divides N.
def parityDegree(N):
    res = 0
    while N > 0:
        if N % 2 == 0:
            res += 1
            N /= 2
        else:
            break
    return res
    pass

#24 = 3 (2^3 = 8)
print("Highest power of 2 that divides 24 is", str(parityDegree(24)))
