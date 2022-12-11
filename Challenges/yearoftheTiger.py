# Year of the Tiger
# TricoloredTowers: Find the maximum number of towers with same color order that can be obtained from an initial group of tricolored towers if
# at most one swap of adjacent colors can be performed in every tower.

from collections import defaultdict

def swaps(t):
    return {t, t[1]+t[0]+t[2], t[0]+t[2]+t[1]}
    pass

def tricoloredTowers(T):
    occ = defaultdict(int)
    for t in T:
        for cand in swaps(t): occ[cand] += 1
    return max(occ.values())
    pass

# ["aab", "cab", "baa", "baa"] = 3
print("[""aab"", ""cab"", ""baa"", ""baa""], the maximum number of towers that we can obtain with the same order of block colors is",
      str(tricoloredTowers(["aab", "cab", "baa", "baa"])))
# ["zzz", "zbz", "zbz", "dgf"] = 2
print("[""zzz"", ""zbz"", ""zbz"", ""dgf""], the maximum number of towers that we can obtain with the same order of block colors is",
      str(tricoloredTowers(["zzz", "zbz", "zbz", "dgf"])))
# ["abc", "cba", "cab", "bac", "bca"] = 3
print("[""abc"", ""cba"", ""cab"", ""bac"", ""bca""], the maximum number of towers that we can obtain with the same order of block colors is",
      str(tricoloredTowers(["abc", "cba", "cab", "bac", "bca"])))
