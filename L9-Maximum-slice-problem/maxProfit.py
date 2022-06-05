#MaxProfit: Given a log of stock prices compute the maximum possible earning.
def maxProfit(A):
    if len(A) == 0:
        return 0
    mymin = A[0]
    mymax = 0
    s = 0

    for i in range(1, len(A)):
        if A[i] < mymin:
            mymin = A[i]
            s = 0
        else:
            s += A[i] - A[i-1]
        if mymax < s:
            mymax = s
            
    return mymax
    pass

#[23171, 21011, 21123, 21366, 21013, 21367] = 356
print("[23171, 21011, 21123, 21366, 21013, 21367], the log of stock prices will have max possible earning of", str(maxProfit([23171, 21011, 21123, 21366, 21013, 21367])))
