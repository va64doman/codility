# Epsilon 2011
# Minfuds: Compute minimal value of the function (max f_n) - (min f_n).
"""
F(X,K)	=	A[K]*X + B[K]
U(X)	=	max{ F(X,K) : 0 <= K < N }
D(X)	=	min{ F(X,K) : 0 <= K < N }
S(X)	=	U(X) − D(X)
"""
import functools

EPS = 0.0000001
INF = 10000.0

def signum(val):
    return 1 if val > 0 else -1 if val < 0 else 0

class Point:
    def __init__(self, x = INF, y = INF):
        self.x = x
        self.y = y
        pass
    pass

class Line:
    def __init__(self, a = INF, b = INF, p1 = None, p2 = None):
        self.a = a
        self.b = b
        if p1 != None and p2 != None:
            self.a = (p1.y - p2.y) / (p1.x - p2.x)
            self.b = p1.y - self.a * p1.x
        pass
    def comparator(left, right):
        if left.a != right.a:
            return signum(left.a - right.a)
        return signum(left.b - right.b)
        pass
    def getPoint(self, x):
        return Point(x, self.a * x + self.b)
        pass
    pass

def computeExtremePoints(lines, maxOrMin):
    extremePoints = []
    for line in lines:
        while True:
            if not extremePoints:
                extremePoints.append(line.getPoint(-INF))
                break
            lastTwoPoint = extremePoints[len(extremePoints) - 2]
            lastPoint = extremePoints[len(extremePoints) - 1]
            extremePoints.pop()
            yDiff = line.getPoint(lastTwoPoint.x).y - lastTwoPoint.y
            if (maxOrMin and yDiff < 0) or (not maxOrMin and yDiff > 0):
                extremePoints.append(intersect(line, Line(p1 = lastTwoPoint, p2 = lastPoint)))
                break
            if len(extremePoints) == 1:
                extremePoints.pop()
        extremePoints.append(line.getPoint(INF))
    return extremePoints
    pass

def computeMinDiff(maxPoints, minPoints):
    minDiff = float('inf')
    diff = float('inf')
    minLine = None
    maxLine = None
    maxIndex = 0
    minIndex = 0
    while maxIndex < len(maxPoints) or minIndex < len(minPoints):
        if minIndex == len(minPoints) or (maxIndex < len(maxPoints) and maxPoints[maxIndex].x <= minPoints[minIndex].x):
            if minIndex == 0:
                minLine = Line(p1 = minPoints[0], p2 = minPoints[1])
            elif minIndex == len(minPoints):
                minLine = Line(p1 = minPoints[len(minPoints) - 2], p2 = minPoints[len(minPoints) - 1])
            else:
                minLine = Line(p1 = minPoints[minIndex - 1], p2 = minPoints[minIndex])
            diff = maxPoints[maxIndex].y - minLine.getPoint(maxPoints[maxIndex].x).y
            maxIndex += 1
        else:
            if maxIndex == 0:
                maxLine = Line(p1 = maxPoints[0], p2 = maxPoints[1])
            elif maxIndex == len(maxPoints):
                maxLine = Line(p1 = maxPoints[len(maxPoints) - 2], p2 = maxPoints[len(maxPoints) - 1])
            else:
                maxLine = Line(p1 = maxPoints[maxIndex - 1], p2 = maxPoints[maxIndex])
            diff = maxLine.getPoint(minPoints[minIndex].x).y - minPoints[minIndex].y
            minIndex += 1
        minDiff = min(minDiff, diff)
    return minDiff
    pass

def intersect(line1, line2):
    x = (line1.b - line2.b) / (line2.a - line1.a)
    y = line1.a * x + line1.b
    return Point(x, y)
    pass

def minfuds(A, B):
    lines = []
    for i in range(len(A)):
        lines.append(Line(a = A[i], b = B[i]))
    lines = sorted(lines, key=functools.cmp_to_key(Line.comparator))
    maxPoints = computeExtremePoints(lines, True)    
    lines = sorted(lines, key=functools.cmp_to_key(Line.comparator), reverse=True)
    minPoints = computeExtremePoints(lines, False)
    return computeMinDiff(maxPoints, minPoints)
    pass
# (A = [-1,1,0], B =[3,0,2]) = 0.5
print("A = [-1,1,0], B =[3,0,2], the minimal value of the function (max f_n) - (min f_n) is", str(minfuds(A = [-1,1,0], B =[3,0,2])))