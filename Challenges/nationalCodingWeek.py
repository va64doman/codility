# National Coding Week
# LargestString: Find the alphabetically largest string that can be obtained by performing some substitutions.

def largestString(S):
    A = list(S)
    i = 0
    while i + 3 <= len(A):
        if A[i:i+3] == list("abb"):
            A[i:i+3] = list("baa")
            i = max(i-2, 0)
        else: i += 1
    return ''.join(A)
    pass

# "ababb" = "baaaa"
print("ababb, the alphabetically largest string that can be obtained by performing the above operation any number of times is", largestString("ababb"))
# "abbbabb" = "babaaaa"
print("abbbabb, the alphabetically largest string that can be obtained by performing the above operation any number of times is", largestString("abbbabb"))
# "aaabab" = "aaabab"
print("aaabab, the alphabetically largest string that can be obtained by performing the above operation any number of times is", largestString("aaabab"))
