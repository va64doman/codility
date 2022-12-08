# Zinc 2018
# TheaterTickets: Given an array A, count the number of different triplets (a, b, c) in which a occurs before b and b occurs before c.

def theaterTickets(A):
    combinations = {}
    combinationsOfOne = 0
    combinationsOfTwo = 0
    combinationsOfThree = 0
    length = len(A)
    for i in range(length):
        currentCombinationsOfTwo = combinationsOfOne
        if A[i] not in combinations:
            combinations[A[i]] = [0,0]
            combinationsOfOne += 1
        currentCombinationsOfThree = combinationsOfTwo
        combinationsOfTwo += currentCombinationsOfTwo - combinations[A[i]][0]
        combinations[A[i]][0] = currentCombinationsOfTwo
        combinationsOfThree += currentCombinationsOfThree - combinations[A[i]][1]
        combinations[A[i]][1] = currentCombinationsOfThree
        combinationsOfThree %= 1000000007
    return combinationsOfThree
    pass

# [1, 2, 1, 1] = 3
print("[1, 2, 1, 1], the number of different triplets (a,b,c) in which a occurs before b and b occurs before c is", str(theaterTickets([1, 2, 1, 1])))
# [1, 2, 3, 4] = 4
print("[1, 2, 3, 4], the number of different triplets (a,b,c) in which a occurs before b and b occurs before c is", str(theaterTickets([1, 2, 3, 4])))
# [2, 2, 2, 2] = 1
print("[2, 2, 2, 2], the number of different triplets (a,b,c) in which a occurs before b and b occurs before c is", str(theaterTickets([2, 2, 2, 2])))
# [2, 2, 1, 2, 2] = 4
print("[2, 2, 1, 2, 2], the number of different triplets (a,b,c) in which a occurs before b and b occurs before c is", str(theaterTickets([2, 2, 1, 2, 2])))
