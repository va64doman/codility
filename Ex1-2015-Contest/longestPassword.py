#LongestPassword: Given a string containing words, find the longest word that satisfies specific conditions.
def longestPassword(S):
    words = S.split(" ")
    longestWord = -1
    for word in words:
        if checkWord(word):
            longestWord = max(longestWord, len(word))
    return longestWord
    pass

def checkWord(word):
    letterCount = digitCount = 0
    for c in word:
        if c.isupper() or c.islower():
            letterCount += 1
        elif c.isdigit():
            digitCount += 1
        else:
            return False
    return letterCount % 2 == 0 and digitCount % 2 == 1

# "test 5 a0A pass007 ?xy1" = 7
print("\"test 5 a0A pass007 ?xy1\", the length of longest word is", str(longestPassword("test 5 a0A pass007 ?xy1")))
