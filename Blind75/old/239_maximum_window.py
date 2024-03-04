class Solution:
    def maxSlidingWindow(self, nums, k):
        from collections import deque
        q = deque() # stores *indices*
        res = []
        for i, cur in enumerate(nums):
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)
            # remove first element if it's outside the window
            if q[0] == i - k:
                q.popleft()
            # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

# https://pythontutor.com/render.html#code=class%20Solution%3A%0A%20%20%20%20def%20maxSlidingWindow%28self,%20nums,%20k%29%3A%0A%20%20%20%20%20%20%20%20from%20collections%20import%20deque%0A%20%20%20%20%20%20%20%20q%20%3D%20deque%28%29%20%23%20stores%20*indices*%0A%20%20%20%20%20%20%20%20res%20%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20for%20i,%20cur%20in%20enumerate%28nums%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20q%20and%20nums%5Bq%5B-1%5D%5D%20%3C%3D%20cur%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20q.pop%28%29%0A%20%20%20%20%20%20%20%20%20%20%20%20q.append%28i%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20remove%20first%20element%20if%20it's%20outside%20the%20window%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20q%5B0%5D%20%3D%3D%20i%20-%20k%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20q.popleft%28%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20window%20has%20k%20elements%20add%20to%20results%20%28first%20k-1%20windows%20have%20%3C%20k%20elements%20because%20we%20start%20from%20empty%20window%20and%20add%201%20element%20each%20iteration%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20i%20%3E%3D%20k%20-%201%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20res.append%28nums%5Bq%5B0%5D%5D%29%0A%20%20%20%20%20%20%20%20return%20res%0A%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.maxSlidingWindow%28%5B24,1,6,3,1,6%5D,%203%29&cumulative=false&curInstr=52&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        output = []
        q = collections.deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
                
            q.append(r)

            # remove left val from window
            c = l
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

        
b = Solution()
b.maxSlidingWindow([24,1,6,3,1,6], 3)
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