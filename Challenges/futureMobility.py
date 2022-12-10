# Future Mobility
# Stones: Given N towers of stones, move stones between towers in order to get
# a requested number of stones on each tower, in a minimum number of moves.

def stones(A, B):
    if sum(A) != sum(B):
        return -1    
    diff = []    
    for i in range(len(A)):
        diff.append(A[i] - B[i])
    result = 0
    for i in range(len(diff)):
        if diff[i] == 0:
            continue
        else:
            result += abs(diff[i])
            if diff[i] > 0:
                if diff[i + 1] < 0:
                    diff[i], diff[i + 1] = max(diff[i] + diff[i + 1], 0), min(diff[i] + diff[i + 1], 0)
                    if diff[i]:
                        diff[i + 2] += diff[i]
                else:
                    diff[i + 2] += diff[i]
            else:
                if diff[i + 1] > 0:
                    diff[i], diff[i + 1] = min(diff[i] + diff[i + 1], 0), max(diff[i] + diff[i + 1], 0)
                    if diff[i]:
                        diff[i + 2] += diff[i]
                else:
                    diff[i + 2] += diff[i]        
        diff[i] = 0
    return result % (10 ** 9 + 7)
    pass

# (A = [1, 1, 2, 4, 3], B = [2, 2, 2, 3, 2]) = 3
print("A = [1, 1, 2, 4, 3], B = [2, 2, 2, 3, 2], the minimum number of moves is", str(stones(A = [1, 1, 2, 4, 3], B = [2, 2, 2, 3, 2])))
# (A = [0, 0, 2, 1, 8, 8, 2, 0], B = [8, 5, 2, 4, 0, 0, 0, 2]) = 31
print("A = [0, 0, 2, 1, 8, 8, 2, 0], B = [8, 5, 2, 4, 0, 0, 0, 2], the minimum number of moves is", str(stones(A = [0, 0, 2, 1, 8, 8, 2, 0], B = [8, 5, 2, 4, 0, 0, 0, 2])))
# (A = [10**9, 10**9, 10**9, 0, 0, 0], B = [0, 0, 0, 10**9, 10**9, 10**9]) = 999999972
print("A = [10**9, 10**9, 10**9, 0, 0, 0], B = [0, 0, 0, 10**9, 10**9, 10**9], the minimum number of moves is", str(stones(A = [10**9, 10**9, 10**9, 0, 0, 0], B = [0, 0, 0, 10**9, 10**9, 10**9])))
# (A = [2], B = [1]) = -1
print("A = [2], B = [1], the minimum number of moves is", str(stones(A = [2], B = [1])))
