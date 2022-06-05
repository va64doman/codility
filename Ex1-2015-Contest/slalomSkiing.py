#SlalomSkiing: Given a sequence, find the longest subsequence that can be decomposed into at most three monotonic parts.
from bisect import bisect_left
def slalomSkiing(A):
    bound = max(A)
    tripleA = []
    for num in A:
        tripleA += [2 * bound + num, 2 * bound - num, num]
    return longest_increasing_subsequence(tripleA)
    
def longest_increasing_subsequence(lst):
    dp = []
    for num in lst:
        idx = bisect_left(dp, num)
        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num
    return len(dp)

#[15,13,5,7,4,10,12,8,2,11,6,9,3] = 8
print("[15,13,5,7,4,10,12,8,2,11,6,9,3], longest subsequence that can be decomposed into at most 3 monotonic parts is",
      str(slalomSkiing([15,13,5,7,4,10,12,8,2,11,6,9,3])))
# [1,5] = 2
print("[1,5], longest subsequence that can be decomposed into at most 3 monotonic parts is", str(slalomSkiing([1,5])))
