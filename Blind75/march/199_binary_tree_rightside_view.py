# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        q = collections.deque([root])

        while q:
          right = None
          for i in range(len(q)):
            node = q.popleft()
            if node:
              right = node
              q.append(node.left)
              q.append(node.right)
          if right:
              res.append(right.val)
        return res
    
# we do bfs with a queue again
# we run while there is something in queue 
# we set right every iteration
    # we loop length of q times to empty out each level
    # at each iteration if there is a node we set right to popped node
    # this will give us the right most valid value
    # we append each nodes left and right also
    # once finished with the iterations we will append if there is a right.val in case its null
    # this will run while there is a queue and empty out at each level checking left to right
# return res after


# 199. Binary Tree Right Side View
# Solved
# Medium
# Topics
# Companies
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []
        
