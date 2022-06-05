#DisappearingPairs: Reduce a string containing instances of the letters "A", "B" and "C" via the following rule: remove one occurrence of "AA", "BB" or "CC".
def disappearingPairs(S):
    stack = []
    for s in S:
        if stack and s == stack[-1]:
            stack.pop()
        else:
            stack.append(s)
    return ''.join(stack)
    pass


#"ACCAABBC" = "AC"
print("ACCAABBC, the reduced string without AA, BB or CC:", disappearingPairs("ACCAABBC"))
#"ABCBBCBA" = ""
print("ABCBBCBA, the reduced string without AA, BB or CC:", disappearingPairs("ABCBBCBA"))
#"BABABA" = "BABABA"
print("BABABA, the reduced string without AA, BB or CC:", disappearingPairs("BABABA"))
