#Nesting: Determine whether a given string of parentheses (single type) is properly nested.
def nesting(S):
    p = 0
    for i in range(0, len(S)):
        if S[i] == '(':
            p += 1
        elif S[i] == ')':
            p -= 1
        if p < 0:
            return 0
    if p != 0:
        return 0
    else:
        return 1
    pass

# (()(())()) = 1
# ()) = 0
print("(()(())()) is ", 'nesting' if nesting("(()(())())") == 1 else 'not nesting')
print("()) is ", 'nesting' if nesting("())") == 1 else 'not nesting')
