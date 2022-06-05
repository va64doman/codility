#RectangleBuilderGreaterArea: Count the distinct rectangle sizes, of area greater than or equal to X, that can be built out of a given set of segments.
def rectBuildGreatArea(A, X):
    res = 0
    count = {}
    for length in A:
        count[length] = count.get(length, 0) + 1
        
    usable = []
    for length in count:
        if count[length] >= 4:
            usable.append(length)
            if length * length >= X:
                res += 1
        elif count[length] >= 2:
            usable.append(length)
    usable.sort()
    
    i, j = 0, len(usable) - 1
    while i < j:
        if usable[i] * usable[j] < X:
            i += 1
        else:
            res += j - i
            if res > 1000000000:
                return -1
            j -= 1
    return res    
    pass

# (X = 5, A = [1,2,5,1,1,2,3,5,1]) = 2
print("X = 5, A = [1,2,5,1,1,2,3,5,1], the number of distinct rectangle sizes that can be built out of a given set of segments is",
      str(rectBuildGreatArea(X = 5, A = [1,2,5,1,1,2,3,5,1])))
