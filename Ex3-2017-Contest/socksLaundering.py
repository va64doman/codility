#SocksLaundering: From drawers containing both clean and dirty socks, choose socks to launder in order to obtain the maximum number of clean pairs of socks.
def socksLaunder(K, C, D):
    res = 0
    clean = [0] * 51
    dirty = [0] * 51
    for sock in C:
        clean[sock] += 1
    for sock in D:
        dirty[sock] += 1
    for i in range(1, 51):
        res += clean[i] // 2
        if clean[i] % 2 != 0 and K > 0 and dirty[i] > 0:
            res += 1
            K -= 1
            dirty[i] -= 1
    for i in range(1, 51):
        if K <= 1:
            break
        if dirty[i] >= 2:
            dirty[i] = min(dirty[i] // 2, K // 2)
            res += dirty[i]
            K -= 2 * dirty[i]
    return res
    pass

#(K = 2, C = [1, 2, 1, 1] and D = [1, 4, 3, 2, 4]) = 3
print("(K = 2, C = [1, 2, 1, 1] and D = [1, 4, 3, 2, 4]), the maximum number of clean pairs of socks:", str(socksLaunder(K = 2, C = [1, 2, 1, 1], D = [1, 4, 3, 2, 4])))
