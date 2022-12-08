# Gallium 2018
# MaxZeroProduct: Given an array of integers, compute the maximum number of zeroes at the end of the product of some three elements of the array.

def maxZeroProduct(A):
    m51 = [-1] * 32
    m52 = [-1] * 64
    m53 = [-1] * 96
    for i in range(len(A)):
        ai = A[i]
        p2 = 0
        while ai & 1 == 0:
            p2 += 1
            ai >>= 1
        p5 = 0
        while ai % 5 == 0:
            p5 += 1
            ai //= 5
        for j in range(64):
            if m52[j] != -1 and (m52[j] + p5) > m53[j+p2]: m53[j+p2] = m52[j] + p5
        for j in range(32):
            if m51[j] != -1 and (m51[j] + p5) > m52[j+p2]: m52[j+p2] = m51[j] + p5
        if p5 > m51[p2]: m51[p2] = p5
    max0 = 0
    for i in range(96):
        z3 = i if i < m53[i] else m53[i]
        max0 = max(max0, z3)
    return max0    
    pass

# [7, 15, 6, 20, 5, 10] = 3
print("[7, 15, 6, 20, 5, 10], the maximum number of zeros at the end of the product is", str(maxZeroProduct([7, 15, 6, 20, 5, 10])))
# [25, 10, 25, 10, 32] = 4
print("[25, 10, 25, 10, 32], the maximum number of zeros at the end of the product is", str(maxZeroProduct([25, 10, 25, 10, 32])))
