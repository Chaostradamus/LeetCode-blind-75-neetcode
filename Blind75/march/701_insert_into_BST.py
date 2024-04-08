# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if not root:
          return TreeNode(val)
        if val > root.val:
          root.right = self.insertIntoBST(root.right, val)
        else:
          root.left = self.insertIntoBST(root.left, val)
        return root
    
# recursive solution is o(h) where h is height and space is o(n) because of call stack
# if no root then we return single new root with val
# else we check val against roots value and call function recursively. this will dig down to the lowest child and insert it
# return the root after
        

        # if not root:
        #   return TreeNode(val)
        # cur = root
        # while True:
        #   if val > cur.val:
        #     if not cur.right:
        #       cur.right = TreeNode(val)
        #       return root
        #     cur = cur.right
        #   else:
        #     if not cur.left:
        #       cur.left = TreeNode(val)
        #       return root
        #     cur = cur.left

# slightly less efficient but constant time space because of pointer
# we check if empty tree than just return single node with new val
# while theres a root
# then if val is less than or greater to root..
# then we check if it even has a next node to travel to. if it doesnt then set the next node to a new treenode with val and return
# if next node does exist tho we just set the pointer from cur to cur.left or right



# 701. Insert into a Binary Search Tree
# Solved
# Medium
# Topics
# Companies
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:

# Example 2:

# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# Example 3:

# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
 