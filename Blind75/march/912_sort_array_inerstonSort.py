class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
          key = nums[i]

          j = i - 1
          while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
          nums[j+1] = key
        return nums
    

# we iterate from 1 to the end
    # we hold current value in variable to keep it 
    # set pointer behind current
    # while in bounds and current val is less than prev
    # we keep swapping and moving pointer backwards
    # once out of that loop we set prev.next value to key
    # O of N space but n^n time complexity




# 912. Sort an Array
# Medium
# Topics
# Companies
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
