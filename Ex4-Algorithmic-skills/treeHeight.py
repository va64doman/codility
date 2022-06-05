#TreeHeight: Compute the height of a binary tree.
def treeHeight(T):
    # If there are no subtree, stop checking that side of the tree.
    if T == None:
        return -1
    return 1 + max(treeHeight(T.l), treeHeight(T.r))
    pass

"""
5
| \
v  >
3  10
| \  \
v  >  >
20 21 1

return 2
"""

class Tree(object):
  x = 0
  l = None
  r = None


root = Tree()
root.x = 5
rootL = Tree()
rootL.x = 3
rootR = Tree()
rootR.x = 10
rootLL = Tree()
rootLL.x = 20
rootLR = Tree()
rootLR.x = 21
rootRL = Tree()
rootRL.x = 1

rootL.l = rootLL
rootL.r = rootLR
rootR.l = rootRL
root.l = rootL
root.r = rootR

print("The height of the tree is", str(treeHeight(root)))

