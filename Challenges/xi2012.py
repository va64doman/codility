# Xi 2012
# KSparseBinaryCount: Count ints with each two consecutive 1s (in a binary representation) separated by at least K 0s.

MODULO = 1000000007
F = []

def kSparseBinaryCount(S, T, K):
    sparseBinaryCount(len(T) + 1, K)
    return subtractMod(below(increase(T), K), below(S, K))
    pass

def sparseBinaryCount(length, K):
    global F
    F = [0] * length
    F[0] = 1
    for i in range(1, length):
        if i > K:
            F[i] = addMod(F[i - 1], F[i - K - 1])
        else:
            F[i] = addMod(F[i - 1], 1)
    pass

def addMod(a, b):
    return (a + b) % MODULO
    pass

def subtractMod(a, b):
    return addMod(a, -b + MODULO)
    pass

def increase(s):
    s = '0' + s
    lastZeroIndex = s.rindex('0')
    return s[0:lastZeroIndex] + '1' + repeatChars('0', len(s) - lastZeroIndex - 1)
    pass

def repeatChars(ch, times):
    return ch * times
    pass

def below(N, K):
    N = '0' + N
    kSparse = True
    countZero = K + 1
    j = 0
    for i in range(len(N)):
        if N[i] == '1':
            if countZero < K:
                kSparse = False
                break
            elif countZero > K:
                j = i
            countZero = 0
        else:
            countZero += 1
    if not kSparse:
        N = N[0:j - 1] + '1' + repeatChars('0', len(N) - j)
    return belowKSparse(N, K)
    pass

def belowKSparse(N, K):
    global F
    result = 0
    for i in range(len(N)):
        if N[i] == '1':
            result = addMod(result, F[len(N) - i - 1])
    return result
    pass

# (S = "101", T = "1111", K = 2) = 2
print("S = 101, T = 1111, K = 2, the number of ints with each 2 consecutive 1s separated by at least 2 0s is",
str(kSparseBinaryCount(S = "101", T = "1111", K = 2)))