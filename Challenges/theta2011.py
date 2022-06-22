# Theta 2011
# GasStations: Calculate cheapest way of buying gas in order to drive along a highway.
def gasStations(D, P, T):
    N = len(D)
    x = 0
    r = 0
    ans = 0
    for i in range(N):
        if D[i] > T:
            return -1
    for i in range(N):
        r = max(D[i] - x, 0)
        l = T - D[i]
        k = 0
        j = i + 1
        while j < N and k < l:
            if P[j] < P[i]:
                break
            k += D[j]
            j += 1
        k = min(k, l)
        if x < D[i]:
            x = k
            r += x
        else:
            if k < x - D[i]:
                x = k
                r += x
            else:
                r += (k + D[i] - x)
                x = k
        ans += P[i] * r
        if ans > 1000000000:
            return -2
    return ans
    pass

# (D = [10,9,8], P = [2,1,3], T = 15) = 41
print("D = [10,9,8], P = [2,1,3], T = 15, the cheapest way to buy gas is", str(gasStations(D = [10,9,8], P = [2,1,3], T = 15)))