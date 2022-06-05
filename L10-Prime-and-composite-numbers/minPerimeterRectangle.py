#MinPerimeterRectangle: Find the minimal perimeter of any rectangle whose area equals N.
def minPeriRect(N):
    for i in range(int(N**0.5), 0, -1):
        if N % i == 0:
            return int(2 * (i+N/i))
    pass

# 30 = 22
print("Area is 30, minimal perimeter is", str(minPeriRect(30)))
