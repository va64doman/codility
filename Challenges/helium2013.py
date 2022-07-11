# Helium 2013
# FindThree: Find the longest border of a given string, that has three non-overlapping occurrences.
def findThree(S):
    N = len(S)
    if N < 3:
        return 0
    P = [0] * N
    left = right = -1
    for i in range(1, N):
        if right < i:
            j = 0
            while i + j < N and S[j] == S[j + i]:
                j += 1
            if j:
                P[i] = j
                left = i
                right = i + j - 1
        elif right - i < P[i - left]:
            j = right + 1
            while j < N and S[j] == S[j-i]:
                j += 1
            P[i] = j - i
            left = i
            right = j - 1
        else:
            P[i] = P[i - left]
    length = N // 3
    j = N - length * 2
    m = 0
    for i in range(length, j + 1):
        m = max(m, P[i])
        if m >= length and P[N - length] == length:
            return length
    length -= 1
    while length > 0:
        m = max(m, P[length])
        j += 1
        m = max(m, P[j])
        j += 1
        m = max(m, P[j])
        if m >= length and P[N - length] == length:
            break
        length -= 1
    return length
    pass

# barbararhubarb = 1
print("barbararhubarb, the length of its longest border that has at least three non-overlapping occurrences is", str(findThree("barbararhubarb")))
# ababab = 2
print("ababab, the length of its longest border that has at least three non-overlapping occurrences is", str(findThree("ababab")))
# baaab = 0
print("baaab, the length of its longest border that has at least three non-overlapping occurrences is", str(findThree("baaab")))