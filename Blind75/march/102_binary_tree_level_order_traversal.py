# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
              node = q.popleft()
              if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level:
              res.append(level)
        return res
    
# using a queue
# while theres a q we create an empty levels array 
    # run another loop range of length of current q times
    # fi there is a node append it to levels and then append left and right to stack
    # after that append level to res

# simplified
# we add root and process it and then append left and right
# 2nd level will have x amount of items so we should loop through x amount of times
# we first pop from deque and process it and then append its left and right
# we use if checks in case there are nulls








# 102. Binary Tree Level Order Traversal
# Solved
# Medium
# Topics
# Companies
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []