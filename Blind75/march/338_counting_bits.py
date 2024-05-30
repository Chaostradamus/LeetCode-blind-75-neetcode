class Solution:
    def countBits(self, n: int) -> List[int]:
      dp = [0] * (n+1)
      offset = 1

      for i in range(1, n + 1):
        if offset * 2 == i:
          offset = i
        dp[i] = 1 + dp[i - offset]
      return dp
    
# dp problem where we alter array in place
# keep an offset variable to figure out which power of 2 we are at
# if we are at a power of 2 then we set offset to i
# we then set current cell to be +1 to whatever dp @i - offset is

# Code
# Testcase
# Testcase
# Test Result
# 338. Counting Bits
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 
        