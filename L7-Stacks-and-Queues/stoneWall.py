#StoneWall: Cover "Manhattan skyline" using the minimum number of rectangles.
def stoneWall(H):
    last = 0
    c = 0
    S = []
    for i in range(0, len(H)):
        if H[i] > last:
            last = H[i]
            c += 1
            S.append(H[i])
        elif H[i] < last:
            while len(S) > 0 and H[i] < S[-1]:
                S.pop()
            if len(S) == 0 or H[i] != S[-1]:
                c += 1
                S.append(H[i])
            last = H[i]
    return c
    pass

# [8,8,5,7,9,8,7,4,8] = 7
print("[8,8,5,7,9,8,7,4,8], the minimum number of blocks in 9 metres long is", str(stoneWall([8,8,5,7,9,8,7,4,8])))
