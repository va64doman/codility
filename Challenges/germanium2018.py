# Germanium 2018
# MaxNotPresent: You have a deck of cards in which each card has two numbers:
# one on the front and one on the back.
# Flip some cards over so as to maximize the smallest integer that's
# not present on any card's front.

maxN = 100005
card = []

def find(x):
    global card
    return x if x == card[x] else find(card[x])
    pass

def maxNotPresent(A, B):
    global card
    global maxN
    
    N = len(A)
    card = [0] * maxN
    visited = [0] * maxN
    maximum = [0] * maxN
    for i in range(1, N + 1):
        card[i] = i
        maximum[i] = i
    for i in range(N):
        u = A[i]
        v = B[i]
        if u > N and v > N: continue
        if u > N: u = v
        if v > N: v = u
        u = find(u)
        v = find(v)
        if u == v: visited[u] = 1
        else:
            card[u] = v
            visited[v] |= visited[u]
            maximum[v] = max(maximum[v], maximum[u])
    ans = N + 1
    for i in range(1, N + 1):
        if visited[find(i)] == 0: ans = min(ans, maximum[find(i)])
    return ans    
    pass

# (A = [1, 2, 4, 3], B = [1, 3, 2, 3]) = 5
print("A = [1, 2, 4, 3], B = [1, 3, 2, 3], the maximum smallest integer that is not present on any card's front is", str(maxNotPresent(A = [1, 2, 4, 3], B = [1, 3, 2, 3])))
# (A = [4, 2, 1, 6, 5], B = [3, 2, 1, 7, 7]) = 4
print("A = [4, 2, 1, 6, 5], B = [3, 2, 1, 7, 7], the maximum smallest integer that is not present on any card's front is", str(maxNotPresent(A = [4, 2, 1, 6, 5], B = [3, 2, 1, 7, 7])))
# (A = [2, 3], B = [2, 3]) = 1
print("A = [2, 3], B = [2, 3], the maximum smallest integer that is not present on any card's front is", str(maxNotPresent(A = [2, 3], B = [2, 3])))

