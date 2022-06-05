#Passing Car: Count the number of passing cars on the road.
def passCar(A):
    sE = 0
    s = 0
    for i in range(0, len(A)):
        if A[i] == 0:
            sE += 1
        elif A[i] == 1:
            s += sE
    if s > 1000000000:
        return -1
    else:
        return s
    pass

# 0 = East, 1 = West
#[0,1,0,1,1] = 5
print("[0,1,0,1,1], the number of passing cars is " + str(passCar([0,1,0,1,1])))
