#Fish: N voracious fish are moving along a river. Calculate how many fish are alive.
def fish(A, B):
    ds = []
    c = 0
    for i in range(0, len(B)):
        if B[i] == 1:
            ds.append(A[i])
        else:
            while len(ds) != 0:
                if ds[-1] > A[i]:
                    c += 1
                    break
                elif ds[-1] < A[i]:
                    ds.pop()
                    c += 1
    return len(A) - c
    pass

# (A = [4,3,2,1,5] B = [0,1,0,0,0]) = 2
# 0 in B = upstream, 1 in B = downstream
# If two fish swim in opposite direction, the big fish eats little fish, cannot be same size.

print("[4,3,2,1,5] fish go in direction [0,1,0,0,0]. Only", str(fish([4,3,2,1,5],[0,1,0,0,0])), "fish alive.")
