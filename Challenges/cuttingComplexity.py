# Cutting Complexity
# StringModification: Given a string of letters 'M' and 'L', compute the minimum number of changes needed to obtain a string such that the length of its longest
# interval of letters 'M' is equal to K.
import sys

def stringModification(S, K):
    currentRate = 0
    maxRate = 0
    queue = []
    minSwitchCount = sys.maxsize
    sumCount = 0
    for node in S:
        if node != 'M':
            if maxRate == K:
                minSwitchCount = min(minSwitchCount, len(queue))
            queue.append(currentRate + 1)
            currentRate = 0
            maxRate += 1
            continue
        currentRate += 1
        maxRate += 1
        if maxRate <= K: continue
        minSwitchCount = min(minSwitchCount, len(queue) + 1)
        if len(queue) > 0:
            while maxRate > K:
                maxRate -= queue.pop(0)
        else:
            sumCount += 1
            currentRate = 0
            maxRate = 0
    if maxRate == K: minSwitchCount = min(minSwitchCount, len(queue))
    return sumCount if sumCount > 0 else minSwitchCount
    pass

# (S = "MLMMLLM", K = 3) = 1
print("S = ""MLMMLLM"", K = 3, the minimum number of changes needed to obtain a string such that the length of its longest interval of letters 'M' is equal to K is",
      str(stringModification(S = "MLMMLLM", K = 3)))
# (S = "MLMMMLMMMM", K = 2) = 2
print("S = ""MLMMMLMMMM"", K = 2, the minimum number of changes needed to obtain a string such that the length of its longest interval of letters 'M' is equal to K is",
      str(stringModification(S = "MLMMMLMMMM", K = 2)))
