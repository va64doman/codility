# Technetium 2019
# MaxPathFromTheLeftTopCorner: Find a maximal value path in a matrix, starting in the top-left corner and ending in the bottom-right corner.

def maxPathFromTheLeftTopCorner(A):
    N, M = len(A), len(A[0])
    path = set([(0,0)])
    res = str(A[0][0])
    for i in range(2, N+M):
        new_path = []
        max_n = 0
        for p1, p2 in path:
            if p1<N-1 and p2<M-1:
                a, b = A[p1][p2+1], A[p1+1][p2]
                if a>b:
                    if a>max_n:
                        max_n = a
                        new_path = [(p1, p2+1)]
                    elif a==max_n:
                        new_path.append((p1, p2+1))
                elif a<b:
                    if b>max_n:
                        max_n = b
                        new_path = [(p1+1, p2)]
                    elif b==max_n:
                        new_path.append((p1+1, p2))
                else:
                    if a>max_n:
                        max_n = a
                        new_path = [(p1, p2+1), (p1+1, p2)]
                    elif a==max_n:
                        new_path.append((p1, p2+1))
                        new_path.append((p1+1, p2))
            elif p1<N-1 and p2==M-1:
                b = A[p1+1][p2]
                if b>max_n:
                    max_n = b
                    new_path = [(p1+1, p2)]
                elif b==max_n:
                    new_path.append((p1+1, p2))
            elif p1==N-1 and p2<M-1:
                a = A[p1][p2+1]
                if a>max_n:
                    max_n = a
                    new_path = [(p1, p2+1)]
                elif a==max_n:
                    new_path.append((p1, p2+1))
        path = set(new_path)
        res += str(max_n)
    return res
    pass

# [[9,9,7], [9,7,2], [6,9,5], [9,1,2]] = "997952"
print("[[9,9,7], [9,7,2], [6,9,5], [9,1,2]], the maximal value path is", maxPathFromTheLeftTopCorner([[9,9,7], [9,7,2], [6,9,5], [9,1,2]]))
