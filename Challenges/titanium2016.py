# Titanium 2016
# BracketsRotation: Find the longest valid slice of a sequence of brackets after performing at most K bracket rotations.
OPENING = '('
CLOSING = ')'

def bracketsRotation(S, K):
    sequence = removeValidBrackets(S)
    print(str(sequence))
    return getLongestSequenceLength(sequence, K)
    pass

def removeValidBrackets(S):
    validBrackets = [''] * len(S)
    stack = []
    for i in range(len(S)):
        c = S[i]
        if c == OPENING: stack.append(i)
        else:
            if not stack: validBrackets[i] = c
            else: stack.pop()
    for i in stack:
        validBrackets[i] = OPENING
    return validBrackets
    pass

def getLongestSequenceLength(sequence, K):
    invalidBracesCount = 0
    for c in sequence:
        if c == OPENING or c == CLOSING: invalidBracesCount += 1
    if invalidBracesCount == 0: return len(sequence)
    bracketsToTheLeft = [0] * (invalidBracesCount + 1)
    position = 1
    for i in range(len(sequence)):
        if sequence[i] == OPENING or sequence[i] == CLOSING:
            bracketsToTheLeft[position] = i + 1
            position += 1
    bracketsToTheRight = [0] * (invalidBracesCount + 1)
    bracketsToTheRight[len(bracketsToTheRight) - 1] = len(sequence)
    position = len(bracketsToTheRight) - 2
    for i in range(len(sequence) - 1, -1, -1):
        if sequence[i] == OPENING or sequence[i] == CLOSING:
            bracketsToTheRight[position] = i
            position -= 1
    splitterPosition = getSplitterPosition(sequence, bracketsToTheLeft)
    return getLongestSequenceByReversedCounts(bracketsToTheLeft, bracketsToTheRight, K, splitterPosition)
    pass

def getSplitterPosition(sequence, bracketsToTheLeft):
    for i in range(1, len(bracketsToTheLeft) - 1):
        if sequence[bracketsToTheLeft[i] - 1] == CLOSING and sequence[bracketsToTheLeft[i + 1] - 1] == OPENING: return i
    return -1
    pass

def getLongestSequenceByReversedCounts(bracketsToTheLeft, bracketsToTheRight, K, splitterPosition):
    maximum = 0
    for i in range(len(bracketsToTheLeft)):
        j = i + 2 * K
        if i < splitterPosition and splitterPosition < j:
            if (splitterPosition - i) % 2 == 1: j -= 2
        if j >= len(bracketsToTheRight):
            length = bracketsToTheRight[len(bracketsToTheRight) - 1] - bracketsToTheLeft[i]
            maximum = max(maximum, length)
            break
        length = bracketsToTheRight[j] - bracketsToTheLeft[i]
        maximum = max(maximum, length)
    if maximum % 2 == 1: maximum -= 1
    return maximum
    pass

# (S = ")()()(", K = 3) = 6
print("S = "")()()("", K = 3, the longest valid slice is", str(bracketsRotation(S = ")()()(", K = 3)))
# (S = ")))(((", K = 2) = 4
print("S = "")))((("", K = 2, the longest valid slice is", str(bracketsRotation(S = ")))(((", K = 2)))
# (S = ")))(((", K = 0) = 0
print("S = "")))((("", K = 0, the longest valid slice is", str(bracketsRotation(S = ")))(((", K = 0)))
