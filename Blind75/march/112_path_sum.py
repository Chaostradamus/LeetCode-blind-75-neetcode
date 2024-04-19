# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        def dfs(node, curSum):
          if not node:
            return False
          curSum += node.val
          if not node.right and not node.left:
            return curSum == targetSum
          return (dfs(node.left, curSum) or dfs(node.right,curSum))
        
        return dfs(root, 0)
    
    
# my first attempt...didndt check if its a leaf node and unsure how to return
# right idea of traversing while keeping a sum and returning but did it backwards from optimal solution

        # if not root:
        #   return
        # cur = root
        # targetSum = targetSum - cur.val
        # if targetSum == 0:
        #   return True
        # if targetSum < 0:
        #   return
        # self.hasPathSum(cur.left, targetSum)
        # self.hasPathSum(cur.right, targetSum)
        # print(targetSum)
        # return False

# create helper function inside that will return False if theres no node to start signialling empty tree
# function takes in a node and a current sum
# add current nodes val to cursum
# check if current node is a leaf (no left or right) and then return true if current sum matches target
# else we will call dfs on left and right passing in current sum
# we can call it as a return statement (condition 1 or condition 2) which will return true if its true and false if not



# 112. Path Sum
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
# Example 3:

# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.