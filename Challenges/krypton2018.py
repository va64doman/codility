# Krypton 2018
# MinTrailingZeros: Find a path in given matrix, such that the product of all the numbers on the path has the minimal number of trailing zeros.
def getValue(num):    
    num2 = 0
    num5 = 0
    contain0 = False
    if num == 0:
        return [True, 0, 0]    
    while num > 0 and (num % 2 == 0 or num % 5 == 0):
        if num % 2 == 0:
            num2 += 1
            num //= 2
        if num % 5 == 0:
            num5 += 1
            num //= 5    
    return [False, num2, num5]
    pass
    
def minTrailingZeros(A):
    if A is None or len(A) == 0:
        return 0    
    n = len(A)
    dp = [[[False, 0, 0] for i in range(n)] for _ in range(n)] # [contain 0 in one path, num of 2, num of 5]    
    # init
    num = A[0][0]
    contain0, num2, num5 = getValue(num)
    dp[0][0] = [contain0, num2, num5]
    # init first col
    for i in range(1, n):
        num = A[i][0]
        contain0, num2, num5 = getValue(num)        
        contain0 = contain0 or dp[i -1][0][0]
        if contain0:
            dp[i][0] = [True, 0, 0]
            continue        
        num2 += dp[i -1][0][1]
        num5 += dp[i - 1][0][2]
        dp[i][0] = [contain0, num2, num5]
    # init first row    
    for j in range(1, n):
        num = A[0][j]
        contain0, num2, num5 = getValue(num)        
        contain0 = contain0 or dp[0][j - 1][0]
        if contain0:
            dp[0][j] = [True, 0, 0]
            continue
        num2 += dp[0][j - 1][1]
        num5 += dp[0][j - 1][2]
        dp[0][j] = [contain0, num2, num5]        
    for i in range(1, n):
        for j in range(1, n):
            num = A[i][j]
            contain0, num2, num5 = getValue(num)            
            if contain0:
                dp[i][j] = [True, 0, 0]
                continue
            if dp[i - 1][j][0]:
                up = 1 
            else:
                up = min(dp[i - 1][j][1] + num2, dp[i - 1][j][2] + num5)            
            if dp[i][j -1][0]:
                left = 1
            else:
                left = min(dp[i][j - 1][1] + num2, dp[i][j - 1][2] + num5)
            if up < left:
                contain0 = dp[i - 1][j][0]
                if contain0:
                    dp[i][j] = [True, 0, 0]
                    continue
                num2 += dp[i -1][j][1]
                num5 += dp[i - 1][j][2]
            else:
                contain0 = dp[i][j - 1][0]
                if contain0:
                    dp[i][j] = [True, 0, 0]
                    continue
                num2 += dp[i][j - 1][1]
                num5 += dp[i][j - 1][2]            
            dp[i][j] = [contain0, num2, num5]    
    contain0, num2, num5 = dp[-1][-1]
    if contain0:
        return 1
    else:
        return min(num2, num5)
    pass

# [[2,10,1,3], [10,5,4,5], [2,10,2,1], [25,2,5,1]] = 1
print("[[2,10,1,3], [10,5,4,5], [2,10,2,1], [25,2,5,1]], the minimal number of trailing zeros is", str(minTrailingZeros([[2,10,1,3], [10,5,4,5], [2,10,2,1], [25,2,5,1]])))
# [[10,1,10,1], [1,1,1,10], [10,1,10,1], [1,10,1,1]] = 2
print("[[10,1,10,1], [1,1,1,10], [10,1,10,1], [1,10,1,1]], the minimal number of trailing zeros is", str(minTrailingZeros([[10,1,10,1], [1,1,1,10], [10,1,10,1], [1,10,1,1]])))
# [[10,10,10], [10,0,10], [10,10,10]]
print("[[10,10,10], [10,0,10], [10,10,10]], the minimal number of trailing zeros is", str(minTrailingZeros([[10,10,10], [10,0,10], [10,10,10]])))
