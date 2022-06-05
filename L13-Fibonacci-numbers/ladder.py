#Ladder: Count the number of different ways of climbing to the top of a ladder.
def ladder(A,B):
    result = [0] * len(A)
    fib = [0] * (len(A) + 2)
    fib[1] = 1
    for i in range(2, len(A) + 2):
        fib[i] = fib[i-1] + fib[i-2]
    for i in range(len(A)):
        result[i] = fib[A[i]+1] & (2**B[i]-1)
    return result
    pass

# (A = [4,4,5,5,1], B = [3,2,4,3,1]) = [5,1,8,0,1]
print("[4,4,5,5,1], [3,2,4,3,1], the number of ways to climb to the top each is", str(ladder([4,4,5,5,1], [3,2,4,3,1])))
