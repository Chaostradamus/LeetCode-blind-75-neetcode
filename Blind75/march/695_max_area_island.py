class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        area = 0
        
        
        def dfs(r, c):
            nonlocal area
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            area = 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for rc, cc in directions:
              area += dfs(r + rc, c + cc)
            return area

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
             ans = max(ans, dfs(r, c))
        return ans


# same as number of islands
# we set rows columns and a set
# because we have area outside of the helper function ..to change it we have to declare nonlocal area inside the helper
# we check if its inbounds a non island or in visit set first
# if not we add to set and declare area = 1
# we create a directions array with sublists of movement patterns and then for loop thourhg each sublist of elements
# and run area += dfs of each direction and return area
# outside of th ehelper function we declare answer as 0 and loop through the grid and keeping a max between ans and first dfs call
# return ans


# 695. Max Area of Island
# Medium
# Topics
# Companies
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 