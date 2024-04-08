# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
          return
        if root.val == val:
            return root
        elif root and root.val > val:
            return self.searchBST(root.left, val)
        elif root and root.val < val:    
            return self.searchBST(root.right, val)
        else:
          return None

# recursive solution
# make sure to check if root and then if roots value is larger or smaller than val
# dont forget to return the recursive calls



# 700. Search in a Binary Search Tree
# Easy
# Topics
# Companies
# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:


# Input: root = [4,2,7,1,3], val = 5
# Output: []
 