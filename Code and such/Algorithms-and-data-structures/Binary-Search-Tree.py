class BSTnode:           
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
# Class defining the structure of BST node objects

class BST:
    def __init__(self):
        self.root = None

#------------------------------------------- Private methods ------------------------------------------
    def _Insertnode(self, node, key):
        if node is None:
            return BSTnode(key)
        else:
            if key < node.key:
                node.left = self._Insertnode(node.left, key)
            elif key > node.key:
                node.right = self._Insertnode(node.right, key)
        return node
# Recursive insertion method that performs a binary search to find the correct
# position to insert a new node by comparing key values
  
    def _Findnode(self, node, query, depth = 0):
        if node is None:
            return None
        elif node.key == query:
            return (node, depth)
        elif query < node.key:
            return self._Findnode(node.left, query, depth + 1)
        elif query > node.key:
            return self._Findnode(node.right, query, depth + 1)
# Recursive lookup method performing a binary search by comparing a node's key
# value to a query value and recursing down the tree until a match is found while
# incrementing an integer each step to find the depth of the node being searched for

    def _FindDeepestNode(self, node):
        if node is None:
            return ([], -1)
        
        if node.left is None and node.right is None:
            return ([node], 0)
        
        lNode, lDepth = self._FindDeepestNode(node.left)
        rNode, rDepth = self._FindDeepestNode(node.right)

        lDepth += 1
        rDepth += 1
        
        if lDepth > rDepth:
            return (lNode, lDepth)
        elif rDepth > lDepth:
            return (rNode, rDepth)
        else:
            deepestList = rNode + lNode
            return (deepestList, lDepth)
# Post-order traversal method recursively navigates the whole tree to find and
# compare the deepest node of each subtree from the root

    def _FindTotalNodes(self, node):
            if node is None:
                return 0
            return 1 + self._FindTotalNodes(node.left) + self._FindTotalNodes(node.right)
# Post-order traversal method recursively navigates the whole tree to tally the total
# number of nodes

#-------------------------------------- Public Interface methods --------------------------------------

    def Insert(self, key):
        self.root = self._Insertnode(self.root, key)

    def Find(self, query):
        result = self._Findnode(self.root, query)
        if result:
            node, depth = result
            print(f"A node with the key: {node.key} is present at a depth of: {depth}")
            return (node.key, depth)
        print(f"No key with the value {query} is present")
        return None

    def DeepestNode(self):
        nodes, depth = self._FindDeepestNode(self.root)
        if nodes:
            keys = [node.key for node in nodes]
            print(f"The deepest node(s): {keys}, and their depth: {depth}")
            return (keys, depth)
        print("Empty tree :(")
        return ([], -1)
    
    def Magnitude(self):
        total = self._FindTotalNodes(self.root)
        print(f"There are {total} total nodes")
        return total
# Helper methods to separate out interface & logic concerns while providing a more
# user-friendly syntax to hide unecessary implementation details

import random
tree = BST()

a = random.sample(range(1, 20000000), 10000000)
for i in a:
    tree.Insert(i)

tree.DeepestNode()
tree.Magnitude()

