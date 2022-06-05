#CommonPrimeDivisors: Check whether two numbers have the same prime divisors.
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
    pass

def commonPriDiv(A, B):
    length = len(A)
    cnt = 0
    for i in range(0,length):
        a = A[i]
        b = B[i]
        D = gcd(a, b)
        while gcd(a,D) != 1:
            a /= gcd(a, D)
        while gcd(b,D) != 1:
            b /= gcd(b, D)
        if a == 1 and b == 1:
            cnt += 1
    return cnt
    pass

# (A = [15,10,3], B = [75, 30, 5]) = 1
print("[15,10,3], [75,30,5]", "have", str(commonPriDiv([15,10,3], [75,30,5])),"same prime divisors.")
