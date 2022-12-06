# Cobaltum 2018
# IncreasingSequences: Given two sequences of integers, count the minimum number of swaps (A[k], B[k]) needed to make both sequences increasing.

def increasingSequences(A, B):
    groups = getGroups(A, B)
    if groups == None:
        return -1
    return sum(groups)
    pass

def getGroups(A, B):
    groups = []
    groupLength = 0
    changes = 0
    prevContinueOnlyWithChange = False
    for i in range(len(A) + 1):
        if groupLength == 0:
            groupLength += 1
            continue
        continueWithoutChange = i == len(A) or A[i-1] < A[i] and B[i-1] < B[i]
        continueWithChange = i == len(A) or A[i-1] < B[i] and B[i-1] < A[i]
        if not continueWithoutChange and not continueWithChange: return None
        if continueWithoutChange and continueWithChange:
            groups.append(min(changes, groupLength - changes))
            groupLength = 1
            changes = 0
            prevContinueOnlyWithChange = False
            continue
        if prevContinueOnlyWithChange: continueWithChange = not continueWithChange
        prevContinueOnlyWithChange = continueWithChange
        if continueWithChange: changes += 1
        groupLength += 1
    return groups
    pass
        

# (A = [5,3,7,7,10], B = [1,6,6,9,9]) = 2
print("A = [5,3,7,7,10], B = [1,6,6,9,9], the minimum number of swaps (A[k], B[k]) needed to make both sequences increasing is",
      str(increasingSequences(A = [5,3,7,7,10], B = [1,6,6,9,9])))
# (A = [5,-3,6,4,8], B = [2,6,-5,1,0]) = -1
print("A = [5,-3,6,4,8], B = [2,6,-5,1,0], the minimum number of swaps (A[k], B[k]) needed to make both sequences increasing is",
      str(increasingSequences(A = [5,-3,6,4,8], B = [2,6,-5,1,0])))
# (A = [1,5,6], B = [-2,0,2]) = 0
print("A = [5,-3,6,4,8], B = [2,6,-5,1,0], the minimum number of swaps (A[k], B[k]) needed to make both sequences increasing is",
      str(increasingSequences(A = [1,5,6], B = [-2,0,2])))
