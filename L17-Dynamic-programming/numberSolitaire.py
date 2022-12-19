#NumberSolitaire: In a given array, find the subset of maximal sum in which the distance between consecutive elements is at most 6.
import sys
def numSol(A):
    len_a = len(A)
    dp = [A[0]] + ([0]*(len_a-1))
    for index in range(1, len_a):
        temp_max = (-sys.maxsize)-1
        for die_number in range(1, 6+1):
            if index-die_number >= 0:
                temp_max = max( dp[index-die_number] + A[index], temp_max ) # super important!
        dp[index] = temp_max
    return dp[len_a-1]     
    pass

#[1,-2,0,9,-1,-2] = 8
print("[1,-2,0,9,-1,-2], the subset of maximal sum in which the distance between consecutive elements is at most 6 is", str(numSol([1,-2,0,9,-1,-2])))
