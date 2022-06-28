# Upsilon 2012
# CartesianSequence: Find the longest path down the Cartesian tree.
INFTY = 2000000000

def cartesianSequence(A):
    N = len(A)
    if N == 0: return 0
    A = A + [INFTY - 1]
    v_stack = [INFTY] * (N + 2)
    h_stack = [0] * (N + 2)
    sp = 1
    for X in A:
        if X > v_stack[sp]:
            # Elements smaller than X on the stack will form its left sub-tree
            while X > v_stack[sp - 1]:
                # merge two elements on top of the stack
                h_stack[sp - 1] = max(h_stack[sp - 1], h_stack[sp] + 1)
                sp = sp-1
            # Element on top of the stack represents left sub-tree of x
            v_stack[sp] = X
            h_stack[sp] = h_stack[sp] + 1
        else:
            # X is a leaf
            sp = sp + 1
            v_stack[sp] = X
            h_stack[sp] = 0
    assert sp == 2
    return h_stack[sp]
    pass

  # [9,10,2,-1,3,-5,0,-3,1,12,5,8,-2,6,4] = 6
print("[9,10,2,-1,3,-5,0,-3,1,12,5,8,-2,6,4], the sequence of length is",str(cartesianSequence([9,10,2,-1,3,-5,0,-3,1,12,5,8,-2,6,4])))