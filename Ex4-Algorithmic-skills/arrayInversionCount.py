#ArrayInversionCount: Compute number of inversion in an array.
def mergesort( aList, first, last ):
    """
    Modified merge sort algorithm.
    Record the inversion count during sort.
    """
    mid = ( first + last ) // 2
    if first < last:
        # Recursive calling
        left_inver = mergesort( aList, first, mid )
        if left_inver == -1:
            return -1
        right_inver = mergesort( aList, mid + 1, last )
        if left_inver == -1:
            return -1
    else:
        # Terminate condition
        return 0
    first_index = first     # The index for the left part
    second_index = mid + 1  # The index for the right part
    temp = [0] * (last-first+1)     # To hold the sorted content
    temp_index = 0
    merge_inver = 0         # Number of inversion in merging
    while first_index <= mid and second_index <= last:
        if aList[first_index] <= aList[second_index]:
            # Less index indicates less value. No inversion.
            temp[temp_index] = aList[first_index]
            first_index += 1
        else:
            # Greater index has less value. Inversion exists.
            # For exampe:
            #       [     4,   5,   2,   3     ]
            #       | Left part |  |Right Part|
            # and first_index = 1, second_index = 3, mid = 2
            # We need the item "2" to be the position 0. So it
            # has to pass all the unwritten items in left part.
            # Here these unwritten items are "4" and "5". So
            # two more inversions are involved.
            # In general, the left part is sorted. So all the
            # elements, being and after first_index, are greater
            # than element in position second_index. AND all of
            # them have less indexes. As the result,
            # there are mid-first_index+1 new reversions.
            temp[temp_index] = aList[second_index]
            second_index += 1
            merge_inver += mid - first_index + 1
            if merge_inver > 1000000000:
                return -1
        temp_index += 1
    if first_index != mid+1:
        # Some element in the left part left. They have less
        # indexes, but greater values. Inversion involves.
        # BUT these inversions have already been counted.
        while first_index <= mid:
            temp[temp_index] = aList[first_index]
            first_index += 1
            temp_index += 1
    if second_index != last+1:
        # Some element in the right part left. They have both
        # greater indexes and values than all in the left part.
        # No inversion is involved.
        while second_index <= last:
            temp[temp_index] = aList[second_index]
            second_index += 1
            temp_index += 1
    # Rewrite the sorted content into the original array
    aList[first:last+1] = temp[:]
    if merge_inver + left_inver + right_inver > 1000000000:
        return -1
    else:
        return merge_inver + left_inver + right_inver

def arrayInversionCount(A):
    return mergesort(A * 1, 0, len(A)-1)
    pass

# [-1,6,3,4,7,4] = 4
# returns −1 if it exceeds 1,000,000,000
print("[-1,6,3,4,7,4], the number of inversion in array:", str(arrayInversionCount([-1,6,3,4,7,4])))
