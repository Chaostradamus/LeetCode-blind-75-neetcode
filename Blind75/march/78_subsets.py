class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


# backtracking algorith
# create 2 arrays, one for result and one to house the subsets
# helper function that takes in the index
# if index is out of bounds we reach the end of a decision tree and will append current subset
# starting off we will append nums[i] to subset
# we will then call dfs on i+1...this will go down the tree and include everything in nums
# we then pop last element and call dfs on i+1 
# call dfs on index 0 and return main res array

# this will traverse the decision tree and get all possible subsets 
# this simulates that at each level we will either take the element or not take the element
# it is log(n*2n) where first n is number of element multiplied by 2* where 2nd n is the number of decisions you can make

#                    1
#              1               _
#           1,2   1          2    _
#        1,2,3   1,2     1,3   1  





# 78. Subsets
# Medium
# Topics
# Companies
# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

# https://pythontutor.com/render.html#code=class%20Solution%3A%0A%20%20%20%20def%20subsets%28self,%20nums%29%3A%0A%20%20%20%20%20%20%20%20res%20%3D%20%5B%5D%0A%0A%20%20%20%20%20%20%20%20subset%20%3D%20%5B%5D%0A%0A%20%20%20%20%20%20%20%20def%20dfs%28i%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20i%20%3E%3D%20len%28nums%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20res.append%28subset.copy%28%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20decision%20to%20include%20nums%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20subset.append%28nums%5Bi%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20dfs%28i%20%2B%201%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20decision%20NOT%20to%20include%20nums%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20subset.pop%28%29%0A%20%20%20%20%20%20%20%20%20%20%20%20dfs%28i%20%2B%201%29%0A%0A%20%20%20%20%20%20%20%20dfs%280%29%0A%20%20%20%20%20%20%20%20return%20res%0Ab%20%3D%20Solution%28%29%0Ab.subsets%28%5B1,2,3%5D%29&cumulative=false&curInstr=99&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false