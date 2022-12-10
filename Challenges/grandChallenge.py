# Grand Challenge
# BalancedPassword: Given a string S, find the length of the longest balanced substring of S.

def getLongest(S):
    if not S:
        return 0        
    result = 0
    pivot = S[0]
    maps = {}
    cur = 0
    for i in range(len(S)):
        if S[i] == pivot:
            cur += 1
        else:
            cur -= 1        
        if cur in maps:
            result = max(result, i - maps[cur] + 1)        
        if S[i] == pivot and cur - 1 not in maps:
            maps[cur - 1] = i
        elif S[i] != pivot and cur + 1 not in maps:
            maps[cur + 1] = i
    return result
    pass

def balancedPassword(S):
    indexs = [i for i in range(len(S))]
    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            indexs[i] = indexs[i - 1]    
    buckets = set()
    result = 0
    start = 0    
    for i in range(len(S)):
        if len(buckets) < 2:
            buckets.add(S[i])
        else:
            if S[i] not in buckets:
                if i - start > result:
                    result = max(result, getLongest(S[start: i]))
                start = indexs[i - 1]
                buckets = set([S[i - 1], S[i]])    
    if len(S) - start > result:
        result = max(result, getLongest(S[start: len(S)]))    
    return result
    pass

# "cabbacc" = 4
print("cabbacc, the length of the longest balanced substring is", str(balancedPassword("cabbacc")))
# "abababa" = 6
print("abababa, the length of the longest balanced substring is", str(balancedPassword("abababa")))
# "aaaaaaa" = 0
print("aaaaaaa, the length of the longest balanced substring is", str(balancedPassword("aaaaaaa")))

