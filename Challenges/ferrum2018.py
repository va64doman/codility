# Ferrum 2018
# LongestNonnegativeSumSlice: Given an array consisting of the integers -1, 0 and 1, find the longest slice with a non-negative sum.

def longestNonnegativeSumSlice(A):
    ret = 0
    totalSum = 0
    minIndexes = {}
    minusOnes = []
    plusOnes = []
    precedingZerosStart = -1
    for i in range(len(A)):
        totalSum += A[i]
        if totalSum >= 0:
            maxAtIndex = i + 1
            ret = max(ret, maxAtIndex)
        if A[i] == 0:
            if precedingZerosStart == -1: precedingZerosStart = i
            if totalSum in minIndexes and minIndexes[totalSum] != -1:
                maxAtIndex = i - minIndexes[totalSum] + 1
                ret = max(ret, maxAtIndex)
            elif precedingZerosStart != -1:
                maxAtIndex = i - precedingZerosStart + 1
                ret = max(ret, maxAtIndex)
        elif A[i] == 1:
            if precedingZerosStart != -1: plusOnes.append(precedingZerosStart)
            else: plusOnes.append(i)
            if totalSum < 0:
                if totalSum not in minIndexes: minIndexes[totalSum] = -1
                else:
                    if minIndexes[totalSum] == -1:
                        popMinusOnes = minusOnes.pop()
                        minIndexes[totalSum] = popMinusOnes
                        maxAtIndex = i - minIndexes[totalSum] + 1
                        ret = max(ret, maxAtIndex)
                    else:
                        if len(minusOnes) > 0:
                            popMinusOnes = minusOnes.pop()
                            maxAtIndex = i - minIndexes[totalSum] + 1
                            ret = max(ret, maxAtIndex)
            else:
                if len(minusOnes) > 0: popMinusOnes = minusOnes.pop()
            precedingZerosStart = -1
        elif A[i] == -1:
            if precedingZerosStart != -1: minusOnes.append(precedingZerosStart)
            else: minusOnes.append(i)
            if totalSum < 0:
                if totalSum not in minIndexes: minIndexes[totalSum] = -1
                else:
                    if minIndexes[totalSum] == -1:
                        popPlusOnes = plusOnes.pop()
                        minIndexes[totalSum] = popPlusOnes
                        maxAtIndex = i - minIndexes[totalSum] + 1
                        ret = max(ret, maxAtIndex)
                    else:
                        if len(plusOnes) > 0:
                            popPlusOnes = plusOnes.pop()
                            maxAtIndex = i - minIndexes[totalSum] + 1
                            ret = max(ret, maxAtIndex)
            else:
                if len(plusOnes) > 0: popPlusOnes = plusOnes.pop()
            precedingZerosStart = -1
    return ret
    pass

# [−1, −1, 1, −1, 1, 0, 1, −1, −1] = 7
print("[−1, −1, 1, −1, 1, 0, 1, −1, −1], the longest slice with a non-negative sum is", str(longestNonnegativeSumSlice([-1, -1, 1, -1, 1, 0, 1, -1, -1])))
# [1, 1, −1, −1, −1, −1, −1, 1, 1] = 4
print("[1, 1, −1, −1, −1, −1, −1, 1, 1], the longest slice with a non-negative sum is", str(longestNonnegativeSumSlice([1, 1, -1, -1, -1, -1, -1, 1, 1])))
