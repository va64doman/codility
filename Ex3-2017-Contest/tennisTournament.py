#TennisTournament: Given the numbers of players and available courts, calculate the maximum number of parallel tennis games.
def tennisTour(P,C):
    return min(P // 2, C)
    pass

#(P = 5, C = 3) = 2
#(P = 10, C = 3) = 3

print("5 players, 3 courts, the maximum number of parallel tennis games is", str(tennisTour(5,3)))
print("10 players, 3 courts, the maximum number of parallel tennis games is", str(tennisTour(10,3)))
