# Pair a Coder
# RemoveSubstrings: Given a string, calculate the length of the shortest string which can be achieved by removing any number of substrings that start and end with the same letter.

def removeSubstrings(S):
    N = len(S)
    nxt = dict()
    dp = [None] *(N+1)
    dps = [None] * (N+1)
    dp[N] = dps[N] = 0
    for i in range(N-1, -1, -1):
        dps[i] = N-i
        if S[i] in nxt:
            j = nxt[S[i]]
            dps[i] = min(dp[j+1], dps[j])
        dp[i] = min(1 + dp[i+1], dps[i])
        nxt[S[i]] = i
    return dp[0]
    pass

# "abccac" = 1
print("abccac, the length of the shortest string that can be obtained from S by applying any number of moves is", str(removeSubstrings("abccac")))
# "abcdabcdabcd" = 2
print("abcdabcdabcd, the length of the shortest string that can be obtained from S by applying any number of moves is", str(removeSubstrings("abcdabcdabcd")))
# "axaabyab" = 0
print("axaabyab, the length of the shortest string that can be obtained from S by applying any number of moves is", str(removeSubstrings("axaabyab")))
