#Peaks: Divide an array into the maximum number of same-sized blocks, each of which should contain an index P such that A[P - 1] < A[P] > A[P + 1].
def peaks(A):
    # build list of peaks
    list_len = len(A)
    peaks = [i for i in range(1, list_len - 1) if A[i - 1] < A[i] > A[i + 1]]
    # iterate through possible block counts
    for i in range(len(peaks), 0, -1):
        # only consider divisors of list_len
        if list_len % i == 0:
            # initialize set of blocks with no peaks
            blocks_without_peaks = set(range(i))
            # drop blocks with peaks, one by one
            for peak in peaks:
                block = peak * i // list_len
                blocks_without_peaks.discard(block)
            # found the max number of blocks
            if not blocks_without_peaks:
                return i
    return 0
    pass

#[1,2,3,4,3,4,1,2,3,4,6,2] = 3
print("[1,2,3,4,3,4,1,2,3,4,6,2], the maximum number of same-sized blocks is", str(peaks([1,2,3,4,3,4,1,2,3,4,6,2])))
