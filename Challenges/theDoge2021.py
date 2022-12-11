# The Doge 2021
# PetsAndToys: Each of N people has either a dog or a cat, and owns a toy for dog or for cat.
# Is it possible to exchange toys between acquaintances so that every animal gets an appropriate toy?

def petsAndToys(P, T, A, B):
    #initial settings.
    l = len(P)
    exchanges_dogs = []
    exchanges_cats = []
    reachable = [-1] * l
    #finding numbers of pets/toys that needs to be exchanged.
    for x in range(l):
        if P[x] != T[x]: 
            if P[x] == 1: exchanges_dogs.append(x)
            elif P[x] == 2: exchanges_cats.append(x)
    #expections
    if len(exchanges_cats)!= len(exchanges_dogs): return False
    if exchanges_cats == exchanges_dogs == []: return True
    if A == B == [] and len(exchanges_cats) != 0: return False 
    #putting connections to right order.
    for x in range(len(A)): 
        if A[x] > B[x]: A[x], B[x] = B[x], A[x]
    connections=sorted(list(zip(A,B)))
    #find full path.
    def get_path(start):
        path = []
        while start != -1:
            path.append(start)
            start = reachable[start]
        return path
        pass
    for node in connections:
        source, destination = node[0], node[1]
        #when both person are not reachable for previous ones.
        if reachable[source] == reachable[destination] == -1:
            reachable[destination] = source
        #rest of cases.      
        else:
            #getting connections with previous people for both persons.
            path = get_path(source) + get_path(destination)
            path = sorted(list(set((path)))) #removing duplicates.
            earliest_person = path.pop(0) #earliest reachable person.
            for person in path: reachable[person] = earliest_person
    #creating arrays of connection/trees of people.
    for node in range(len(exchanges_dogs)):
        exchanges_dogs[node] = get_path(exchanges_dogs[node])[-1]
        exchanges_cats[node] = get_path(exchanges_cats[node])[-1]
    if sorted(exchanges_cats) == sorted(exchanges_dogs): return True
    else: return False
    pass

# (P = [1, 1, 2], T = [2, 1, 1], A = [0, 2], B = [1, 1]) = True
print("P = [1, 1, 2], T = [2, 1, 1], A = [0, 2], B = [1, 1], it is possible to exchange toys in such a way that every animal receives an appropriate toy is",
      str(petsAndToys(P = [1, 1, 2], T = [2, 1, 1], A = [0, 2], B = [1, 1])))
# (P = [2, 2, 1, 1, 1], T = [1, 1, 1, 2, 2], A = [0, 1, 2, 3], B = [1, 2, 0, 4]) = False
print("P = [2, 2, 1, 1, 1], T = [1, 1, 1, 2, 2], A = [0, 1, 2, 3], B = [1, 2, 0, 4], it is possible to exchange toys in such a way that every animal receives an appropriate toy is",
      str(petsAndToys(P = [2, 2, 1, 1, 1], T = [1, 1, 1, 2, 2], A = [0, 1, 2, 3], B = [1, 2, 0, 4])))
# (P = [1, 1, 2, 2, 1, 1, 2, 2], T = [1, 1, 1, 1, 2, 2, 2, 2], A = [0, 2, 4, 6], B = [1, 3, 5, 7]) = False
print("P = [1, 1, 2, 2, 1, 1, 2, 2], T = [1, 1, 1, 1, 2, 2, 2, 2], A = [0, 2, 4, 6], B = [1, 3, 5, 7], it is possible to exchange toys in such a way that every animal receives an appropriate toy is",
      str(petsAndToys(P = [1, 1, 2, 2, 1, 1, 2, 2], T = [1, 1, 1, 1, 2, 2, 2, 2], A = [0, 2, 4, 6], B = [1, 3, 5, 7])))
# (P = [2, 2, 2, 2, 1, 1, 1, 1], T = [1, 1, 1, 1, 2, 2, 2, 2], A = [0, 1, 2, 3, 4, 5, 6], B = [1, 2, 3, 4, 5, 6, 7]) = True
print("P = [2, 2, 2, 2, 1, 1, 1, 1], T = [1, 1, 1, 1, 2, 2, 2, 2], A = [0, 1, 2, 3, 4, 5, 6], B = [1, 2, 3, 4, 5, 6, 7], it is possible to exchange toys in such a way that every animal receives an appropriate toy is",
      str(petsAndToys(P = [2, 2, 2, 2, 1, 1, 1, 1], T = [1, 1, 1, 1, 2, 2, 2, 2], A = [0, 1, 2, 3, 4, 5, 6], B = [1, 2, 3, 4, 5, 6, 7])))
