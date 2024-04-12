# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
          return root
        if key > root.val:          
          root.right = self.deleteNode(root.right, key)
        elif key < root.val:          
          root.left = self.deleteNode(root.left, key)
        else:
          if not root.left:
            return root.right
          if not root.right:
            return root.left
          
          
          cur = root.right
          while cur.left:
            cur = cur.left
          root.val = cur.val
          root.right = self.deleteNode(root.right, root.val)
        return root
    
# o(h) 
# if theres no root then we return prev root
# we search for the correct node by comparing values and recursively searching left or right with originsl function
# if no comparison works then we found the node....if the node i empty on either side starting from the left then we dont have to do nything
# but return the opposite

# the magic
# we search smallest value of right subtree because the smallest value will still be bigger than the current deleted root's value
# once we find smallest left value of right subtree we swap values with the root node
# then we call delete node on roots.right to keep balancing the subtree
# we return root at the end


# 450. Delete Node in a BST
# Solved
# Medium
# Topics
# Companies
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []
 