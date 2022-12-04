# Vanadium 2016
# WinterLights: Given a string of digits, count the number of subwords
# (consistent subsequences) that are anagrams of any palindrome.
MODULO = 1000000007

def winterLights(S):
    return winterLightsCalc(S, 10)
    pass

def winterLightsCalc(S, dictSize):
    if S == None or S == "" or not S: return 0
    N = len(S)
    chars = [char for char in S]
    capacity = 1 << dictSize
    counts = [0] * capacity
    globalCount = 0
    globalMask = 0
    for i in range(N):
        C = chars[i]
        localMask = bitmask(C)
        counts[globalMask] += 1
        # XOR
        globalMask ^= localMask
        localCount = counts[globalMask]
        j = 1
        while j < capacity:
            localCount += counts[j^globalMask]
            j <<= 1
        globalCount += localCount
        globalCount %= MODULO
    return globalCount
    pass

def bitmask(C):
    return 1 << (ord(C) - ord('0'))
    pass

# 02002 = 11
print("02002, the number of subwords is", str(winterLights("02002")))
