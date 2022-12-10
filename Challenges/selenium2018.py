# Selenium 2018
# SprinklersArrangement: Count the minimum number of moves required to rearrange sprinklers so as to maximize the number of farmland fields that get watered.

from collections import defaultdict
 
def get_minmoves(l):
    keys = list(range(1,len(l)+1))
    d = defaultdict(int)
    list_repeated = []   
    for num in l:
        if num in d: list_repeated.append(num)
        else: d[num] += 1   
    result = sum(([abs(x1 - x2) for (x1, x2) in zip(sorted(list_repeated), sorted(set(keys) - set(d.keys())))]))
    return result
    pass
    
def sprinkletsArrangement(X, Y):
    return(get_minmoves(X) + get_minmoves(Y)) % 1000000007
    pass

# (X = [1, 2, 2, 3, 4], Y = [1, 1, 4, 5, 4]) = 5
print("X = [1, 2, 2, 3, 4], Y = [1, 1, 4, 5, 4], the minimum number of moves required to rearrange sprinklers ",
      "so as to maximize the number of farmland fields that get watered is", str(sprinkletsArrangement(X = [1, 2, 2, 3, 4], Y = [1, 1, 4, 5, 4])))
# (X = [1, 1, 1, 1], Y = [1, 2, 3, 4]) = 6
print("X = [1, 1, 1, 1], Y = [1, 2, 3, 4], the minimum number of moves required to rearrange sprinklers ",
      "so as to maximize the number of farmland fields that get watered is", str(sprinkletsArrangement(X = [1, 1, 1, 1], Y = [1, 2, 3, 4])))
# (X = [1, 1, 2], Y = [1, 2, 1]) = 4
print("X = [1, 1, 2], Y = [1, 2, 1], the minimum number of moves required to rearrange sprinklers ",
      "so as to maximize the number of farmland fields that get watered is", str(sprinkletsArrangement(X = [1, 1, 2], Y = [1, 2, 1])))
