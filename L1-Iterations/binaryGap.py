# Binary gap: Find maximum consecutive 0s between both 1 ends
def binaryGap(N):
    # Ignore the first two characters (0b) from the binary conversion.
    N = bin(N)[2:]
    b = 0
    maxb = 0
    for k in N:
        # If there is 0 even if it continues, add the total number of 0s from the current gap.
        # It will not affect the maximum number of binary gap if 0s are not surrounded by 1s at both ends.
        if int(k) == 0:
            b += 1
        # Unless there is a 1, check if the current binary gap is larger than the previous gap.
        elif int(k) == 1:
            maxb = max(b, maxb)
            b = 0
    return maxb
    pass

# 9 = 1001, bg = 2
# 529 = 1000010001, bg = 4
# 20 = 10100, bg = 1
# 15 = 1111, bg = 0
# 32 = 10000, bg = 0
# 1041 = 100000100001, bg = 5
print("The binary gap of 9 or binary(" + str(bin(9)[2:]) + ") is " + str(binaryGap(9)) + ".")
print("The binary gap of 529 or binary(" + str(bin(529)[2:]) + ") is " + str(binaryGap(529)) + ".")
print("The binary gap of 20 or binary(" + str(bin(20)[2:]) + ") is " + str(binaryGap(20)) + ".")
print("The binary gap of 15 or binary(" + str(bin(15)[2:]) + ") is " + str(binaryGap(15)) + ".")
print("The binary gap of 32 or binary(" + str(bin(32)[2:]) + ") is " + str(binaryGap(32)) + ".")
print("The binary gap of 1041 or binary(" + str(bin(1041)[2:]) + ") is " + str(binaryGap(1041)) + ".")
