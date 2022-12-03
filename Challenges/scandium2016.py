# Scandium 2016
# EvenSumsGame: Compute a winning move in a game in which you remove slices with even sums of elements.
def evenSumsGame(A):
    odds = 0
    for i in range(len(A)):
        A[i] &= 1
        if A[i] == 1: odds += 1

    if odds == 1:
        for i in range(len(A)):
            if A[i] == 1:
                if i > len(A) - 1 - i: return "0," + str(i - (len(A) - 1 - i) - 1)
                elif i < len(A) - 1 - i: return str(i + 1) + "," + str(len(A) - 1 - i)
                else: return "NO SOLUTION"
    if odds & 1 == 0: return "0," + str(len(A) - 1)
    
    left = leftEven(A)
    right = rightEven(A)
    rightIndex = len(A) - 1 - right
    
    if left >= right:
        oddIndex = findOddIndex(A, rightIndex - 1)
        diff = left - right
        x = left - diff
        remainingEvenCounts = rightIndex - oddIndex - 1
        y = oddIndex
        if remainingEvenCounts > 0:
            if x >= remainingEvenCounts:
                x -= remainingEvenCounts
                remainingEvenCounts = 0
            else: x = 0
        if remainingEvenCounts > right: y += remainingEvenCounts - right
        return str(x) + "," + str(y)
    else:
        oddIndex = findOddIndex(A, rightIndex - 1)
        middleSize = rightIndex - oddIndex - 1
        x = -1
        y = -1
        if middleSize >= right:
            x = 0
            diff = middleSize - right
            y = oddIndex + diff
        elif left + middleSize >= right:
            y = oddIndex
            x = left
            diff = left + middleSize - right
            if x >= diff: x -= diff
            else:
                temp = x
                x = 0
                diff -= temp
                y += diff
        else:
            x = left + 1
            diff = right - left
            y = rightIndex + diff
        return str(x) + "," + str(y)
    pass

def findOddIndex(A, start):
    while start >= 0 and A[start] == 0:
        start -= 1
    return start
    pass

def leftEven(A):
    for i in range(len(A)):
        if A[i] == 1: return i
    return -1
    pass

def rightEven(A):
    for i in range(len(A) - 1, -1, -1):
        if A[i] == 1: return len(A) - 1 - i
    return -1
    pass

# [4,5,3,7,2] = "1,2"
print("[4,5,3,7,2], the winning move is", str(evenSumsGame([4,5,3,7,2])))
# [2,5,4] = "NO SOLUTION"
print("[2,5,4], the winning move is", str(evenSumsGame([2,5,4])))
