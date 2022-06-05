# HilbertMaze: Find the shortest path between two fields in a Hilbert maze.
def hilbertMaze(N, A, B, C, D):
    """
    Using the A* algorithm, return the shortest path from the start point to the end point in the maze
    It should be noted that the grid coordinates in the title and the grid coordinates in the array are opposite, and now the array shall prevail
    Therefore, it is necessary to convert the coordinates of the starting point and the ending point in the title.
    """
    if A == C and B == D:
        return 0
    # The coordinates of the real start point and end point
    start_a, start_b = 2 ** (N + 1) - B, A
    end_c, end_d = 2 ** (N + 1) - D, C
    # Start the A* algorithm
    close_list = {} # collection of grids that have been walked
    open_list = {(start_a, start_b): [(start_a, start_b), 0]} # set of grids to go
    while (end_c, end_d) not in open_list and open_list:
        # Select the grid with the smallest cost function in open_list
        cost_least = min(open_list.items(), key=lambda k: k[1][1])[0]
        # Calculate adjacent grids to go to
        x, y = cost_least
        point_list = point_go(N, x, y)
        copy_open_list = open_list.copy()
        if point_list:
            for j in point_list:
                if j in close_list: # ignore
                    pass
                elif j in open_list: # need to compare the values, choose the smaller one, and change the parent's node
                    new_cost = 1 + manhattan(j[0], j[1], end_c, end_d)
                    if new_cost < open_list[j][1]:
                        copy_open_list[j][0] = cost_least
                else:
                    copy_open_list[j] = [(x, y), 1 + manhattan(j[0], j[1], end_c, end_d) + open_list[(x, y)][1]]
        # store to the meshes that have been traversed
        close_list[cost_least] = open_list[cost_least][0]
        del copy_open_list[cost_least]
        open_list = copy_open_list
    if not open_list: # No solution
        return 0
    else: # get the best path
        close_list[(end_c, end_d)] = open_list[(end_c, end_d)][0]
        end_sign = 0
        path_list = [(end_c, end_d)]
        while end_sign != (start_a, start_b):
            end_sign = close_list[path_list[-1]]
            path_list.append(end_sign)
    # In order to make the coordinates and the maze are the same, now transform, mainly to verify the correctness of the result
    trans_list = []
    for h in path_list:
        trans_list.append([h[1], 2 ** (N+1) - h[0]])
    return len(trans_list) - 1    
    pass

def judge_walkable(n, x, y):
    # Need to convert the coordinates (x, y) equivalently to the grid in the maze with N=1.
    # At this time, the relationship of the coordinates in N=1 is given
    # First construct the maze when n=1
    maze_list = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
    # The situation of each grid in the maze with N=1
    maze_dict = {(i, j): maze_list[i][j] for i in range(len(maze_list)) for j in range(len(maze_list[i]))}
    while (x, y) not in maze_dict or n != 1:
        # First determine the three grids at the intersection of the small maze
        if x == 2 ** n:
            # upper left, lower left intersect
            if y == 1:
                return 1
            # top right, bottom right intersect
            elif y == 2 ** (n + 1) - 1:
                return 1
            else:
                return 0
        if y == 2 ** n:
            # top left, top right intersect
            if x == 2 ** n - 1:
                return 1
            else:
                return 0
        # Then judge whether it is around
        if x == 0 or x == 2 ** (n+1):
            return 0
        if y == 0 or y == 2 ** (n+1):
            return 0
        # Make different changes according to different regions
        if 1 <= x < 2**n < y < 2**(n+1): # Top right
            y -= 2**n
        elif 1 <= y < 2**n < x < 2**(n+1): # Lower left
            # First rotate 90 degrees counterclockwise, the original a row b column becomes 2**nb row a column
            a = x - 2 ** n
            b = y
            x, y = 2 ** n + 2 ** n-b, a
            # Then translate up 2**n units
            x -= 2 ** n
        elif 2**n < x < 2**(n+1)and 2**n < y < 2**(n+1): # Lower right
            # First rotate 90 degrees clockwise, the original a row and b column become b row (2**na) column
            a = x - 2 ** n
            b = y - 2 ** n
            x, y = 2 ** n + b, 2**n + 2**n - a
            # Then translate up 2**n units
            x -= 2 ** n
            # Then translate left 2**n units
            y -= 2 ** n
        n -= 1
    return maze_dict[(x, y)]
    pass

# Use A* to get the optimal path from the start point to the end point
def point_go(n, x, y):
    point_list = []
    length = 2 ** (n+1) + 1
    # Right
    if x >= 1:
        if not judge_walkable(n, x-1, y):
            point_list.append((x - 1, y))
    # Left
    if x < length - 1:
        if not judge_walkable(n, x+1, y):
            point_list.append((x + 1, y))
    # Up
    if y >= 1:
        if not judge_walkable(n, x, y-1):
            point_list.append((x, y - 1))
    # Down
    if y < length - 1:
        if not judge_walkable(n, x, y+1):
            point_list.append((x, y + 1))
    return point_list
    pass


def manhattan(a, b, c, d):
    """
    Calculate the Manhattan distance between the grid with coordinates (a,b) and the grid with coordinates (c,d)
    Manhattan distance: the sum of the absolute value of the difference between the abscissa and the ordinate of the corresponding grid
    """
    return abs(a - c) + abs(b - d)
    pass

#(N = 1, A = 2, B = 1, C = 3 and D = 4) = 8
print("Maze size of (2^(1+1)) + 1, the shortest path between (2,1) and (3,4) is", str(hilbertMaze(N = 1, A = 2, B = 1, C = 3, D = 4)))
#(N = 2, A = 2, B = 5, C = 6 and D = 6) = 7
print("Maze size of (2^(2+1)) + 1, the shortest path between (2,5) and (6,6) is", str(hilbertMaze(N = 2, A = 2, B = 5, C = 6, D = 6)))
#(N = 3, A = 6, B = 6, C = 10 and D = 13) = 39
print("Maze size of (2^(3+1)) + 1, the shortest path between (6,6) and (10,13) is", str(hilbertMaze(N = 3, A = 6, B = 6, C = 10, D = 13)))
