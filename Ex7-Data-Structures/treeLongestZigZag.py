#TreeLongestZigZag: Given a tree, find a downward path with the maximal number of direction changes.
def treeLongestZigZag(T):
    if T == None or (T.l == None and T.r == None):
        return 0
    leftLen,rightLen = 0,0
    if T.l != None:
        leftLen += traverse(T.l, 1, True, leftLen)
    if T.r != None:
        rightLen += traverse(T.r, 1, False, rightLen)
    if leftLen > rightLen:
        return leftLen
    return rightLen
    pass

def traverse(T, length, isLeft, maxLen):
    maximum = max(length, maxLen)
    if T.l != None:
        if isLeft:
            maximum = traverse(T.l, 1, True, maximum)
        else:
            maximum = traverse(T.l, length + 1, True, maximum)
    if T.r != None:
        if isLeft:
            maximum = traverse(T.r, length + 1, False, maximum)
        else:
            maximum = traverse(T.r, 1, False, maximum)
    return maximum
    pass

class Tree(object):
  x = 0
  l = None
  r = None

"""
5
| \
v  >
3  10
|   | \
v   v  >
20  1   15
|        | \
v        v  >
6        30  8
          |
          v
          9

returns 2 (15 to 30)
"""
# zigzag containing only one edge or one node has length 0.
root = Tree()
root.x = 5
rootL = Tree()
rootL.x = 3
rootLL = Tree()
rootLL.x = 20
rootLLL = Tree()
rootLLL.x = 6
rootR = Tree()
rootR.x = 10
rootRL = Tree()
rootRL.x = 1
rootRR = Tree()
rootRR.x = 15
rootRRL = Tree()
rootRRL.x = 30
rootRRLL = Tree()
rootRRLL.x = 9
rootRRR = Tree()
rootRRR.x = 8

rootLL.l =rootLLL
rootL.l = rootLL
root.l = rootL
rootRRL.l = rootRRLL
rootRR.l = rootRRL
rootRR.r = rootRRR
rootR.l = rootRL
rootR.r = rootRR
root.r = rootR

print("The length of longest zig zag in tree is", str(treeLongestZigZag(root)))
