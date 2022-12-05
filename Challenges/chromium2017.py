# Chromium 2017
# ZigZagEscape: Given a sequence S of integers, find a number of increasing sequences I such that every two consecutive elements in I appear in S,
# but on the opposite sides of the first element of I.

def zigZagEscape(H):
    MOD = 1000000007
    N = len(H)
    order = [0] * N
    mask32 = (1 << 16) - 1
    for i in range(N):
        order[i] = (H[i] << 16) + i
    order.sort()
    
    for i in range(N):
        H[order[i] & mask32] = N - i - 1

    hs2p = 1
    while N > hs2p:
        hs2p <<= 1

    m00 = [0] * (hs2p << 1)
    m01 = [0] * (hs2p << 1)
    m10 = [0] * (hs2p << 1)
    m11 = [0] * (hs2p << 1)
    for i in range(hs2p, 2 * hs2p):
        m00[i] = 1
        m01[i] = 1
        m10[i] = 0
        m11[i] = 1

    im = hs2p >> 1
    while im > 0:
        for i in range(im, im << 1):
            L = 2 * i
            R = L + 1
            m00[i] = (m00[L] * m00[R] + m01[L] * m10[R]) % MOD
            m01[i] = (m00[L] * m01[R] + m01[L] * m11[R]) % MOD
            m10[i] = (m10[L] * m00[R] + m11[L] * m10[R]) % MOD
            m11[i] = (m10[L] * m01[R] + m11[L] * m11[R]) % MOD
        im >>= 1

    nChoice = 1
    for i in range(N):
        irang = hs2p + H[i] - 1
        if H[i] > 0:
            psind = irang
            LL = m00[irang]
            LR = m01[irang]
            RL = m10[irang]
            RR = m11[irang]
            if psind & 1 == 1:
                tLL = LL
                tLR = LR
                tRL = RL
                tRR = RR
                L = psind ^ 1
                LL = (m00[L] * tLL + m01[L] * tRL) % MOD
                LR = (m00[L] * tLR + m01[L] * tRR) % MOD
                RL = (m10[L] * tLL + m11[L] * tRL) % MOD
                RR = (m10[L] * tLR + m11[L] * tRR) % MOD
            psind >>= 1
            
            while psind > 1:
                if psind & 1 == 1:
                    tLL = LL
                    tLR = LR
                    tRL = RL
                    tRR = RR
                    L = psind ^ 1
                    LL = (m00[L] * tLL + m01[L] * tRL) % MOD
                    LR = (m00[L] * tLR + m01[L] * tRR) % MOD
                    RL = (m10[L] * tLL + m11[L] * tRL) % MOD
                    RR = (m10[L] * tLR + m11[L] * tRR) % MOD
                psind >>= 1
            nChoice = nChoice + LL + LR + RL + RR - 1
            while nChoice >= MOD:
                nChoice -= MOD
        m01[irang + 1] = 0
        m10[irang + 1] = 1
        psind = (irang + 1) >> 1
        while psind > 0:
            L = psind << 1
            R = L + 1
            m00[psind] = (m00[L] * m00[R] + m01[L] * m10[R]) % MOD
            m01[psind] = (m00[L] * m01[R] + m01[L] * m11[R]) % MOD
            m10[psind] = (m10[L] * m00[R] + m11[L] * m10[R]) % MOD
            m11[psind] = (m10[L] * m01[R] + m11[L] * m11[R]) % MOD
            psind >>= 1
    return nChoice
    pass

# [13, 2, 5] = 7
print("[13, 2, 5], the number of possibilities 1000000007 is", str(zigZagEscape([13, 2, 5])))
# [4, 6, 2, 1, 5] = 23
print("[4, 6, 2, 1, 5], the number of possibilities 1000000007 is", str(zigZagEscape([4, 6, 2, 1, 5])))
