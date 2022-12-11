# The Great Code Off 2021
# CakeFactory: Count the number of cakes consisting of K different layers in the order 1, 2, ..., K
# that will be created after a sequence of operations of putting a layer on some interval.

def cakeFactory(N, K, A, B, C):
    base = 1
    while base < N: base *= 2
    tree = [(0,0)] * (base * 2)

    def combine(p1, p2):
        c1, s1 = p1
        c2, s2 = p2
        if s1 == -1 or s2 == -1: return (0, -1)
        elif s1 == 0: return p2
        elif s2 == 0: return p1
        elif c1 + s1 == c2: return (c1, s1 + s2)
        else: return (0, -1)
        pass

    def tree_add(v, xl, xr, a, b, c):
        if b < xl or xr < a: return
        elif a <= xl and xr <= b: tree[v] = combine(tree[v], (c,1))
        else:
            tree[2*v] = combine(tree[2*v], tree[v])
            tree[2*v+1] = combine(tree[2*v+1], tree[v])
            tree[v] = (0,0)
            xm = (xl + xr) // 2
            tree_add(2*v, xl, xm, a, b, c)
            tree_add(2*v+1, xm+1, xr, a, b, c)
        pass
    
    for a,b,c in zip(A, B, C):
        tree_add(1, 0, base-1, a-1, b-1, c)

    def tree_count(v):
        if v >= base:
            c, s = tree[v]
            return int(c == 1 and s == K)
        else:
            tree[2*v] = combine(tree[2*v], tree[v])
            tree[2*v+1] = combine(tree[2*v+1], tree[v])
            return tree_count(2*v) + tree_count(2*v+1)
        pass
    
    return tree_count(1)
    pass

# (N = 5, K = 3, A = [1, 1, 4, 1, 4], B = [5, 2, 5, 5, 4], C = [1, 2, 2, 3, 3]) = 3
print("N = 5, K = 3, A = [1, 1, 4, 1, 4], B = [5, 2, 5, 5, 4], C = [1, 2, 2, 3, 3], the number of well-prepared cakes after executing the sequence of instructions is",
      str(cakeFactory(N = 5, K = 3, A = [1, 1, 4, 1, 4], B = [5, 2, 5, 5, 4], C = [1, 2, 2, 3, 3])))
# (N = 6, K = 4, A = [1, 2, 1, 1], B = [3, 3, 6, 6], C = [1, 2, 3, 4]) = 2
print("N = 6, K = 4, A = [1, 2, 1, 1], B = [3, 3, 6, 6], C = [1, 2, 3, 4], the number of well-prepared cakes after executing the sequence of instructions is",
      str(cakeFactory(N = 6, K = 4, A = [1, 2, 1, 1], B = [3, 3, 6, 6], C = [1, 2, 3, 4])))
# (N = 3, K = 2, A = [1, 3, 3, 1, 1], B = [2, 3, 3, 1, 2], C = [1, 2, 1, 2, 2]) = 1
print("N = 3, K = 2, A = [1, 3, 3, 1, 1], B = [2, 3, 3, 1, 2], C = [1, 2, 1, 2, 2], the number of well-prepared cakes after executing the sequence of instructions is",
      str(cakeFactory(N = 3, K = 2, A = [1, 3, 3, 1, 1], B = [2, 3, 3, 1, 2], C = [1, 2, 1, 2, 2])))
# (N = 5, K = 2, A = [1, 1, 2], B = [5, 5, 3], C = [1, 2, 1]) = 3
print("N = 5, K = 2, A = [1, 1, 2], B = [5, 5, 3], C = [1, 2, 1], the number of well-prepared cakes after executing the sequence of instructions is",
      str(cakeFactory(N = 5, K = 2, A = [1, 1, 2], B = [5, 5, 3], C = [1, 2, 1])))
