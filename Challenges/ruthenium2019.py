# Ruthenium 2019
# ReplacingBooks: Given a list of integers, return the maximum number of consecutive integers equal to each other after replacing at most K of them.

from collections import defaultdict as dfd
def replacingBooks(A, K):
    if len(A) <= K:
        return len(A)
    res = 0
    tail = 0
    book = dfd(int)
    M = 0
    for i in range(len(A)):
        book[A[i]] += 1
        M = max(M, book[A[i]])
        if M+K <= res:
            book[A[tail]] -= 1
            tail += 1
        else:
            res += 1
    return res
    pass

# (A = [1, 1, 3, 4, 3, 3, 4], K = 2) = 5
print("A = [1, 1, 3, 4, 3, 3, 4], K = 2, the maximum number of consecutive integers equal to each other after replacing at most K of them is",
      str(replacingBooks(A = [1, 1, 3, 4, 3, 3, 4], K = 2)))
# (A = [4, 5, 5, 4, 2, 2, 4], K = 0) = 2
print("A = [4, 5, 5, 4, 2, 2, 4], K = 0, the maximum number of consecutive integers equal to each other after replacing at most K of them is",
      str(replacingBooks(A = [4, 5, 5, 4, 2, 2, 4], K = 0)))
# (A = [1, 3, 3, 2], K = 2) = 4
print("A = [1, 3, 3, 2], K = 2, the maximum number of consecutive integers equal to each other after replacing at most K of them is",
      str(replacingBooks(A = [1, 3, 3, 2], K = 2)))

