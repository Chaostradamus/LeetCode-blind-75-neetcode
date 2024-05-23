class Solution:
    def uniquePaths(self, row: int, col: int) -> int:
        row = [1] * col

        for i in range(row-1):
          newRow = [1] * col
          for j in range(col-2, -1, -1):
            newRow[j] = newRow[j +1] + row[j]
          row = newRow
        return row [0]
    

# the thought process here i to work backwards from the finish
# going backwards we go up and left
# we initialize the first row of 1's
# we loop through the number of rows starting from the bottom one
    # create new row same as we did with row
    # loop through the number of columns working from the second to last column adding the right and underneath values 
        # outside of the column loop we initialize row as newRow
# outside of the loops we return row [0] which will be the cumulative addition of all the steps

# 62. Unique Paths
# Solved
# Medium
# Topics
# Companies
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down