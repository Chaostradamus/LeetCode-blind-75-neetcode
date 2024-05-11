class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # rows, cols = len(grid), len(grid[0])
        # visit = set()
        # islands = 0
        
        # def bfs(r, c):
        #     q = collections.deque()
        #     visit.add((r,c))
        #     q.append((r,c))
        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #         for dr, dc in directions:
        #             r,c = row +dr, col +dc
        #             if(r in range(rows) and c in range(cols) and grid[r][c] =='1' and (r,c) not in visit):
        #                 q.append((r,c))
        #                 visit.add((r,c))
                        
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] =='1' and(r,c) not in visit:
        #             bfs(r,c)
        #             islands +=1
        # return islands
        if not grid or not grid[0]:
          return 0
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return
          
            visit.add((r,c))
            directions = [[0,1], [1,0] , [0, -1], [-1, 0]]
            for dr, dc in directions:
              dfs(r + dr, c +dc)

        for r in range(rows):
          for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visit:
              islands += 1
              dfs(r,c)
        return islands



# 200. Number of Islands
# Solved
# Medium
# Topics
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
