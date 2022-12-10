# Palladium 2020
# CoverBuildings: Given N rectangular buildings of width 1, find the minimum total area of two rectangular banners that cover all of the buildings.

def coverBuildings(H):
    N = len(H)
    leftstart, rightstart = [0]*N, [0]*N
    leftstart[0] = H[0]
    rightstart[-1] = H[-1]
    for i in range(1, N):
        if H[i] > leftstart[i-1]:
            leftstart[i] = H[i]
        else:
            leftstart[i] = leftstart[i-1]
        if H[N-i-1] > rightstart[N-i]:
            rightstart[N-i-1] = H[N-i-1]
        else:
            rightstart[-i-1] = rightstart[-i]
    res = rightstart[0]*N
    for i in range(1, N):
        res = min(res, leftstart[i-1]*i + rightstart[i]*(N-i))
    return res
    pass

# [3,1,4] = 10
print("[3,1,4], the minimum total area of two rectangular banners that cover all of the buildings is", str(coverBuildings([3,1,4])))
# [5,3,2,4] = 17
print("[5,3,2,4], the minimum total area of two rectangular banners that cover all of the buildings is", str(coverBuildings([5,3,2,4])))
# [5,3,5,2,1] = 19
print("[5,3,5,2,1], the minimum total area of two rectangular banners that cover all of the buildings is", str(coverBuildings([5,3,5,2,1])))
# [7,7,3,7,7] = 35
print("[7,7,3,7,7], the minimum total area of two rectangular banners that cover all of the buildings is", str(coverBuildings([7,7,3,7,7])))
# [1,1,7,6,6,6] = 30
print("[1,1,7,6,6,6], the minimum total area of two rectangular banners that cover all of the buildings is", str(coverBuildings([1,1,7,6,6,6])))
