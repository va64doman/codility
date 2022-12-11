# May the 4th
# DoubleHanoi: Find the maximum number of disks that can be placed on two rods.
# The disks should be in decreasing order of size on the first rod and in increasing order of size on the second rod.

from collections import defaultdict

def doubleHanoi(A, L, R):
    cnt = defaultdict(int)
    for a in A:
        cnt[a] += 1
    ans = 0
    for a in cnt:
        rods = (a < L) + (a > R)
        ans += min(cnt[a],rods)
    return ans
    pass

# (A = [2, 3, 3, 4], L = 3, R = 1) = 3
print("A = [2, 3, 3, 4], L = 3, R = 1, the maximum number of disks that can be placed on two rods is", str(doubleHanoi(A = [2, 3, 3, 4], L = 3, R = 1)))
# (A = [1, 4, 5, 5], L = 6, R = 4) = 4
print("A = [1, 4, 5, 5], L = 6, R = 4, the maximum number of disks that can be placed on two rods is", str(doubleHanoi(A = [1, 4, 5, 5], L = 6, R = 4)))
# (A = [5, 2, 5, 2], L = 8, R = 1) = 4
print("A = [5, 2, 5, 2], L = 8, R = 1, the maximum number of disks that can be placed on two rods is", str(doubleHanoi(A = [5, 2, 5, 2], L = 8, R = 1)))
# (A = [1, 5, 5], L = 2, R = 4) = 2
print("A = [1, 5, 5], L = 2, R = 4, the maximum number of disks that can be placed on two rods is", str(doubleHanoi(A = [1, 5, 5], L = 2, R = 4)))
