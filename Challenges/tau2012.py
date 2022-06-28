# Tau 2012
# TorusLot: Find a maximum-sum rectangular area in a matrix.
def torus_lot(C):
    Res = 0
    M = len(C)
    N = len(C[0])
    if M > N:
        # Transpose C
        C1 = [([0] * M)] * N
        for j in range(N):
            C1[j] = C1[j][:]
            for i in range(M):
                C1[j][i] = C[i][j]
        C = C1
        M = len(C)
        N = len(C[0])
    # sum[i][j] = profit of a rectangle [0..i-1]x[0..j-1]
    sum = [([0] * (N+1))] * (M+1)
    for i in range(1, M+1):
        sum[i] = sum[0][:]
        for j in range(1, N+1):
            sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + C[i-1][j-1]
    Res = 0 # Maximum profit of a rectangle
    for i1 in range(M):
        for i2 in range(i1+1, M+1):
            Min1 = 0 # Minimum profit of a rectangle [i1..i2-1]x[0..j-1]
            MinJ1 = 0 # Maximum such j
            MaxP1 = 0 # Maximum profit of a rectangle [i1..i2-1]x[j’..j-1]
            Max1 = 0 # Maximum profit of a rectangle [i1..i2-1]x[0..j-1]
            MaxJ1 = 0 # Minimum such j
            MinC1 = 0 # Minimum profit of a rectangle [i1..i2-1]x[j’..j-1]
            Min2 = 0 # Minimum profit of a rectangle [0..i1-1,i2..M-1]x[0..j-1]
            MinJ2 = 0 # Maximum such j
            MaxP2 = 0 # Maximum profit of a rectangle [0..i1-1,i2..M-1]x[j’..j-1]
            Max2 = 0 # Maximum profit of a rectangle [0..i1-1,i2..M-1]x[0..j-1]
            MaxJ2 = 0 # Minimum such j
            MinC2 = 0 # Minimum profit of a rectangle [0..i1-1,i2..M-1]x[j’..j-1]
            for j in range(1,N+1):
                Profit1 = sum[i2][j] - sum[i1][j]
                if Profit1 <= Min1:
                    Min1 = Profit1
                    MinJ1 = j
                if (Profit1 - Min1 > MaxP1):
                    MaxP1 = Profit1 - Min1
                if Profit1 > Max1:
                    Max1 = Profit1
                    MaxJ1 = j
                if (Profit1 - Max1 < MinC1):
                    MinC1 = Profit1 - Max1
                Profit2 = sum[M][j] - Profit1
                if Profit2 <= Min2:
                    Min2 = Profit2
                    MinJ2 = j
                if (Profit2 - Min2 > MaxP2):
                    MaxP2 = Profit2 - Min2
                if Profit2 > Max2:
                    Max2 = Profit2
                    MaxJ2 = j
                if (Profit2 - Max2 < MinC2):
                    MinC2 = Profit2 - Max2
            Res = max(Res, MaxP1, MaxP2, Profit1 - MinC1,Profit2 - MinC2)
    return Res
    pass

# [[1,-1,2],[-1,-1,-1],[3,-1,4]] = 10
C = [[1,-1,2],[-1,-1,-1],[3,-1,4]]
print("[[1,-1,2],[-1,-1,-1],[3,-1,4]], the maximum-sum rectangular area is", str(torus_lot(C)))
# [[1,-3],[-2,3]] = 3
C = [[1,-3],[-2,3]]
print("[[1,-3],[-2,3]], the maximum-sum rectangular area is", str(torus_lot(C)))