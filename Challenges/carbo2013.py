# Carbo 2013
# PrefixMaxProduct: Find the maximal product of string prefixes.
def prefixMaxProduct(S):
    N = len(S)
    p = [0] * N
    num = [0] * (N + 1)
    num[N] = 1
    left = right = -1
    for i in range(1, N):
        if right < i:
            j = 0
            while i + j < N and S[j] == S[j + i]:
                j += 1
            if j:
                p[i] = j
                left = i
                right = i + j - 1
        elif right - i < p[i- left]:
            j = right + 1
            while j < N and S[j] == S[j - i]:
                j += 1
            p[i] = j - i
            left = i
            right = j - 1
        else: p[i] = p[i - left]
        num[p[i]] += 1
    total = answer = 0
    i = N
    while i:
        total += num[i]
        if total  > 1000000000 // i: return 1000000000
        answer = max(answer, total * i)
        i -= 1
    return answer
    pass
# abababa = 10
print("abababa, the maximal product of string prefixes is", str(prefixMaxProduct("abababa")))
# aaa = 4
print("aaa, the maximal product of string prefixes is", str(prefixMaxProduct("aaa")))