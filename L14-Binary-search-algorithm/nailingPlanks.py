#NailingPlanks: Count the minimum number of nails that allow a series of planks to be nailed.

def check_nailed(start_pts, end_pts, nails, candidate):
    """Check if candidate nails are nailing all planks."""
    # build and populate prefix sums nail map
    nail_map = [0] * (2 * (len(start_pts) + 1) + 1)
    for nail in nails[0:candidate]:
        nail_map[nail] = 1
    for i in range(1, len(nail_map)):
        nail_map[i] += nail_map[i - 1]
    # if there's at least one not-nailed plank, return false
    for i, _ in enumerate(start_pts):
        # plank not nailed = no nail between end and start point
        if nail_map[end_pts[i]] == nail_map[start_pts[i] - 1]:
            return False
    # all planks nailed using candidate number of nails
    return True

def nailingPlanks(A, B, C):
    """Solution method implementation."""
    # initialize binary search and result vars
    upper, lower, result = len(C), 0, -1
    # apply binary search algorithm
    while upper >= lower:
        # get middle point
        mid = (upper + lower) // 2
        # determine if all planks are nailed using "mid" nails
        all_nailed = check_nailed(A, B, C, mid)
        # not all planks nailed. Readjust binary search interval
        if not all_nailed:
            lower = mid + 1
        # all planks nailed. Update result
        else:
            result = mid
            upper = mid - 1
    return result

#(A = [1,4,5,8], B = [4,5,9,10], C =[4,6,7,10,2]) = 4
print("A = [1,4,5,8], B = [4,5,9,10], C =[4,6,7,10,2], the minimum number of nails that allow a series of planks to be nailed is",
      str(nailingPlanks([1,4,5,8], [4,5,9,10], [4,6,7,10,2])))
