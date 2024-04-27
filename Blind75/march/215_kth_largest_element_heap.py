class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      heap = nums[:k]
      heapify(heap)
      for i in range (k, len(nums)):
        if heap[0] < nums[i]:
          heappushpop(heap,nums[i])
      return heap[0]

# insert nums into a heap from o to k not included
    # this will populate an array with k amount of elements
    # we then heapify that array to have them sorted
# starting from kth index to end of nums array...we compare top of heap with ith index of nums
# if nums at ith index is larger than heaps top then we pushpop(heap, nums[i])
    # this pushes nums at i into the heap that then reorganizes everything and pops out the smallest element

# we do this till the end of the array which means we will do k amount of pops giving us the kth largest element of the array
# at the top of the min-heap

# 215. Kth Largest Element in an Array
# Solved
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
 