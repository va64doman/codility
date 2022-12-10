# Niobium 2019
# FlippingMatrix: A matrix of binary values is given. We can flip the values in selected columns.
# What is the maximum number of rows that we can obtain that contain all the same values?

def flippingMatrix(A):
    N = len(A)    
    def transform(arr):
        s1 = ''.join(str(a) for a in arr)
        s2 = ''.join(str(a^1) for a in arr)
        return max(s1, s2)
        pass
    record = {}
    for i in range(N):
        temp = transform(A[i])
        if temp in record:
            record[temp] += 1
        else:
            record[temp] = 1    
    res = 0
    for key in record:
        res = max(res, record[key])    
    return res
    pass

# [[0,0,0,0], [0,1,0,0], [1,0,1,1]] = 2
print("[[0,0,0,0], [0,1,0,0], [1,0,1,1]], the maximum number of rows that we can obtain that contain all the same values is",
      str(flippingMatrix([[0,0,0,0], [0,1,0,0], [1,0,1,1]])))
# [[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]] = 4
print("[[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]], the maximum number of rows that we can obtain that contain all the same values is",
      str(flippingMatrix([[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]])))
