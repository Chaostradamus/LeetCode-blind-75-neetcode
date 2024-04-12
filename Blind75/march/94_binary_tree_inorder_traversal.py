# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # iterative
        # keep a stack to pop back up tree correctly
        # while theres a current node or something in the stack
        # while there is a current node ( not traveled to a null node)
        # we add to stack then keep travelling left
        # once at lowest depth we pop node from stack and add val to res
        # we then traverse to the .right to repeat everything again

        res = []
        stack = []
        cur = root

        while cur or stack:
          while cur:
            stack.append(cur)
            cur = cur.left
          cur = stack.pop()
          res.append(cur.val)
          cur = cur.right
        return res

        # recursive

        # base case is null
        # the previous call will call on it's left...once it returns the next line is to add val to res
        # then call helper function on right side
        # call helper on main parent root and return the res

        res = []

        def helper(root):
          if not root:
            return
          helper(root.left)
          res.append(root.val)
          helper(root.right)
          
        helper(root)
        return res

# 94. Binary Tree Inorder Traversal
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 