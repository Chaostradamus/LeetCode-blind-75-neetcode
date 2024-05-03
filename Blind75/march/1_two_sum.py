class Solution(object):
    def twoSum(self, nums, target):
        
        res = {}

        for i , n in enumerate(nums):
          diff = target - n
          if diff in res:
            return [res[diff], i]
          res[n] = i


# o(n) runtime and space
# idea is create a hashmap and append value first as key then index as value
# this is because we are gauranteed to have exacrtly one solution so the diff has to be in the hashmap at the end
# this means that eventually the diff will equal the one of the keys in the hashmap
# we enumerate and iterate through nums
# we find the diff as target - n in nums...if the diff is found then we found a pair between the diff(key) and value(index) and current index
# else we add the current i and n with n being the key and i being the value


# 1. Two Sum
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]