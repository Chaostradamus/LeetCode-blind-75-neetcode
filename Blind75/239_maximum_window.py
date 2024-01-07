# my solution passed 34/51 test cases. not taking lists of 2 into account i think

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l, r = 0 , k-1

        res = []
        if len(nums) ==1:
          res.append(nums[0])
          return res
        while r < len(nums):
          l2, r2 = l, r
          biggest = 0
          while l2 < r2:
            biggest = max(nums[l2], nums[r2])

            if nums[l2] < nums[r2]:
              l2 += 1
            else:
              r2 -= 1
          res.append(biggest)
          l += 1
          r += 1
        return res

# try #1 tried double slidinig windows. window within a window but only passed 37/51 test cases. think it has to do with length of nums edge cases

# 239. Sliding Window Maximum
# Hard
# 17.5K
# 622
# Companies
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]