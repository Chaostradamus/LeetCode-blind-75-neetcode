"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
      new = {}

      def dfs(node):
        if node in new:
          return new[node]
          
        copy = Node(node.val)
        new[node] = copy
        for nei in node.neighbors:
          copy.neighbors.append(dfs(nei))
        return copy

      return dfs(node) if node else None
    
# create a hashmap to link from old to new copies
# dfs function
#   if node is in hashmap then return that copy(this is for returning neighboring nodes)
#   create a copy = a new Node(with passed in node's.val)
#   loop through nodes neighbors and append it as copy's neighbor by calling dfs(each neighbor)
#   this should return all the neighbors to copy as a dfs 
#   each node that has been explored already will return as a neighbor of the calling node eventually bubbling back up from the deepest depth
#   it will start at node 1 go search as far as it can and finishes up with node 1's last neighbor
#   once looping is done we return that copy
# return a call on dfs(node) if theres a node else None
    

# 133. Clone Graph
# Solved
# Medium
# Topics
# Companies
# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

# Example 1:


# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# Example 2:


# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
# Example 3:

# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.