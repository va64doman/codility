#MinMaxDivision: Divide array A into K blocks and minimize the largest sum of any block.
def checkBlocks(A, g):
    blocks = 1
    blockSum = 0
    for a in A:
        blockSum += a
        if blockSum > g:
            blockSum = a
            blocks += 1
    return blocks

def minMaxDiv(K, M, A):
    minV = 0
    maxV = 0
    for a in A:
        maxV += a
        minV = min(minV, a)
        
    bestAns = maxV
    while minV <= maxV:
        mid = (minV + maxV) // 2
        blocks = checkBlocks(A, mid)
        if blocks > K:
            minV = mid + 1
        else:
            maxV = mid - 1
            if mid < bestAns:
                bestAns = mid
    return bestAns
    pass

#(K = 3, M = 5, A = [2,1,5,1,2,2,2]) = 6
print("K = 3, M = 5, A = [2,1,5,1,2,2,2], the minimal large sum is", str(minMaxDiv(3,5,[2,1,5,1,2,2,2])))
