# Rubidium 2018
# SheepAndSunshades: Given a set of points on a cartesian plane, find the minimum distance between some pair of them to maximise another metric.
def sheepAndSunshades(X,Y):
    P, Q = [], []
    for i in range(len(X)):
        P.append((X[i],Y[i]))
        Q.append((X[i],Y[i]))
    P.sort(key=lambda x: (x[0],x[1]))
    Q.sort(key=lambda x: (x[1],x[0]))    
    def run(P,Q):
        l = len(P)
        if l<=3:
            delta = float('inf')
            for i in range(l-1):
                for j in range(i+1,l):
                    delta = min(delta, max(abs(P[i][0]-P[j][0]), 
                                           abs(P[i][1]-P[j][1])))
            return delta        
        half = l//2
        P_L = set(P[:half])
        Q1, Q2 = [], []
        for i in range(l):
            if Q[i] in P_L:
                Q1.append(Q[i])
            else:
                Q2.append(Q[i])            
        mid_x = P[half][0]
        delta = min(run(P[:half],Q1), run(P[half:],Q2))        
        Q_inStrip = []
        for i in range(l):
            if abs(Q[i][0]-mid_x) <= delta:
                Q_inStrip.append(Q[i])
                delta_prime = float('inf')
        for i in range(len(Q_inStrip)):
            for j in range(1,4):
                if i+j < len(Q_inStrip):
                    delta_prime = min(delta_prime, 
                                      max(abs(Q_inStrip[i][0]-Q_inStrip[i+j][0]),
                                          abs(Q_inStrip[i][1]-Q_inStrip[i+j][1])))
        return delta_prime if delta_prime<delta else delta
        pass
    return run(P,Q) // 2
    pass

# (X = [0, 0, 10, 10], Y = [0, 10, 0, 10]) = 5
print("X = [0, 0, 10, 10], Y = [0, 10, 0, 10], the minimum distance between some pair of them to maximise another metric is", str(sheepAndSunshades(X = [0, 0, 10, 10], Y = [0, 10, 0, 10])))
# (X = [1, 1, 8], Y = [1, 6, 0]) = 2
print("X = [1, 1, 8], Y = [1, 6, 0], the minimum distance between some pair of them to maximise another metric is", str(sheepAndSunshades(X = [1, 1, 8], Y = [1, 6, 0])))
