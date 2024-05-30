class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]


      for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
          if text1[i] == text2[j]:
            dp[i][j] = 1 + dp[i +1][j+1]
          else:
            dp[i][j] = max(dp[i+1][j], dp[i][j+1])

      return dp[0][0]

# bottom up 2d dp approach
# initialize a 2d matrix with all 0's text2+1 by text1 +1 lengths
# we use text2 first because that is the columsn and text 1 is the rows
# we add a plus 1 to use the fake out of bounds as 0's
# we then start from the bottom right cell and check if tex1 and text2 match at that position
    # if they match we add 1 to that plus the diagonal bottomright cell
    # if they dont match we takr the max of the cell beneath and to the right of current cell
# return when finishe dthe top left cell
# this creates a table where if we find a match we add 1 and go diagonally and if we dont find a match we take the largest 
# value held at the right or bottom of current cell

# 1143. Longest Common Subsequence
# Solved
# Medium
# Topics
# Companies
# Hint
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.