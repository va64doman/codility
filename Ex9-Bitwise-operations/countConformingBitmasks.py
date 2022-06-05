#CountConformingBitmasks: Count 30-bit bitmasks conforming to at least one of three given 30-bit bitmasks.
def countConformingBitmasks(A, B, C):
    common = confs(A | B) + confs(A | C) + confs(B | C) - confs(A | B | C)
    return confs(A) + confs(B) + confs(C) - common
    pass

def confs(N):
    return 1 << zeros(N)
    pass

def zeros(N):
    res = 0
    for i in range(30):
        if N % 2 == 0:
            res += 1
        N >>= 1
    return res

#(A = 1073741727, B = 1073741631, C = 1073741679) = 8
print("(A = 1073741727, B = 1073741631, C = 1073741679), the number of 30-bit bitmasks conforming to at least one of 3 given 30-bit bitmasks is",
      str(countConformingBitmasks(A = 1073741727, B = 1073741631, C = 1073741679)))
