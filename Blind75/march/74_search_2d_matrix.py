class Solution(object):
    def searchMatrix(self, matrix, target):
      rows, cols = len(matrix), len(matrix[0])
      
      top, bottom  = 0, rows -1

      while top <= bottom:
        mid = (top + bottom) // 2
        if target > matrix[mid][-1]:
          top = mid + 1
        elif target < matrix[mid][0]:
          bottom = mid - 1
        else:
          break
      if not (top <= bottom):
        return False
      
      l = 0
      r = cols -1
      row = (top + bottom) // 2
      while l <= r:
            mid = (l+r) // 2
            if target == matrix[row][mid]:
              return True
            elif target < matrix[row][mid]:
              r = mid -1
            elif target > matrix[row][mid]:
              l = mid + 1
      return False
# make sure to add parens on top + bottom
    # set rows and cols 
    # to find correct row we just do binry search on the matrix just a little different
    # check target againstlast value of row and move pointer 
    # or check target with first val of row and move pointer
    # if neither if checks fit then the target is in the middle of that row so break oout of the loop
    # if not in bounds tho then return false
    # after that we can do binary search like normal on that row

# my solution which is N * log(m*n) cause iterates through entire rows vs binary searching them

class Solution(object):
    def searchMatrix(self, matrix, target):
      

      for n in range(len(matrix)):
        if target ==  matrix[n][-1]:
           return True
        if target < matrix[n][-1]:
          l = 0
          r = len(matrix[n])
          mid = (l+r) // 2
          while l <= r:
            mid = (l+r) // 2
            if matrix[n][mid] == target:
              return True
            elif matrix[n][mid] < target:
              l = mid + 1
            else:
              r = mid - 1
        
          return None
# 74. Search a 2D Matrix
# Attempted
# Medium
# Topics
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# https://pythontutor.com/render.html#code=class%20Solution%3A%0A%20%20%20%20def%20searchMatrix%28self,%20matrix,%20target%29%3A%0A%20%20%20%20%20%20rows,%20cols%20%3D%20len%28matrix%29,%20len%28matrix%5B0%5D%29%0A%20%20%20%20%20%20%0A%20%20%20%20%20%20top,%20bottom%20%20%3D%200,%20rows%20-1%0A%0A%20%20%20%20%20%20while%20top%20%3C%3D%20bottom%3A%0A%20%20%20%20%20%20%20%20mid%20%3D%20%28top%20%2B%20bottom%29%20//%202%0A%20%20%20%20%20%20%20%20if%20target%20%3E%20matrix%5Bmid%5D%5B-1%5D%3A%0A%20%20%20%20%20%20%20%20%20%20top%20%3D%20mid%20%2B%201%0A%20%20%20%20%20%20%20%20elif%20target%20%3C%20matrix%5Bmid%5D%5B0%5D%3A%0A%20%20%20%20%20%20%20%20%20%20bottom%20%3D%20mid%20-%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20if%20not%20%28top%20%3C%3D%20bottom%29%3A%0A%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%0A%20%20%20%20%20%20l%20%3D%200%0A%20%20%20%20%20%20r%20%3D%20cols%20-1%0A%20%20%20%20%20%20row%20%3D%20%28top%20%2B%20bottom%29%20//%202%0A%20%20%20%20%20%20while%20l%20%3C%3D%20r%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20mid%20%3D%20%28l%2Br%29%20//%202%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20target%20%3D%3D%20matrix%5Brow%5D%5Bmid%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20target%20%3C%20matrix%5Brow%5D%5Bmid%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20r%20%3D%20mid%20-1%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20target%20%3C%20matrix%5Brow%5D%5Bmid%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20l%20%3D%20mid%20%2B%201%0A%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.searchMatrix%28%5B%5B1%5D,%5B3%5D,%5B5%5D%5D,%205%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false