# Zirconium 2019
# DreamTeam: Divide developers into two teams to maximize their total contribution.

def dreamTeam(A, B, F):
    N = len(A)
    V = []
    for i in range(N):
        V.append([A[i], B[i], A[i]-B[i]])
    V.sort(key=lambda x:x[2], reverse=True)
    res = 0
    for i in range(F):
        res += V[i][0]
    for i in range(F, N):
        res += V[i][1]
    return res
    pass

# (A = [4, 2, 1], B = [2, 5, 3], F = 2) = 10
print("A = [4, 2, 1], B = [2, 5, 3], F = 2, the maximum sum of contribution is", str(dreamTeam(A = [4, 2, 1], B = [2, 5, 3], F = 2)))
# (A = [7, 1, 4, 4], B = [5, 3, 4, 3], F = 2) = 18
print("A = [7, 1, 4, 4], B = [5, 3, 4, 3], F = 2, the maximum sum of contribution is", str(dreamTeam(A = [7, 1, 4, 4], B = [5, 3, 4, 3], F = 2)))
# (A = [5, 5, 5], B = [5, 5, 5], F = 1) = 15
print("A = [5, 5, 5], B = [5, 5, 5], F = 1, the maximum sum of contribution is", str(dreamTeam(A = [5, 5, 5], B = [5, 5, 5], F = 1)))
