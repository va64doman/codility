# Bromum 2018
# Buckets: Given N buckets and M colored balls to put in them, find the earliest moment when some bucket contains Q balls of the same color.

def buckets(N, Q, B, C):
    import collections
    if Q > len(C) or B is None or len(B) == 0 or C is None or len(C) == 0:
        return -1
    buckets = collections.defaultdict(dict)
    for i in range(len(B)):
        color = C[i]
        bucket = B[i]
        buckets[bucket][color] = buckets[bucket].get(color, 0) + 1
        if buckets[bucket][color] == Q:
            return i
    return -1
    pass

# (N = 3, Q = 2, B = [1, 2, 0, 1, 1, 0, 0, 1], C = [0, 3, 0, 2, 0, 3, 0, 0]) = 4
print("N = 3, Q = 2, B = [1, 2, 0, 1, 1, 0, 0, 1], C = [0, 3, 0, 2, 0, 3, 0, 0], the earliest moment when some buck contains Q balls of the same color is",
      str(buckets(N = 3, Q = 2, B = [1, 2, 0, 1, 1, 0, 0, 1], C = [0, 3, 0, 2, 0, 3, 0, 0])))
# (N = 2, Q = 2, B = [0, 1], C = [5, 5]) = -1
print("N = 2, Q = 2, B = [0, 1], C = [5, 5], the earliest moment when some buck contains Q balls of the same color is",
      str(buckets(N = 2, Q = 2, B = [0, 1], C = [5, 5])))
# (N = 2, Q = 2, B = [0, 1, 0, 1, 0, 1], C = [1, 3, 0, 0, 3, 3]) = 5
print("N = 2, Q = 2, B = [0, 1, 0, 1, 0, 1], C = [1, 3, 0, 0, 3, 3], the earliest moment when some buck contains Q balls of the same color is",
      str(buckets(N = 2, Q = 2, B = [0, 1, 0, 1, 0, 1], C = [1, 3, 0, 0, 3, 3])))
