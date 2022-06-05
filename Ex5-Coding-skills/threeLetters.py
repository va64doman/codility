#ThreeLetters: Given two integers A and B, return a string which contains A letters "a" and B letters "b" with no three consecutive letters being the same.
import math
def threeLetters(A,B):
    if A == 0 and B == 0:
        return ""
    S = {"A": A, "B": B}
    cur = "A" if A >= B else "B"
    ans = ""
    count = 0
    for i in range(A+B):
        if cur == "A":
            ans += "a"
        else:
            ans += "b"
        S[cur] -= 1
        count += 1
        if S["A"] == 0:
            cur = "B"
            continue
        if S["B"] == 0:
            cur = "A"
            continue
        nxt = "A" if S["A"] >= S["B"] else "B"
        if nxt != cur:
            cur = nxt
            count = 0
        if count == 2:
            cur = "B" if cur == "A" else "A"
            count = 0
    return ans
    pass

#(A = 5 and B = 3) = "aabaabab" or "abaabbaa" or any correct answers
print("The string with 5 'a's and 3 'b's with no three consecutive letters being the same is", threeLetters(5,3))
#(A = 3 and B = 3) = "ababab", "aababb", "abaabb" or any of several other strings
print("The string with 3 'a's and 3 'b's with no three consecutive letters being the same is", threeLetters(3,3))
#(A = 1 and B = 4) = "bbabb"
print("The string with 1 'a's and 4 'b's with no three consecutive letters being the same is", threeLetters(1,4))
