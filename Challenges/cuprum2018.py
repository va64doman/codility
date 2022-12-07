# Cuprum 2018
# BeautifulPassword: Given a string, find the length of the longest substring in which every character appears an even number of times.

def beautifulPassword(S):
    occurrences = {0:1}
    length = len(S)
    sums = 0
    maximum = 0
    for i in range(length):
        currentElement = S[i]
        if ord(currentElement) <= ord('9'): sums ^= 1 << (ord(currentElement) - ord('0'))
        else: sums ^= 1 << (ord(currentElement) - ord('a') + 10)
        if sums in occurrences: maximum = max(maximum, i - occurrences[sums])
        else: occurrences[sums] = i
    return maximum
    pass

# "6daa6ccaaa6d" = 8
print("6daa6ccaaa6d, the length of the longest substring in which every character appears an even number of times is", str(beautifulPassword("6daa6ccaaa6d")))
# "abca" = 0
print("abca, the length of the longest substring in which every character appears an even number of times is", str(beautifulPassword("abca")))
