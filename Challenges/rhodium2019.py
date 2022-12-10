# Rhodium 2019
# TreeRange: Given a tree, calculate number of its subtrees whose vertex labels form a continuous range of integers.

def treeRange(T):
    N = len(T)
    res = 0    
    for i in range(N-1):
        bad = {}
        bad_count = 1
        if T[i] != i:
            bad[T[i]] = 1        
        for j in range(i+1, N):
            if j in bad:
                bad_count -= bad.pop(j)                
            if not i <= T[j] <= j:
                if T[j] in bad:
                    bad[T[j]] += 1
                else:
                    bad[T[j]] = 1
                bad_count += 1
            elif j == T[j]:
                bad_count += 1                
            if bad_count <= 1:
                res += 1
    return res+N
    pass

# [2,0,2,2,1,0] = 12
print("[2,0,2,2,1,0], the number of its subtrees whose vertex labels form a continuous range of integers is", str(treeRange([2,0,2,2,1,0])))
