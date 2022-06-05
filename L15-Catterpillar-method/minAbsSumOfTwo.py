#MinAbsSumOfTwo: Find the minimal absolute value of a sum of two elements.
def minAbsSumOfTwo(A):
    A.sort()
    startIdx = 0
    endIdx = len(A) - 1
    minAbsSum = (2 * 10**9) + 1
    
    while startIdx <= endIdx:
        absSum = abs(A[startIdx] + A[endIdx])
        if absSum < minAbsSum:
            minAbsSum = absSum
        if abs(A[startIdx]) > abs(A[endIdx]):
            startIdx += 1
        else:
            endIdx -= 1
    return minAbsSum        
    pass

# [1,4,-3] = 1
print("[1,4,-3], the minimal absolute value of sum of 2 elements is", str(minAbsSumOfTwo([1,4,-3])))
# [-8,4,5,-10,3] = 3
print("[-8,4,5,-10,3], the minimal absolute value of sum of 2 elements is", str(minAbsSumOfTwo([-8,4,5,-10,3])))
