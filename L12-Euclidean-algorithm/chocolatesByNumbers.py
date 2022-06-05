#ChocolatesByNumbers: There are N chocolates in a circle. Count the number of chocolates you will eat.
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
    pass

def chocByNums(N, M):
    return int(N / gcd(N, M))
    pass

# (N = 10, M = 4) = 5
print("N = 10, M = 4, the number of chocolates eaten is", str(chocByNums(10,4)))
