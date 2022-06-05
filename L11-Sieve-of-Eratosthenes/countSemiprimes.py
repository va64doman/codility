#CountSemiprimes: Count the semiprime numbers in the given range [a..b]
def countSemiPrimes(N, P, Q):
    primes = [1] * (N + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(N**0.5) + 1):
        if primes[i]:
            k = i * i
            while k <= N:
                primes[k] = 0
                k += i
    allsemiprimes = [0] * (N + 1)
    for i in range(0, N + 1):
        for j in range(0, N + 1):
            if primes[i] and primes[j] and i * j <= N:
                allsemiprimes[i * j] = 1
            if i * j > N:
                break
    semiprimes = [0] * len(P)
    semiprimescum = [0] * (N + 1)
    s = 0

    for i in range(0, N + 1):
        s += allsemiprimes[i]
        semiprimescum[i] = s
    for i in range(0, len(P)):
        semiprimes[i] = semiprimescum[Q[i]] - semiprimescum[P[i] - 1]
    return semiprimes
    pass

# (N = 26, P = [1,4,16], Q = [26,10,20]) = [10,4,0]
print("(N = 26, P = [1,4,16], Q = [26,10,20]), the number of semiprimes each are", str(countSemiPrimes(26, [1,4,16], [26,10,20])))
