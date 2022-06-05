#FibFrog: Count the minimum number of jumps required for a frog to get to the other side of a river.
def fibN(N):
    fib = [0] * 100
    fib[1] = 1
    for i in range(2, 100):
        fib[i] = fib[i-1] + fib[i-2]
        if fib[i] > N:
            return fib[2:i]

def fibFrog(A):
    A.append(1)
    fib = fibN(len(A))
    reachSteps = [0] * len(A)

    #leafs that can be reached in one step first
    for j in fib:
        if A[j-1] == 1:
            reachSteps[j-1] = 1

    #search leafs with more than one step
    for i in range(len(A)):
        if A[i] == 0 or reachSteps[i] > 0:
            continue
        min_i = -1
        min_v = 100000
        for j in fib:
            previousi = i - j
            if previousi < 0:
                break
            if reachSteps[previousi] > 0 and min_v > reachSteps[previousi]:
                min_v = reachSteps[previousi]
                min_i = previousi
        if min_i != -1:
            reachSteps[i] = min_v + 1
    if reachSteps[len(A)-1] > 0:
        return reachSteps[len(A) - 1]
    return -1
    pass

#[0,0,0,1,1,0,1,0,0,0,0] = 3
print("[0,0,0,1,1,0,1,0,0,0,0], the minimum numer of jumps is", str(fibFrog([0,0,0,1,1,0,1,0,0,0,0])))
