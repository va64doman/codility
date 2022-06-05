#DwarfsRafting: Find out how many dwarfs can fit on a raft such that it's balanced when crossing a river.
def dwarfRaft(N, S, T):
    quadrant_left_front = (N // 2) * (N // 2)
    quadrant_left_back = (N // 2) * (N // 2)
    quadrant_right_front = (N // 2) * (N // 2)
    quadrant_right_back = (N // 2) * (N // 2)
    boundary = N // 2
    # Compute how many slots are available in each quadrant.
    for barrel in S.split():
        # Adjust to 0-based index.
        row = int(barrel[:-1]) - 1
        column = ord(barrel[-1]) - ord("A")
        if row < boundary:
            # The barrel is in the front.
            if column < boundary:
                # The barrel is in the left.
                quadrant_left_front -= 1
            else:
                # The barrel is in the right.
                quadrant_right_front -= 1
        else:
            # The barrel is in the back.
            if column < boundary:
                # The barrel is in the left.
                quadrant_left_back -= 1
            else:
                # The barrel is in the right.
                quadrant_right_back -= 1
    # lf is short for left front, etc.
    # To keep balance, we need:
    #   1. weight_lf + weight_lb = weight_rf + weight_rb
    #   2. weight_lf + weight_rf = weight_rf + weight_rb
    # Solve the equations and we can get the answer:
    #   1. weight_lf = weight_rb
    #   2. And weight_rf = weight_lb
    allowance_lf = min(quadrant_left_front, quadrant_right_back)
    allowance_rb = min(quadrant_left_front, quadrant_right_back)
    allowance_lb = min(quadrant_left_back, quadrant_right_front)
    allowance_rf = min(quadrant_left_back, quadrant_right_front)
    # Minus the seats, which are already occupied by dwarfs.
    for dwarf in T.split():
        # Adjust to 0-based index.
        row = int(dwarf[:-1]) - 1
        column = ord(dwarf[-1]) - ord("A")
        if row < boundary:
            # The dwarf is in the front.
            if column < boundary:
                # The dwarf is in the left.
                allowance_lf -= 1
                if allowance_lf < 0:    return -1
            else:
                # The dwarf is in the right.
                allowance_rf -= 1
                if allowance_rf < 0:    return -1
        else:
            # The dwarf is in the back.
            if column < boundary:
                # The dwarf is in the left.
                allowance_lb -= 1
                if allowance_lb < 0:    return -1
            else:
                # The dwarf is in the right.
                allowance_rb -= 1
                if allowance_rb < 0:    return -1
    return allowance_lf + allowance_rb + allowance_lb + allowance_rf    
    pass

# (N = 4, S = "1B 1C 4B 1D 2A", T = "3B 2D") = 6
print("N = 4, S = '1B 1C 4B 1D 2A',T = '3B 2D', the number of dwarfs can fit in a raft that is balanced to cross the river is",
      str(dwarfRaft(N = 4, S = "1B 1C 4B 1D 2A", T = "3B 2D")))
