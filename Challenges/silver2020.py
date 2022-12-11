# Silver 2020
# RectanglesStrip: From a given set choose as many rectangles with a common side as possible.

def rectanglesStrip(A, B):
    def update_results(number):
        if not (number in results): results[number]=1
        else: results[number]+=1
        pass
    results = {}
    for rectangle in range(len(A)):
        update_results(A[rectangle])
        if A[rectangle]!=B[rectangle]: 
            update_results(B[rectangle])  
    return ((max(list(results.values()))))
    pass

# (A = [2, 3, 2, 3, 5], B = [3, 4, 2, 4, 2]) = 3
print("A = [2, 3, 2, 3, 5], B = [3, 4, 2, 4, 2], the maximum number of rectangles that can be arranged into a strip is", str(rectanglesStrip(A = [2, 3, 2, 3, 5], B = [3, 4, 2, 4, 2])))
# (A = [2, 3, 1, 3], B = [2, 3, 1, 3]) = 2
print("A = [2, 3, 1, 3], B = [2, 3, 1, 3], the maximum number of rectangles that can be arranged into a strip is",str(rectanglesStrip(A = [2, 3, 1, 3], B = [2, 3, 1, 3])))
# (A = [2, 10, 4, 1, 4], B = [4, 1, 2, 2, 5]) = 3
print("A = [2, 10, 4, 1, 4], B = [4, 1, 2, 2, 5], the maximum number of rectangles that can be arranged into a strip is",str(rectanglesStrip(A = [2, 10, 4, 1, 4], B = [4, 1, 2, 2, 5])))
