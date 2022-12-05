# Manganum 2017
# FinalTurn: Given positions of all enemy figures and your figure (queen) in checkers game,
# count the maximum number of points (1 for pawn, 10 for queen) you can earn by beating enemy's figures in one round.

def finalTurn(X, Y, T):
    maxY = max(Y)
    maxX = max(X)
    minX = min(X)
    indexOfQueen = T.index("X")
    posX = X[indexOfQueen]
    posY = Y[indexOfQueen]
    dir1 = nextStep(posX,posY,X,Y,maxY,maxX,minX,-1,T,False)
    dir2 = nextStep(posX,posY,X,Y,maxY,maxX,minX,1,T,False)
    return max(dir1, dir2)
    pass

def nextStep(posX, posY, X, Y, maxY, maxX, minX, xVal, T, isMoveable):
    posY += 1
    posX += xVal
    if posY > maxY or (((posX < minX and posX + xVal < posX) or (posX > maxX and posX + xVal > posX)) and not isMoveable): return 0
    point = getPoint(posX, posY, X, Y, T)
    if point > 0:
        isMoveable = True
        posY += 1
        posX += xVal
        if getPoint(posX, posY, X, Y, T) > 0: return 0
    dir1 = nextStep(posX, posY, X, Y, maxY, maxX, minX, xVal, T, isMoveable)
    dir2 = 0
    if isMoveable: dir2 = nextStep(posX, posY, X, Y, maxY, maxX, minX, xVal - (2 * xVal), T, False)
    return max(dir1, dir2) + point
    pass

def getPoint(posX, posY, X, Y, T):
    for i in range(len(X)):
        if X[i] == posX and Y[i] == posY:
            if T[i] == 'p': return 1
            elif T[i] == 'q': return 10
    return 0
    pass

# (X = [3, 5, 1, 6], Y = [1, 3, 3, 8], T = "Xpqp") = 10
print("(X = [3, 5, 1, 6], Y = [1, 3, 3, 8], T = ""Xpqp""), the maximum number of points he can score in a single turn is",
      str(finalTurn(X = [3, 5, 1, 6], Y = [1, 3, 3, 8], T = "Xpqp")))
# (X = [0, 3, 5, 1, 6], Y = [4, 1, 3, 3, 8], T = "pXpqp") = 2
print("(X = [0, 3, 5, 1, 6], Y = [4, 1, 3, 3, 8], T = ""pXpqp""), the maximum number of points he can score in a single turn is",
      str(finalTurn(X = [0, 3, 5, 1, 6], Y = [4, 1, 3, 3, 8], T = "pXpqp")))
# (X = [0, 6, 2, 5, 3, 0], Y = [4, 8, 2, 3, 1, 6], T = "ppqpXp") = 12
print("(X = [0, 3, 5, 1, 6], Y = [4, 1, 3, 3, 8], T = ""pXpqp""), the maximum number of points he can score in a single turn is",
      str(finalTurn(X = [0, 6, 2, 5, 3, 0], Y = [4, 8, 2, 3, 1, 6], T = "ppqpXp")))
