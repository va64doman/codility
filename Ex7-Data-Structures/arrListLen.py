#ArrListLen: Compute length of a single-link list encoded in an array.
def arrListLen(A):
    cnt = 0
    if A[0] != -1:
        cnt += 1
        return cnt + countList(A[0], A)
    else:
        return 1
    pass

def countList(idx, A):
    if A[idx] == -1:
        return 1
    return 1 + countList(A[idx], A)    
    pass

#[1,4,-1,3,2] = 4
print("[1,4,-1,3,2], the length of single-link list encoded in this array is", str(arrListLen([1,4,-1,3,2])))

