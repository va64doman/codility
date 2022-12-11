# Fury Road
# ScooterRoad: Calculate the minimum time that you need to get through the diversified road to your work.

def cost(scooter, sand):
    costs = [[20,30], [5,40]]
    return costs[scooter][sand]
    pass

def scooterRoad(R):
    N = len(R)
    foot = [0] * (N+1)
    for i in range(N-1,-1,-1): foot[i] = foot[i+1] + cost(False, R[i] == 'S')
    ans = foot[0]
    c = 0
    for i in range(N):
        c += cost(True, R[i] == 'S')
        ans = min(ans, c + foot[i+1])
    return ans
    pass

# "ASAASS" = 115
print("ASAASS, the minimum time that you need to get to work is", str(scooterRoad("ASAASS")))
# "SSA" = 80
print("SSA,the minimum time that you need to get to work is", str(scooterRoad("SSA")))
# "SSSSAAA" = 175
print("SSSSAAA, the minimum time that you need to get to work is", str(scooterRoad("SSSSAAA")))

