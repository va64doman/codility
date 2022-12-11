# Gamer's
# FillTheGaps: Given a string consisting of characters 'a', 'b' and/or '?', replace each '?' with 'a' or 'b'
# so that the longest fragment of the resulting string consisting of equal letters is as short as possible.

def fragments(S):
    i = 0
    while i < len(S):
        d = 1
        while i + d < len(S) and S[i+d] == S[i]: d += 1
        if S[i] != '?': yield(i, d)
        i += d
    pass

def fillTheGaps(S):
    S = list(S)
    ans = 1
    for i, d in fragments(S):
        ans = max(ans, d)
    for i, d in fragments(S):
        if d == ans:
            other = 'a' if S[i] == 'b' else 'b'
            if i + d < len(S) and S[i+d] == '?': S[i+d] = other
    for i, d in fragments(S): ans = max(ans, d)
    return ans
    pass

# "aa??bbb" = 3
print("aa??bbb, he minimum possible length of the longest fragment of S consisting of equal characters after replacing all ""?"" characters with letters is",
      str(fillTheGaps("aa??bbb")))
# "a?b?aa?b?a" = 2
print("a?b?aa?b?a, he minimum possible length of the longest fragment of S consisting of equal characters after replacing all ""?"" characters with letters is",
      str(fillTheGaps("a?b?aa?b?a")))
# "??b??" = 1
print("??b??, he minimum possible length of the longest fragment of S consisting of equal characters after replacing all ""?"" characters with letters is",
      str(fillTheGaps("??b??")))
# "aa?b?aa" = 3
print("aa?b?aa, he minimum possible length of the longest fragment of S consisting of equal characters after replacing all ""?"" characters with letters is",
      str(fillTheGaps("aa?b?aa")))
