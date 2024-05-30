class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
      m, n = len(grid), len(grid[0])
      dp = [0] * n
      dp[n-1] = 1

      for r in reversed(range(m)):
        for c in reversed(range(n)):
          if grid[r][c]:
            dp[c] = 0
          elif c + 1 < n:
            dp[c] = dp[c] + dp[c + 1]
      return dp[0]
        
# same as unique paths 1 but with roadblocks
# initialize rows and colum lengths first
# set a dp board with an entire row length size of columns  with 0's
# set last element in that row as 1 to show there is one path to the end
# looping by rows and inner loop by columns in reversed order for both
# if its a blocked off cell then set it to 0
# else if its in bounds...we dont need to check in bounds vertically only laterally because we will always use the cell value in place vertically
# to check if its in bounds we just need to check if column +1 is less than column length
#  if it is then we add up current cell(which will be the cell below here) + plus cell to the right [c +1]
# return dp[0] at the end

# https://pythontutor.com/render.html#code=%0Afrom%20typing%20import%20List%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20uniquePathsWithObstacles%28self,%20grid%3A%20List%5BList%5Bint%5D%5D%29%20-%3E%20int%3A%0A%20%20%20%20%20%20%20%20M,%20N%20%3D%20len%28grid%29,%20len%28grid%5B0%5D%29%0A%20%20%20%20%20%20%20%20dp%20%3D%20%5B0%5D%20*%20N%0A%20%20%20%20%20%20%20%20dp%5BN-1%5D%20%3D%201%0A%0A%20%20%20%20%20%20%20%20%23%20Time%3A%20O%28N*M%29,%20Space%3A%20O%28N%29%0A%20%20%20%20%20%20%20%20for%20r%20in%20reversed%28range%28M%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20c%20in%20reversed%28range%28N%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20grid%5Br%5D%5Bc%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20dp%5Bc%5D%20%3D%200%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20elif%20c%20%2B%201%20%3C%20N%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20dp%5Bc%5D%20%3D%20dp%5Bc%5D%20%2B%20dp%5Bc%20%2B%201%5D%0A%20%20%20%20%20%20%20%20return%20dp%5B0%5D%0A%0Ab%20%3D%20Solution%28%29%0Ab.uniquePathsWithObstacles%28%5B%5B0,0,0%5D,%5B0,1,0%5D,%5B0,0,0%5D%5D%29&cumulative=false&curInstr=48&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

# 63. Unique Paths II
# Medium
# Topics
# Companies
# Hint
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:


# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1