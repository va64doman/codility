#ParkingBill: Given two strings representing times of entry and exit from a car parking lot, find the cost of the ticket according to the given billing rules.
import math

def timeStamp(T):
    comp = T.split(":")
    return int(comp[0]) * 60 + int(comp[1])
    pass

def parkingBill(E,L):
    cost = 2 + 3
    duration = timeStamp(L) - timeStamp(E)
    duration -= 60
    if duration > 0:
        cost += int(math.ceil(duration / 60.0)) * 4
    return cost
    pass

# (E = "10:00" and L = "13:21") = 17
# 2 + 3 + (3 * 4) = 17
print("The cost between 10:00 and 13:21 is", str(parkingBill("10:00", "13:21")))
# (E = "09:42" and L = "11:42") = 9
# 2 + 3 + 4 = 9
print("The cost between 09:42 and 11:42 is", str(parkingBill("09:42", "11:42")))
"""
The entrance fee of the car parking lot is 2;
The first full or partial hour costs 3;
Each successive full or partial hour (after the first) costs 4.
"""
