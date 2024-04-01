class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        
        while l <= r:
          mid = (l + r) // 2
          if nums[mid] == target:
            return mid
          elif nums[mid] < target:
            l = mid + 1
          else:
            r = mid - 1
        return -1

# hold left and right pointers
    # while in bounds
    # take mid by doing l + r divided by 2...if that index contains the target return it
    # else if target is smaller than we move right to left portion of the array by doing r = mid -1 
    # if target is bigger than we need to search right portion by doing left = mid +1
    # we reset mid to inbetween new left/right and do it again
    # log N because we split N down by half every time


# 704. Binary Search
# Solved
# Easy
# Topics
# Companies
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1