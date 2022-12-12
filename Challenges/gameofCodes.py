# Game of Codes
# ThreeLettersBlocks: Given a string S, delete as few letters as possible to obtain a word composed of at most three blocks.

def threeLettersBlock(S):
    N = len(S)
    blockCount = 0
    blockSize = [0 for i in range(N)]
    blockCharNumber = [0 for i in range(N)]
    currentCharNumber = -1
    blockCount = -1
    for i in range(len(S)):
        charNumber = ord(S[i]) - ord('a')
        if charNumber == currentCharNumber: blockSize[blockCount] += 1
        else:
            blockCount += 1
            blockSize[blockCount] = 1
            blockCharNumber[blockCount] = charNumber
            currentCharNumber = charNumber
    blockCount += 1
    maxLengthBefore = [-1, -1, -1, 0]
    lastBlock = [[0 for j in range(4)] for i in range(26)]
    lastBlockLength = [[0 for j in range(4)] for i in range(26)]
    for j in range(26):
        for i in range(4):
            lastBlock[j][i] = -1
    for i in range(blockCount):
        for j in range(4):
            if maxLengthBefore[j] == -1: continue
            blockChar = blockCharNumber[i]
            currentMax = maxLengthBefore[j]
            if lastBlock[blockChar][j] != -1:
                combineLength = lastBlockLength[blockChar][j] + blockSize[i]
                lastBlock[blockChar][j] = i
                maxLengthBefore[j] = max(currentMax, combineLength)
                lastBlockLength[blockChar][j] = combineLength
            if j > 0:
                combineLength = currentMax + blockSize[i]
                maxLengthBefore[j - 1] = max(maxLengthBefore[j - 1], combineLength)
                lastBlock[blockChar][j - 1] = i
                lastBlockLength[blockChar][j - 1] = max(lastBlockLength[blockChar][j - 1], combineLength)
    return max(max(maxLengthBefore[0], maxLengthBefore[1]), max(maxLengthBefore[2], maxLengthBefore[3]))
    pass

# "aabacbba" = 6
print("aabacbba, the length of the longest word composed of at most three blocks, obtained by deleting some letters from S is", str(threeLettersBlock("aabacbba")))
# "aabxbaba" = 6
print("aabxbaba, the length of the longest word composed of at most three blocks, obtained by deleting some letters from S is", str(threeLettersBlock("aabxbaba")))
# "xxxyxxyyyxyyy" = 11
print("xxxyxxyyyxyyy, the length of the longest word composed of at most three blocks, obtained by deleting some letters from S is", str(threeLettersBlock("xxxyxxyyyxyyy")))
# "atheaxbtheb" = 5
print("atheaxbtheb, the length of the longest word composed of at most three blocks, obtained by deleting some letters from S is", str(threeLettersBlock("atheaxbtheb")))
