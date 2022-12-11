# Spooktober
# StacksOfCoins: Move coins between the given stacks to obtain a stack with the maximum possible number of coins.

def calc(A):
    coins = 0
    pref = []
    for a in A:
        pref.append(coins)
        coins = (coins + a) // 2
    return pref
    pass

def stacksOfCoins(A):
    ans = 0
    le = calc(A)
    ri = calc(A[::-1])[::-1]
    for i in range(len(A)):
        coins = le[i] + A[i] + ri[i]
        ans = max(ans, coins)
    return ans
    pass

# [2, 3, 1, 3] = 5
print("[2, 3, 1, 3], the maximum number of coins that can be accumulated in one stack after performing any number of moves is", str(stacksOfCoins([2, 3, 1, 3])))
# [3, 7, 0, 5] = 9
print("[3, 7, 0, 5], the maximum number of coins that can be accumulated in one stack after performing any number of moves is", str(stacksOfCoins([3, 7, 0, 5])))
# [1, 1, 1, 1, 1] = 1
print("[1, 1, 1, 1, 1], the maximum number of coins that can be accumulated in one stack after performing any number of moves is", str(stacksOfCoins([1, 1, 1, 1, 1])))
