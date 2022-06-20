# Delta 2011
#MinAbsSum: Given array of integers, find the lowest absolute sum of elements.
def minAbsSum(A):
    # variables initialization and setup
    abs_numbers = [abs(i) for i in A]
    sum_of_elems = sum(abs_numbers)
    dyn = [0] + [-1] * (sum_of_elems - 1)
    result = sum_of_elems
    occurrences = {}
    # build occurrences dictionary
    for number in abs_numbers:
        occurrences[number] = occurrences.get(number, 0) + 1
    # main loop - process dynamic list
    for i in occurrences:
        for j in range(sum_of_elems):
            if dyn[j] >= 0:
                dyn[j] = occurrences[i]
            elif j >= i and dyn[j - i] > 0:
                dyn[j] = dyn[j - i] - 1
    # get the sum closest to half the sum of elements
    for i in range(sum_of_elems // 2 + 1):
        if dyn[i] >= 0:
            result = min(result, sum_of_elems - 2 * i)
    return result    
    pass

#[1,5,2,-2] = 0
print("[1,5,2,-2], the lowest absolute sum is", str(minAbsSum([1,5,2,-2])))
