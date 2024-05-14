class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh , time = 0, 0
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(len(grid)):
          for c in range(len(grid[0])):
            if grid[r][c] == 1:
              fresh += 1
            if grid[r][c] == 2:
              q.append((r,c))
        
        while q and fresh > 0:

          for i in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
              row, col = r + dr, c + dc
              if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                grid[row][col] = 2
                q.append((row,col))
                fresh -= 1
          time += 1
        return time if fresh == 0 else -1
    
# first initialize a queue and freshoranges and time variables
# we need to find all fresh and rotten oranges first
# loop through the grid and add 1 each time fresh orange is found and append coordinates to queue each time rotten one is found
# while queue isnt empty and fresh oranges is greater than 0
#   we will loop through the queueu len of Q times 
#   pop from queue's left and set as rows cols 
#  create directions array to move up down left right
#   loop through each subsets two value slike for dr and dc in directions
#   set rows and cols as r + dr , c + dc
#   check if the row and column spot in bounds (in range of grid and grid[0]) and if grid at [rows][cols] == 1
#   if its fresh turn to rotten and add that spot to queue
    # drecrease fresh by 1 each time also
# after each time emptying through the queue we add 1 to time...counts as 1 minute or one breathe of the bfs
# at the end we return time if fresh oranges = 0 else we truen -1

# https://pythontutor.com/render.html#code=%0Aimport%20collections%0Aclass%20Solution%3A%0A%20%20%20%20def%20orangesRotting%28self,%20grid%29%3A%0A%20%20%20%20%20%20%20%20q%20%3D%20collections.deque%28%29%0A%20%20%20%20%20%20%20%20fresh%20,%20time%20%3D%200,%200%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20directions%20%3D%20%5B%5B0,%201%5D,%20%5B0,%20-1%5D,%20%5B1,%200%5D,%20%5B-1,%200%5D%5D%0A%0A%20%20%20%20%20%20%20%20for%20r%20in%20range%28len%28grid%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20for%20c%20in%20range%28len%28grid%5B0%5D%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20grid%5Br%5D%5Bc%5D%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20fresh%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20grid%5Br%5D%5Bc%5D%20%3D%3D%202%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20q.append%28%28r,c%29%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20while%20q%20and%20fresh%20%3E%200%3A%0A%0A%20%20%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28q%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20r,%20c%20%3D%20q.popleft%28%29%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20dr,%20dc%20in%20directions%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20row,%20col%20%3D%20r%20%2B%20dr,%20c%20%2B%20dc%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20%28row%20in%20range%28len%28grid%29%29%20and%20col%20in%20range%28len%28grid%5B0%5D%29%29%20and%20grid%5Brow%5D%5Bcol%5D%20%3D%3D%201%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20grid%5Brow%5D%5Bcol%5D%20%3D%202%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20q.append%28%28row,col%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20fresh%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20time%20%2B%3D%201%0A%20%20%20%20%20%20%20%20return%20time%20if%20fresh%20%3D%3D%200%20else%20-1%0A%0Ab%20%3D%20Solution%28%29%0Ab.orangesRotting%28%5B%5B2,1,1%5D,%5B1,1,0%5D,%5B0,1,1%5D%5D%29&cumulative=false&curInstr=58&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false




# 994. Rotting Oranges
# Solved
# Medium
# Topics
# Companies
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.