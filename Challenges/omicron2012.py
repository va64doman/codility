# Omicron 2012
# PowerFib: Given integers A and B, calculate Fib(A ** B) % 10000103.
"""
F(0) = 0
F(1) = 1
F(N) = F(N−1) + F(N−2) for N >= 2
"""
MOD = 10000103
"""
Use of modulo 10 000 103 not only simplifies arithmetical operations: for any P > 0, the
sequence (Fib(i) mod P) is periodic. It follows from the fact that values of Fib(i) mod P and
Fib(i+1) mod P fully determine the following elements of this sequence, and there are at most
P^2 different pairs of such values.
In particular, for P = 10 000 103 the sequence (Fib(i) mod P) has period T = 20 000 208.
"""
T = 20000208

def mul(x, y, M):
    return x * y % M
    pass

def add(x, y, M):
    x += y
    return x if x < M else x - M
    pass

def mulmatrix(a, b):
    c = [0] * 2
    for i in range(2):
        c[i] = [0] * 2
    for i in range(2):
        for j in range(2):
            c[i][j] = 0
            for k in range(2):
                c[i][j] = add(c[i][j], mul(a[i][k], b[k][j], MOD), MOD)
    return c            
    pass

def make(a, b):
    for i in range(2):
        for j in range(2):
            a[i][j] = b[i][j]
    pass

def powerFib(N, M):
    p = 1
    x = N
    while M:
        if M & 1:
            p = mul(p,x,T)
        x = mul(x,x,T)
        M >>= 1
    p -= 1
    if p == 0:
        return 0
    a = [0] * 2
    b = [0] * 2
    for i in range(2):
        a[i] = [0] * 2
        b[i] = [0] * 2
    a[0][0] = a[1][1] = b[0][1] = b[1][0] = b[1][1] = 1
    while p:
        if p & 1:
            c = mulmatrix(a,b)
            make(a,c)
        c = mulmatrix(b,b)
        make(b,c)
        p >>= 1
    return a[1][1]
    pass
# (N = 2, M = 3) = 21
print("N = 2 and M = 3, (F(2^3) = F(8)) % 10000103 =", str(powerFib(2,3)))