# class Solution:
#   def findKthLargest(self, nums, k):
#     k = len(nums) - k

#     def quickSelect(l, r):
#       p, pivot = l, nums[r]

#       for i in range(l, r):
#         if nums[i] <= pivot:
#           nums[p], nums[i] = nums[i], nums[p]
#           p += 1
#       nums[p], nums[r] = nums[r], nums[p]
      
#       if p > k: return quickSelect(l, p -1)
#       elif p < k: return quickSelect(p +1, r)
#       else: return nums[p]
#     return quickSelect(0, len(nums) -1)



# we perform quick sort on the array to find kth largest element
# by perorming quickselect we find the correct spot for each pivot
# if that pivot index matches len(nums) - k, then we have the correct kth largest element
# we pass in 0 in end of nums as pivot for parameters for initial quicksort
# we establish pointers l r and pivot pointer starting at beginning 
# we iterate through and swap every place with nums[i] and pivot pointer if its smaller than the pivot value which is at the end
# this will leave all nunbers smaller on the left and find us the pivots correct index in nums
# if they pivot index and k match we return 
# else we call function again recursively
# if found pivot index is bigger we call it on the left side (l , p-1)
# if found pivot index is smaller we call it on the right side (p+1, r)


# 215. Kth Largest Element in an Array
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104