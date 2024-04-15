# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        n = 0

        stack = []
        curr = root

        while curr or stack:
          while curr:
            stack.append(curr)
            curr = curr.left
          curr = stack.pop()
          n += 1
          if k == n:
            return curr.val
          curr = curr.right
        
# using stack to iteratively traverse in order
# while there is a current node OR something in stack:
# while theres a current node we will append current node to stack and move leftward
# if we cant move leftward we are at lowest node
# we pop from stack and decrease K and check if k is zero
# if k is zero then we return the current nodes val
# else we set cur to right and repeat the process of finishing all cur.right's leftmost subtree to find smallest value
# once left subtree is done stack will help us pop all the way back up to parent subtree
# log N i think timeand space



# 230. Kth Smallest Element in a BST
# Solved
# Medium
# Topics
# Companies
# Hint
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3