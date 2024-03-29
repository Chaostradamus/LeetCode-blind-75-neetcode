class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = {}
        for num in nums:
          bucket[num] = 1 + bucket.get(num, 0)
        
        l = 0
        for val, count in bucket.items():
            cur = l + count
            nums[l:cur] = [val]* count
            l = cur
        
        return nums

       
# fill up a bucket hashmap 
    # set pointer at left
    # for value and count in nums
    # current = left + count ....this tells us how far to populate the array
    # we will go from nums[left to current] * count amount of times to populate the array with correct amount
    # maybe could use a better name than current...start to finish?
    # set left to current to move pointer up to new starting point
    

# 75. Sort Colors
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.