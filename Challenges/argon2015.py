# Argon 2015
# TrekAndSwim: Find a longest slice of a binary array that can be split into two parts: in the left part, 0 should be the leader;
#              in the right part, 1 should be the leader.

def trekAndSwim(A):
    firstZero = -1
    lastOne = -1
    seaDaysCount = 0
    seaEndIndex = 0
    seaArraySize = 0
    mountainStartIndex = 0

    for i in range(len(A)):
        if firstZero == -1 and A[i] == 0: firstZero = i
        if A[i] == 1: lastOne = i
    if firstZero == -1 or lastOne == -1 or firstZero >= lastOne: return 0
    totalNumOfZeros = 0
    for i in range(firstZero, lastOne + 1, 1):
        if i == firstZero: seaEndIndex = i
        if A[i] == 0: totalNumOfZeros += 1
        if A[i] == 0 and seaTripNotFail(i - firstZero + 1, totalNumOfZeros):
            seaDaysCount = totalNumOfZeros
            seaEndIndex = i

    seaArraySize = seaEndIndex - firstZero + 1
    if mountainStartIndex - seaEndIndex > 1: return 0

    startItrator = lastOne
    tempOnes = 0
    tempZeros = 0
    tempEffectiveZeros = 0
    extraDays = 0

    while startItrator > firstZero:
        if extraDays + lastOne >= len(A) - 1: break
        if startItrator > seaEndIndex:
            if A[startItrator] == 1:
                tempOnes += 1
                newExtraDays = getExtraDays(tempOnes, tempZeros)
                if newExtraDays > extraDays: extraDays = newExtraDays
            elif A[startItrator] == 0: tempZeros += 1
        else:
            if A[startItrator] == 1:
                tempOnes += 1
                newExtraDays = getExtraDays(tempOnes, tempZeros)
                if newExtraDays > extraDays:
                    newArraySize = startItrator - firstZero + 1
                    if seaTripNotFail(newArraySize, seaDaysCount - tempEffectiveZeros):
                        extraDays = newExtraDays
                        seaArraySize = newArraySize
                        seaEndIndex = startItrator - 1
                        seaDaysCount -= tempEffectiveZeros
                        tempEffectiveZeros = 0
            elif A[startItrator] == 0:
                tempZeros += 1
                tempEffectiveZeros += 1
        startItrator -= 1
        
    expansionVal = arrayExpandLeft(firstZero, seaDaysCount, seaArraySize, A)
    firstZero -= expansionVal
    seaArraySize += expansionVal
    mountainTripDuration = lastOne - seaEndIndex + extraDays
    
    return seaArraySize + mountainTripDuration               
    pass

def getExtraDays(numOfOnes, numOfZeros):
    return numOfOnes - numOfZeros - 1
    pass

def arrayExpandLeft(firstZero, seaDaysCount, seaArraySize, A):
    expansionVal = 0
    while seaTripHasExtraSwimDays(seaArraySize, seaDaysCount) and firstZero > 0:
        if firstZero == 0: break
        firstZero -= 1
        seaArraySize += 1
        expansionVal += 1
    return expansionVal
    pass

def seaTripNotFail(seaArraySize, numOfZeros):
    return numOfZeros - (seaArraySize - numOfZeros) >= 1
    pass

def seaTripHasExtraSwimDays(seaArraySize, numOfZeros):
    return numOfZeros - (seaArraySize - numOfZeros) > 1
    pass

# [1,1,0,1,0,0,1,1] = 7
print("[1,1,0,1,0,0,1,1], the longest slice of a binary array that can be split into two parts is", str(trekAndSwim([1,1,0,1,0,0,1,1])))
# [1,0] = 0
print("[1,1,0,1,0,0,1,1], the longest slice of a binary array that can be split into two parts is", str(trekAndSwim([1,0])))
