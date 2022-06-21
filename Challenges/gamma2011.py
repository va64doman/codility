# Gamma 2011
# CountPalindromicSlices: Count the palindromic subwords of given string.
def countPalindromicSlices(S):
    limit = 100000000
    paliStr = "#"
    sLen = len(S)
    for i in range(sLen):
        paliStr += S[i] + '#'
    paliLen = len(paliStr)
    palindrome = [0] * paliLen
    maxRight = -1
    centreForMaxRight = -1
    for i in range(paliLen):
        if maxRight > i:
            palindrome[i] = min(palindrome[centreForMaxRight * 2 - i], maxRight - i)
        else:
            palindrome[i] = 1
        while (i - palindrome[i] >= 0) and (i + palindrome[i] < paliLen) and (paliStr[i - palindrome[i]] == paliStr[i + palindrome[i]]):
            palindrome[i] += 1
        if i + palindrome[i] > maxRight:
            maxRight = i + palindrome[i]
            centreForMaxRight = i
    result = 0
    for i in range(paliLen):
        result += (palindrome[i] - 1) // 2
        if result > limit:
            return -1
    return result
    pass

# baababa = 6
print("baababa, the number of palindromic subwords is", str(countPalindromicSlices("baababa")))