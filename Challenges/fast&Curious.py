# Fast & Curious
# NewMotorway: Given a number of cities located along a road, build a motorway between two cities to minimize
# the sum of distances from all cities to the easternmost one.

def newMotorway(A):
    N = len(A)
    cost = 0
    for i in range(1,N): cost += A[N-1] - A[i]
    best = cost
    for X in range(N-1):
        cost -= A[N-1] - A[X+1]
        cost += (X+1) * (A[X+1] - A[X])
        best = min(best, cost)
    return best % (10**9 + 7)
    pass

# [1, 5, 9, 12] = 7
print("[1, 5, 9, 12], the minimum total travel time is", str(newMotorway([1, 5, 9, 12])))
# [5, 15] = 0
print("[5, 15], the minimum total travel time is", str(newMotorway([5, 15])))
# [2, 6, 7, 8, 12] = 9
print("[2, 6, 7, 8, 12], the minimum total travel time is", str(newMotorway([2, 6, 7, 8, 12])))
# (N = 20 and A[K] = K * (5 * 10**7) for each K from 0 to 19) = 499999972
A = [0] * 20
for i in range(20):
    A[i] = i * (5 * 10**7)
print("[N = 20 and A[K] = K * (5 * 10**7) for each K from 0 to 19, the minimum total travel time is", str(newMotorway(A)))
