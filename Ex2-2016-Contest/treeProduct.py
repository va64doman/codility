#TreeProduct: Remove at most two edges from a tree graph to maximize the product of the components' sizes.
# https://www.tutorialspoint.com/python_data_structure/python_graphs
# https://python-course.eu/applications-python/graphs-python.php
def treeProduct(A, B):
    if len(A) != len(B):
        return -1
    
    graph = Graph()
    vertices = A + B
    vertices = set(vertices)
    for vert in vertices:
        graph.addVertex(vert)
    for i in range(len(A)):
        graph.addEdge(A[i], B[i])
    pass

class Graph(object):
    def __init__(self, graphDict=None):
        if graphDict == None:
            graphDict = {}
        self.graphDict = graphDict
        pass
    def edges(self, vertex):
        return self.graphDict[vertex]
        pass
    def allVertices(self):
        return set(self.graphDict.keys())
        pass
    def allEdges(self):
        return self.generateEdges()
        pass
    def addVertex(self, vertex):
        if vertex not in self.graphDict:
            self.graphDict[vertex] = []
        pass
    def addEdge(self, v1, v2):
        vertex1, vertex2 = v1, v2
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self.graphDict:
                self.graphDict[x].append(y)
            else:
                self.graphDict[x] = [y]
        pass
    def generateEdges(self):
        edges = []
        for vertex in self.graphDict:
            for neighbour in self.graphDict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
        pass
    def __iter__(self):
        self._iter_obj = iter(self.graphDict)
        return self._iter_obj
        pass
    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)
        pass
    def __str__(self):
        res = "vertices: "
        for k in self.graphDict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generateEdges():
            res += str(edge) + " "
        return res
        pass
    def findPath(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex 
            in graph """
        if path == None:
            path = []
        graph = self.graphDict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.findPath(vertex, 
                                               end_vertex, 
                                               path)
                if extended_path: 
                    return extended_path
        return None
        pass    
    def findAllPaths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self.graphDict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.findAllPaths(vertex, end_vertex, path)
                for p in extended_paths: 
                    paths.append(p)
        return paths
        pass
    def vertexDegree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
        it, i.e. the number of adjacent vertices. Loops are counted 
        double, i.e. every occurence of vertex in the list 
        of adjacent vertices. """ 
        degree =  len(self.graphDict[vertex]) 
        if vertex in self.graphDict[vertex]:
            degree += 1
        return degree
        pass
    def findIsolatedVertices(self):
        """ returns a list of isolated vertices. """
        graph = self.graphDict
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated
        pass
    def Delta(self):
        """ the maximum degree of the vertices """
        max = 0
        for vertex in self.graphDict:
            vertex_degree = self.vertexDegree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max
        pass
    def degreeSequence(self):
        """ calculates the degree sequence """
        seq = []
        for vertex in self.graphDict:
            seq.append(self.vertexDegree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)
        pass
pass

#(A = [0,1,1,3,3,6,7], B = [1,2,3,4,5,3,5]) = 18
#(A = [0,1], B = [1,2]) = 3

treeProduct(A = [0,1,1,3,3,6,7], B = [1,2,3,4,5,3,5])

"""
ruby version
# https://app.codility.com/programmers/lessons/91-tasks_from_indeed_prime_2016_challenge/tree_product/
# Perfect score, O(n log n)  https://app.codility.com/demo/results/trainingT8ASPQ-2K5/

# Solving this challenge with an algorithm that works in O(n**2) was not that big of a challenge, so I didn't bother.
# Figuring out the optimal trisection of a graph in O(n log n) time was very, very challenging.
#


# Mapping the language of the problem to common tree graph terminology:
# "Posts" -> nodes,  "bridges" -> edges, "area" -> a component, "Destroying a bridge" -> cutting an edge.
# Note: nodes are usually called vertices (singular: vertex) in the larger context of mathematical graph theory.

# Edges is a hash of integers that index into the global tree array. Hash for quick insert and delete.
# We delete the edges when we connect the associated node. Children and Parent are actual nodes.

class Assert < StandardError; end
class Node

  attr_reader :id, :edges, :children, :parent, :weight

  def initialize(my_id)
    @id = my_id     # Not strictly necessary, but handy for debugging
    @edges = {}     # IDs of other nodes we are connected to
    @children = []  # References to our children so we can navigate the tree top-to-bottom. Empty for leaves.
    @parent = nil   # A reference to our parent so we can navigate the tree bottom-to-top. Nil for the root.
    @weight = 1     # The number of nodes in the component the node is left in after cutting the parent edge
    @heavy_child = nil # The child with the largest weight
  end

  # For processing the input. Registers an ID of a node we are connected to.
  def add_edge(node_id)
    @edges[node_id] = true
  end

  # For building the tree. Attaches a subtree to this node.
  # Every path from the subtree to any other node goes through self.
  def add_subtree(node)
    raise Assert.new("Adding unrecognized child #{node.id} to node #{@id}") unless @edges.delete(node.id)
    @heavy_child = nil
    children.push(node)
    @weight += node.weight
  end

  # For building the tree. Attaches self to our parent. The only path to our children is through self.
  def set_parent(node)
    raise Assert.new("Setting parent #{node.id} not in edges") unless @edges.delete(node.id)
    @parent = node
  end

  # Find the child with the largest weight.
  # This is used so rarely and in such specific situations that general search optimizations actually slow it down.
  def heavy_child
    return @heavy_child unless @heavy_child.nil?
    @heavy_child = @children.first
    @children.each { |c| @heavy_child = c if c.weight > @heavy_child.weight }
    @heavy_child
  end

  # Execute the block on the tree in depth-first, pre-order
  def self.pre_order(root, &block)
    yield root
    root.children.each {|c| self.pre_order(c, &block)}
  end

  # Execute the block on the tree in depth-first, post-order
  def self.post_order(root, &block)
    root.children.each {|c| self.post_order(c, &block)}
    yield root
  end


  # Given an array of nodes that have their edges set, build the tree in a way that guarantees
  # no child of the root has weight > tree_size / 2. This is very important to the rest of the algorithm.
  # Requires that node_array[i].id == i.
  def self.build_tree(node_array)
    min_root_weight = (node_array.size / 2) + 1 # If we find a node this size, make it the root

    q = []
    # queue up the leaves
    node_array.each { |node| q.push(node) if node.edges.size == 1 }
    # build from the bottom up, until we find the root
    while q.size > 1
      v = q.shift # v for vertex, because I do not want to use n
      raise Assert.new("node #{v.id} processed as leaf but has #{v.edges.size} edges left") unless v.edges.size == 1 || v.weight >= min_root_weight

      # This is a little tricky. We want to make sure that no child of the root has weight > n /2
      # Since every non-leaf node can be either child or parent to its neighbor, we can force
      # this by refusing to add parents to any node that is too heavy, and instead wait for
      # the parents to come around and add themselves as children. Because the only way for a tree
      # to have 2 nodes that have weight > n/2 is for one to be a child of the other, we can
      # be sure that if we never attach an overweight node as a child, the tree will only have
      # one such node.
      if v.weight < min_root_weight
        parent = node_array[v.edges.keys.first]
        v.set_parent(parent)
        parent.add_subtree(v)
        q.push(parent) if parent.edges.size == 1
      else
        # It often happens that the center of the tree is the best root, in which case it comes out of this loop last.
        # To preserve that behavior and ensure we process all the children when we find the root
        # early, we just push it onto the end of the queue again.
        q.push(v)
      end
    end
    # Last one left is root
    root = q.shift

    raise Assert.new("Nominated #{root.id} as root but it has #{root.edges.size} edges left") unless root.edges.size == 0
    raise Assert.new("Nominated #{root.id} as root but it has #{root.weight} weight") unless root.weight == node_array.size
    raise Assert.new("Root has child with weight > n/2 {node_array.size / 2}:\n   #{root.inspect}") if root.heavy_child.weight >= min_root_weight

    root
  end

  # Helper functions for development, not strictly necessary for the solution
  def to_s
    "\##{@id}"
  end

  def inspect
    str = "\##{@id}=#{@weight}"
    unless children.empty?
      str += "\n    |\n  " + @children.reduce("") { |s, c| s += "  \##{c.id}=#{c.weight}" }
    end
    str
  end
end


# The main program
def s(a, b)
  raise Assert "Bad input" unless a.size == b.size

  root = nil
  tree = Array.new(a.size + 1) # tree stores n+1 nodes (guard posts)
  # We can save ourselves some hassle and rely on stronger assumptions if we eliminate the special cases early
  return tree.size unless tree.size > 4

  (0...tree.size).each { |i| tree[i] = Node.new(i) }

  # Add edges to nodes. The first step of building the tree.
  (0...a.size).each do |i|
    tree.fetch(a[i]).add_edge(b[i])
    tree.fetch(b[i]).add_edge(a[i])
  end

  root = Node.build_tree(tree)
  best_bisection = root.heavy_child.weight
  best_bisection_result = best_bisection * (tree.size - best_bisection)

  # Start working on finding the best trisection

  # Find the heaviest branch of the tree. We want to process it separately because it is special.
  heavy_subtree = root.heavy_child

  # Build cut lists
  # In the end, we want a sorted array with unique values, and Array.uniq is going to put the array in a hash
  # anyway, so we might as well just build the hash up front.
  heavy_cuts = {1 => true} # a list of possible subtree sizes resulting from a single cut on the heavy branch
  other_cuts = {1 => true} # list of possible subtree sizes resulting from a single cut anywhere but the heavy branch.

  root.children.each do |s|
    next if s.weight == 1
    if s == heavy_subtree
      Node.post_order(s) { |c| heavy_cuts[c.weight] = true }
    else
      Node.post_order(s) { |c| other_cuts[c.weight] = true }
    end
  end


  # convert to sorted arrays so we can do binary searches on them
  # This and future searches we do is what makes the whole algorithm O(n log n) instead of O(n)
  heavy_cuts = Cutlist.new(heavy_cuts.keys.sort)
  other_cuts = Cutlist.new(other_cuts.keys.sort)

  #   *Here is the magic*
  #
  # We have arranged the tree such that
  # 1) the maximum possible weight of the heavy subtree is n > 2, and
  # 2) no other subtree is heavier than the heavy subtree
  #
  # Condition 1 means that the only possible way the best trisection would involve 2 cuts on the heavy branch
  # is if the best possible trisection is the best bisection of the heavy branch separated from the rest of the tree.
  #
  # Condition 2 means that we can never find a better trisection without cutting on the heavy branch than
  # we can find by cutting the heavy branch at the root and bisecting the rest of the tree. Along with condition 1,
  # this means the second cut will not be on the heavy branch, so we only need to check cuts on the remaining branches.
  #

  # Check condition 1
  heavy_bisection = heavy_cuts.closest_to(heavy_subtree.weight / 2.0)
  best_trisection_result = heavy_bisection * (heavy_subtree.weight - heavy_bisection) * (tree.size - heavy_subtree.weight)

  # Check condition 2
  # We test cuts of the heavy branch against the best bisection of the rest of the tree until the subtree of h is too small.
  heavy_cuts.reverse!
  heavy_cuts.each do |h|
    other_bisection = other_cuts.closest_to((tree.size - h) / 2.0)
    other_trisection_result = h * other_bisection * (tree.size - (h + other_bisection))
    best_trisection_result = other_trisection_result if best_trisection_result < other_trisection_result
    # If the subtree under h is smaller than the other 2 components, it will not help to make it even smaller
    break if h < other_bisection && h < (tree.size - (h + other_bisection))
  end

  [tree.size, best_bisection_result, best_trisection_result].max
end

class Cutlist < Array
  # Find the element in the self closest to target value x.
  # REQUIRES the array to be sorted smallest to largest, and contain at least 1 value.
  # O(log n) where n is size of ary
  def closest_to(x)
    raise ArgumentError.new if size == 0 or x < 0
    # First, find the smallest value in ary >= x
    i = (0...size).bsearch { |i| self[i] >= x }
    return self[-1] if i.nil?
    return self[i] if i == 0 || self[i] == x
    # Finally, check if the next lower value is closer to x, and return the best value
    raise ArgumentError.new("Array not sorted smallest to largest") unless self.fetch(i-1) < self.fetch(i)
    (x - self[i]).abs < (x - self[i-1]).abs ? self[i] : self[i-1]
  end
end

#
#   A[0] = 0    B[0] = 1
#   A[1] = 1    B[1] = 2
#   A[2] = 1    B[2] = 3
#   A[3] = 3    B[3] = 4
#   A[4] = 3    B[4] = 5
#   A[5] = 6    B[5] = 3
#   A[6] = 7    B[6] = 5

# ([0,1,1,3,3,6,7], [1,2,3,4,5,3,5])
# ([0, 1, 1, 3, 3, 6, 7], [1, 2, 3, 4, 5, 3, 5]) # 18
#
# ([0, 1], [1, 2]) # 3
#
# 1 heavy node, 1 path branch that has to be bisected.
# ([0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0], [6, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) # 54
# ([0, 0, 0, 0, 0, 5, 4, 3, 2, 1, 0], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 6]) # 54
#
# s([0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0], [6, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) # 63
#

def solution(a, b)
  s(a, b).to_s # Codility requires the result to be a string
end
"""


""" JavaScript
function setUnion(a, b) {
  const union = new Set([...a, ...b]);
  return union;
}

function setIntersection(a, b) {
  const intersection = new Set([...a].filter((x) => b.has(x)));
  return intersection;
}

function setDifference(a, b) {
  const difference = new Set([...a].filter((x) => !b.has(x)));
  return difference;
}
// ***** End: Helper functions *****

const A = [0, 1, 1, 3, 4, 5, 6, 7, 8, 8, 8];
const B = [1, 2, 4, 4, 5, 6, 7, 8, 9, 10, 11];

function highestDegree(A, B) {
  const N = A.length;

  const dict = {};
  function addElt(dict, n0, n1) {
    if (dict[n0]) {
      dict[n0].add(n1);
    } else {
      dict[n0] = new Set([n1]);
    }
  }

  for (let i = 0; i < N; ++i) {
    const n0 = A[i];
    const n1 = B[i];

    addElt(dict, n0, n1);
    addElt(dict, n1, n0);
  }

  let res = undefined;
  let maxDegree = 0;
  for (const [node, set] of Object.entries(dict)) {
    const currentDegree = set.size;
    if (maxDegree < currentDegree) {
      maxDegree = currentDegree;
      res = parseInt(node);
    }
  }

  return [res, N, dict];
}

function graphFromNode(rootNode, dict) {
  const graph = {};

  const rootNeighbourghood = dict[rootNode];

  // Initialisation of the graph
  for (let node of rootNeighbourghood) {
    graph[node] = new Set([node]);
  }

  for (const [kNode, curNeighbourghood] of Object.entries(graph)) {
    const seedNode = parseInt(kNode);

    const nodeToVisite = [seedNode];
    const alreadyVisited = new Set();
    while (nodeToVisite.length !== 0) {
      const curNode = nodeToVisite.shift();

      const accessibleNodes = dict[curNode];

      for (let node of accessibleNodes) {
        if (node !== rootNode && !alreadyVisited.has(node)) {
          curNeighbourghood.add(node);
          nodeToVisite.push(node);
        }
      }

      alreadyVisited.add(curNode);
    }

  }

  return graph;
}


function cut1Bridge(A, B, graphsFromNode) {
  let maxProd = 0;
  for (let i = 0; i < A.length; ++i) {
    const nCut0 = A[i];
    const nCut1 = B[i];
    const curGraph = graphsFromNode[nCut0];

    let comp0Size = 1;
    for (let node of Object.keys(curGraph)) {
      const iNode = parseInt(node);
      if (iNode !== nCut1) {
        comp0Size += curGraph[node].size;
      }
    }
    const comp1Size = curGraph[nCut1].size;

    const prod = comp0Size * comp1Size;

    if (maxProd < prod) {
      maxProd = prod;
    }
  }
  return maxProd;
}

function cut2Bridge(A, B, graphsFromNode) {
  let maxProd = 0;

  for (let i = 0; i < A.length - 1; ++i) {
    for (let j = i + 1; j < A.length; ++j) {
      const nCut00 = A[i];
      const nCut01 = B[i];
      const nCut10 = A[j];
      const nCut11 = B[j];

      const curGraph0 = graphsFromNode[nCut00];
      const curGraph1 = graphsFromNode[nCut10];

      let setNCut00 = new Set([nCut00]);
      for (let node of Object.keys(curGraph0)) {
        const iNode = parseInt(node);
        if (iNode !== nCut01) {
          setNCut00 = setUnion(setNCut00, curGraph0[node]);
        }
      }
      const setNCut01 = curGraph0[nCut01];

      let setNCut10 = new Set([nCut10]);
      for (let node of Object.keys(curGraph1)) {
        const iNode = parseInt(node);
        if (iNode !== nCut11) {
          setNCut10 = setUnion(setNCut10, curGraph1[node]);
        }
      }
      const setNCut11 = curGraph1[nCut11];

      console.log("nCut00", nCut00);
      console.log("nCut01", nCut01);
      console.log("nCut10", nCut10);
      console.log("nCut11", nCut11);

      let electedSet0;
      let electedSet1;
      let comp0Size;
      let comp1Size;
      if (setNCut00.has(nCut10) && setNCut00.has(nCut11)) {
        electedSet0 = setNCut00;
        comp0Size = setNCut01.size;
      } else {
        electedSet0 = setNCut01;
        comp0Size = setNCut00.size;
      }

      if (setNCut10.has(nCut00) && setNCut10.has(nCut01)) {
        electedSet1 = setNCut10;
        comp1Size = setNCut11.size;
      } else {
        electedSet1 = setNCut11;
        comp1Size = setNCut10.size;
      }

      const intersectionSet = setIntersection(electedSet0, electedSet1);

      const comp2Size = intersectionSet.size;


      const prod = comp0Size * comp1Size * comp2Size;
      console.log("prod", prod);
      console.log("");

      if (maxProd < prod) {
        maxProd = prod;
      }
    }
  }
  return maxProd;
}

function solution(A, B) {
  const [rootNode, N, dict] = highestDegree(A, B);

  if (N < 3) {
    const res = N + 1;
    return res;
  }

  const graph = graphFromNode(rootNode, dict);
  // console.log("graph", graph);

  // Don't cut bridge
  let case0Prod = 0;
  for (const [node, set] of Object.entries(graph)) {
    case0Prod += set.size;
  }
  case0Prod += 1;
  let maxProd = case0Prod;

  // Cut 1 bridge
  let graphsFromNode = {};
  for (let node = 0; node < N + 1; ++node) {
    graphsFromNode[node] = graphFromNode(node, dict);
  }

  const prodCut1 = cut1Bridge(A, B, graphsFromNode);
  if (maxProd < prodCut1) {
    maxProd = prodCut1;
  }

  const prodCut2 = cut2Bridge(A, B, graphsFromNode);
  if (maxProd < prodCut2) {
    maxProd = prodCut2;
  }

  return maxProd;
}
"""
