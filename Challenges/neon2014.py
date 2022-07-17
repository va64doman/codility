# Neon 2014
# BoatAlignment: Connect N points with N line segments so as to minimize the largest distance between them.
def boatAlignment(R,X,M):
    boatWidth = 2 * X
    N = len(R)
    if N * boatWidth > M:
        return -1
    boatPositions = [0] * N
    boatPositions[0] = X
    for i in range(1, N):
        boatPositions[i] = boatPositions[i - 1] + boatWidth
    bollardDistances = [0] * N
    for i in range(N):
        bollardDistances[i] = R[i] - boatPositions[i]
    limitingDistances = getLimitingDistancesArray(bollardDistances)
    movement = 0
    maxBoatPosition = M - X
    for i in range(N):
        possibleMovement = (bollardDistances[i] + limitingDistances[i]) // 2 - movement
        if possibleMovement > 0:
            if boatPositions[N - 1] + movement + possibleMovement >= maxBoatPosition:
                movement = maxBoatPosition - boatPositions[N - 1]
                while i < N:
                    bollardDistances[i] -= movement
                    i += 1
                break
            else:
                movement += possibleMovement
        bollardDistances[i] -= movement
    return getMaxDistance(bollardDistances)
    pass

def getLimitingDistancesArray(distances):
    N = len(distances)
    limitingDistances = [0] * N
    lowestDistance = distances[N - 1]
    for i in range(N - 1, -1, -1):
        if lowestDistance > distances[i]: lowestDistance = distances[i]
        limitingDistances[i] = lowestDistance
    return limitingDistances
    pass

def getMaxDistance(distances):
    maxDistance = abs(distances[0])
    for dist in distances:
        if abs(dist) > maxDistance:
            maxDistance = abs(dist)
    return maxDistance
    pass

# (R = [1,3,14], X = 2, M = 16) = 3
print("R = [1,3,14], X = 2, M = 16, the minimal max distance is", str(boatAlignment(R = [1,3,14], X = 2, M = 16)))