# Frog jump: Minimal number of jumps from X to Y in D jumps.
def frogJump(X, Y, D):
    # Find the integer division between difference of X and Y by D jumps.
    v = (Y - X) // D
    # If the jumps by v times exceeds or land on Y, then it required v times, otherwise v+1 times.
    if X + v * D >= Y:
        return v
    else:
        return v + 1
    pass

# (10,85,30) = 3
print("From 10 to 85 by 30 jumps, the minimal number of jumps is " + str(frogJump(10,85,30)))


