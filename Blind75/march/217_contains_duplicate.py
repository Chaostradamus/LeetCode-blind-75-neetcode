class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for n in nums:
          if n in hashSet:
            return True
          hashSet.add(n)
        return False


# create a hashset and iterate through nums
# if hashset contains n then return true else we add to hashset and return false when done
# o(n) time and space


# 217. Contains Duplicate
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 