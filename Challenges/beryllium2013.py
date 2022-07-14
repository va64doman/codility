# Beryllium 2013
# PrefixSuffixSet: Calculate the number of pairs (P, S) such that {A[0], ..., A[P]} = {A[S], ..., A[N-1]}.
"""
A prefix suffix set is a pair of indices (P, S) such that 0 <= P, S < N and such that:

every value that occurs in the sequence A[0], A[1], ..., A[P] also occurs in the sequence A[S], A[S + 1], ..., A[N − 1],

every value that occurs in the sequence A[S], A[S + 1], ..., A[N − 1] also occurs in the sequence A[0], A[1], ..., A[P].
"""
def prefixSuffixSet(A):
    first = {}
    last = {}
    N = len(A)
    answer = 0
    x = 0
    y = 0
    for i in range(N):
        last[A[i]] = i
    for i in range(N - 1, -1, -1):
        first[A[i]] = i
    print(str(last))
    i = -1
    j = N
    while True:
        i += 1
        p = last[A[i]]
        while j > p:
            j -= 1
            x = first[A[j]]
            while i < x:
                i += 1
                p = min(p, last[A[i]])
        x = i + 1
        while x < N and last[A[x]] >= j:
            x += 1
        y = j - 1
        while y >= 0 and first[A[y]] <= i:
            y -= 1
        answer += (x - i) * (j -y)
        if answer > 1000000000:
            return 1000000000
        if x >= N or y < 0:
            break
        i = x - 1
        j = y + 1
    return answer
    pass

# [3,5,7,3,3,5] = 14
print("[3,5,7,3,3,5], the number of pairs is", str(prefixSuffixSet([3,5,7,3,3,5])))