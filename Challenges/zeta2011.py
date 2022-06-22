# Zeta 2011
# BallSwitchBoard: Calculate how balls roll through a board of switches.

# Computes the number of balls to make it into this square
def calcBall(A, K, b, r, x, y):
	left = 0
	top = 0
	if x == 0 and y == 0:
		top = K
	if x > 0:
		t = r[x-1] + b[x-1]
		if A[y][x-1] == -1:
			left = t // 2
		elif A[y][x-1] == 0:
			left = r[x-1]
		elif A[y][x-1] == 1:
 			left = (t + 1) // 2
	if y > 0:
		t = r[x] + b[x]
		if A[y-1][x] == -1:
			top = (t + 1) // 2
		elif A[y-1][x] == 0:
 			top = b[x]
		elif A[y-1][x] == 1:
			top = t // 2
	b[x] = top
	r[x] = left
	pass

# -1 => ball leaves through the bottom
# +1 => ball leaves through the right
def ballSwitchBoard(A, K):
	height = len(A)
	if height == 0:
		return k
	width = len(A[0])
	bottom = [0] * width
	right = [0] * width
	for y in range(height):
		for x in range(width):
			calcBall(A, K, bottom, right, x, y)
	# Given the lower-right, determine how many pass down
	passBR = bottom[width - 1] + right[width -1]
	if A[height-1][width-1] == -1:
		return (passBR + 1) // 2
	elif A[height-1][width-1] == 0:
		return bottom[width - 1]
	elif A[height-1][width-1] == 1:
		return passBR // 2
	return 0
	pass
"""
(K = 4,
(A) Row x column =
-1,0,-1
1,0,0
)

returns 1
"""
A = [[-1,0,-1],[1,0,0]]
print("A = [[-1,0,-1],[1,0,0]], K = 4, " + 
"the number of balls that will leave the board through the bottom edge of the bottom-right switch is", 
str(ballSwitchBoard(A, 4)))