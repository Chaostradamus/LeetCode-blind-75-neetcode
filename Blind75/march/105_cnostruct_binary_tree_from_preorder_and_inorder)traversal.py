# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
          return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

# preorder processes the root first
# inorder will return tree in ascending order
# we use thi sknowledge by using preorders first node as the root of the entire tree
# we know everything left of the root will be on the left subtree for the inorder array
# we know everything to the right of the both indices of root will be right subtree
# we call builTree for left to be 
    # preorder(everything from after root up to mid) takes this everything after the current root and up to mid(inorder's index of root)
    # inorder(everything up to mid) this passes in everything from the start up to the current root(known from preorder)
    # this supplies the entire left subtree of current root
# we call buildtree on the right from everything after mid for both pre/inorder arrays
# return root after finished




# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Solved
# Medium
# Topics
# Companies
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]