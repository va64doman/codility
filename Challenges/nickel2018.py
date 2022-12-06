# Nickel 2018
# PascalTriangle: Compute the number of "True" values in an OR-Pascal-triangle structure.

def pascalTriangle(P):
    result = 0
    total = len(P) * (len(P) + 1) // 2
    check = True
    for i in range(len(P) - 2):
        if P[i] != P[i+1]:
            check = not check
            break
    if check: result = total
    else:
        check = not check
        for i in range(len(P) - 2):
            if P[i] == P[i+1]:
                check = not check
                break
        if check: return 0
        else:
            groups = buildGroups(P)
            groupsSum = sum(getGroupValue(g) for g in groups)
            result = total - groupsSum
    return min(1000000000, result)
    pass

def buildGroups(P):
    groups = []
    for i in range(len(P)):
        if P[i]: continue
        if i == 0 or P[i-1]: groups.append(Group(1))
        else: groups[-1].length += 1
    return groups
    pass

def getGroupValue(group):
    return group.length * (group.length + 1) // 2
    pass

class Group:
    def __init__(self, length):
        self.length = length
        pass
    pass

# [True, False, False, True, False] = 11
print("[True, False, False, True, False], the number of True values in an OR Pasal triangle is", str(pascalTriangle([True, False, False, True, False])))
# [True, False, False, True] = 7
print("[True, False, False, True], the number of True values in an OR Pasal triangle is", str(pascalTriangle([True, False, False, True])))
