#FirstUnique: Find the first unique number in a given sequence.
def firstUnique(A):
    counts = {}
    for item in A:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for item in counts:
        if counts[item] == 1:
            return item
    return -1
    pass

#[4,10,5,4,2,10] = 5
print("[4,10,5,4,2,10], the first unique number is", str(firstUnique([4,10,5,4,2,10])))
#[1,4,3,3,1,2] = 4
print("[1,4,3,3,1,2], the first unique number is", str(firstUnique([1,4,3,3,1,2])))
#[6,4,4,6] = -1
print("[6,4,4,6], the first unique number is", str(firstUnique([6,4,4,6])))
