# Rho 2012
# HitTheNumber: Find the shortest addition chain ending with a given integer.
def hitTheNumber(A):
    v = [1]
    i = 1
    while not dfs(A, v, i):
        i += 1
    return v
    pass

def dfs(A, v, length):
    if v[len(v) - 1] == A:
        return True
    if len(v) >= length:
        return False
    i = v[len(v) - 1]
    j = length - len(v)
    while (i < A) and j:
        i <<= 1
        j -= 1
    if i < A:
        return False
    i = len(v) - 1
    y = v[i] << 1
    while i >= 0 and y > v[len(v) - 1]:
        j = i
        x = v[i] + v[j]
        while j >= 0 and x > v[len(v) - 1]:
            if x <= A:
                v.append(x)
                if dfs(A, v, length):
                    return True
                v.pop()
            j -= 1
            x = v[i] + v[j]
        i -= 1
        y = v[i] << 1
    return False
    pass
# 42 = [1, 2, 3, 6, 12, 24, 30, 42] or [1, 2, 4, 5,  8, 16, 21, 42]
# TODO: Somehow it came up with [1,2,4,8,16,32,40,42].
"""
x0 = 1
xn = 42
for each i = 1, ... , n, xi = xj + xk for some 0 <= j,k < i

Step 1: [1]
Step 2: [1,2] because 1 + 1 = 2
Step 3: [1,2,4] because 2 + 2 = 4
Step 4: [1,2,4,8] because 4 + 4 = 8
Step 5: [1,2,4,8,16] because 8 + 8 = 16
Step 6: [1,2,4,8,16,32] because 16 + 16 = 32
Step 7: [1,2,4,8,16,32,40] because 32 + 8 = 40
Step 8: [1,2,4,8,16,32,40,42] because 40 + 2 = 42
The expected answer has length of 8 as well as the actual answer.

If using [1, 2, 3, 6, 12, 24, 30, 42]
Step 1: [1]
Step 2: [1,2] because 1 + 1 = 2
Step 3: [1,2,3] because 1 + 2 = 3
Step 4: [1,2,3,6] because 3 + 3 = 6
Step 5: [1,2,3,6,12] because 6 + 6 = 12
Step 6: [1,2,3,6,12,24] because 12 + 12 = 24
Step 7: [1,2,3,6,12,24,30] because 24 + 6 = 30
Step 8: [1,2,3,6,12,24,30,42] because 30 + 12 = 42

If using [1, 2, 4, 5, 8, 16, 21, 42]
Step 1: [1]
Step 2: [1,2] because 1 + 1 = 2
Step 3: [1,2,4] because 2 + 2 = 4
Step 4: [1,2,4,5] because 4 + 1 = 5
Step 5: [1,2,4,5,8] because 4 + 4 = 8
Step 6: [1,2,4,5,8,16] because 8 + 8 = 16
Step 7: [1,2,4,5,8,16,21] because 16 + 5 = 21
Step 8: [1,2,4,5,8,16,21,42] because 21 + 21 = 42
"""
print("The shortest addition chain ending with 42 is", str(hitTheNumber(42)))