# Code Alone
# ABSwaps: Calculate the minimum required number of swaps of neighbouring letters in a string built from the letters 'a' and 'b',
# after which the string would contain both "aaa" and "bbb" as substrings.

def abSwaps(S):
    if S.count('a') < 3 or S.count('b') < 3: return -1
    for a, b in ['ab', 'ba']:
        if S.find(a*3) != -1:
            pos = [i for i in range(len(S)) if S[i] == b]
            ans = len(S)
            for i in range(len(pos)-2): ans = min(ans, pos[i+2] - pos[i] -2)
            return ans
    d = dict()
    q = []
    for i in range(len(S)):
        w = S[i:i+8]
        if w not in d:
            d[w] = 0
            q.append(w)
    while q:
        w = q[0]
        q = q[1:]
        if w.find('aaa') != -1 and w.find('bbb') != -1: return d[w]
        for i in range(len(w)-1):
            w2 = w[:i] + w[i+1] + w[i] + w[i+2:]
            if w2 not in d:
                d[w2] = d[w] + 1
                q.append(w2)
    pass

# "ababab" = 3
print("ababab, the number of swaps after which S would contain ""aaa"" and ""bbb"" as substrings is", str(abSwaps("ababab")))
# "abbbbaa" = 4
print("abbbbaa, the number of swaps after which S would contain ""aaa"" and ""bbb"" as substrings is", str(abSwaps("abbbbaa")))
# "bbbababaaab" = 0
print("bbbababaaab, the number of swaps after which S would contain ""aaa"" and ""bbb"" as substrings is", str(abSwaps("bbbababaaab")))
# "abbabb" = -1
print("abbabb, the number of swaps after which S would contain ""aaa"" and ""bbb"" as substrings is", str(abSwaps("abbabb")))
