# Yttrium 2019
# DifferentCharacters: Given a string, find the shortest substring that can be removed to yield a string that contains exactly K different characters.
def checkOutside(A):
    res = 0
    for i in range(26):
        if A[i] != 0:
            res += 1
    return res
    pass

def differentCharacters(S, K):
    N = len(S)
    if K==0: return N
    A = [0]*26
    for c in S:
        A[ord(c)-97] += 1
    if checkOutside(A) < K:
        return -1
    elif checkOutside(A)==K:
        return 0    
    res = N
    head, tail = -1, 0
    while head < N:
        temp = checkOutside(A) # temp >= K
        if temp==K:
            res = min(res, head-tail+1)
            c = S[tail]
            A[ord(c)-97] += 1
            tail += 1
        else: # temp > K
            head += 1
            if head==N: return res
            c = S[head]
            A[ord(c)-97] -= 1
    return res
    pass

# (S = "abaacbca", K = 2) = 3
print("S = ""abaacbca"", K = 2, the length of the shortest substring that can be removed to yield a string that contains exactly K different characters is",
      str(differentCharacters(S = "abaacbca", K = 2)))
# (S = "aabcabc", K = 1) = 5
print("S = ""aabcabc"", K = 1, the length of the shortest substring that can be removed to yield a string that contains exactly K different characters is",
      str(differentCharacters(S = "aabcabc", K = 1)))
# (S = "zaaaa", K = 1) = 1
print("S = ""zaaaa"", K = 1, the length of the shortest substring that can be removed to yield a string that contains exactly K different characters is",
      str(differentCharacters(S = "zaaaa", K = 1)))
# (S = "aaaa", K = 2) = -1
print("S = ""aaaa"", K = 2, the length of the shortest substring that can be removed to yield a string that contains exactly K different characters is",
      str(differentCharacters(S = "aaaa", K = 2)))
