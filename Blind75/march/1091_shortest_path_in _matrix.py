class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
      direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]
      n = len(grid)
      visit = set((0,0))
      q = deque([(0,0,1)])

      while q:
        r, c, length = q.popleft()
        if (min(r, c) < 0 or max(r,c) >= n or grid[r][c] == 1):
          continue
        if r == n-1 and c == n -1:
          return length
        for dr, dc in direct:
          if (r+ dr, c + dc) not in visit:
            q.append((r+dr, c + dc, length +1))
            visit.add((r + dr, c + dc))
      return -1

# for bfs we used  queue
# initialize length variables and 8 point direction array
# initialize queue and visited set and place initial grid spot appended. also set length to queue tuple to keep track of length

# while there is  q
# we pop from queue's left and set the tuple to row col length
#  we will check if its in bounds or is a blocked spot then we continie
# if itsat the end location we return length
# then we loop through all the sublists of directions
#   if r and c with the dr and cc added isnt in visit then we append it and add 1 to length
#   the we add it to visited
# return -1 at the end which means no possible path to the end

# 1091. Shortest Path in Binary Matrix
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1