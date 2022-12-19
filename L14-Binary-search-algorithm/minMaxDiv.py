#MinMaxDivision: Divide array A into K blocks and minimize the largest sum of any block.
def resulting_blocks(target_no_of_blocks, numbers, target_sum):
    """Count blocks that have a sum at most equal to target_sum."""
    result, temp_sum = 0, 0
    for number in numbers:
        if temp_sum + number > target_sum:
            result += 1
            temp_sum = number
        else:
            temp_sum += number
    result += 1
    return max(result, target_no_of_blocks)
    pass

def minMaxDiv(K, M, A):
    upper, lower, result = sum(A), max(A), -1
    # main binary search loop
    while upper >= lower:
        # get mid point
        mid = (upper + lower) // 2
        # split array into blocks summing up the mid point       
        blocks = resulting_blocks(K, A, mid)
        
        # the sweet spot's above mid point       
        if blocks > K:
            lower = mid + 1
        # found a minimal large sum candidate
        # seek an even lower candidate in [lower, mid-1]
        elif blocks == K:
            result = mid if result == -1 else min(result, mid)
            upper = mid - 1
    return result
    pass

#(K = 3, M = 5, A = [2,1,5,1,2,2,2]) = 6
print("K = 3, M = 5, A = [2,1,5,1,2,2,2], the minimal large sum is", str(minMaxDiv(3,5,[2,1,5,1,2,2,2])))
