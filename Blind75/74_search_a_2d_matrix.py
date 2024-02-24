class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

        # https://pythontutor.com/render.html#code=class%20Solution%28object%29%3A%0A%20%20%20%20def%20searchMatrix%28self,%20matrix,%20target%29%3A%0A%20%20%20%20%20%20%20%20ROWS,%20COLS%20%3D%20len%28matrix%29,%20len%28matrix%5B0%5D%29%0A%0A%20%20%20%20%20%20%20%20top,%20bot%20%3D%200,%20ROWS%20-%201%0A%20%20%20%20%20%20%20%20while%20top%20%3C%3D%20bot%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20row%20%3D%20%28top%20%2B%20bot%29%20//%202%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20target%20%3E%20matrix%5Brow%5D%5B-1%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20top%20%3D%20row%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20target%20%3C%20matrix%5Brow%5D%5B0%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20bot%20%3D%20row%20-%201%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%0A%0A%20%20%20%20%20%20%20%20if%20not%20%28top%20%3C%3D%20bot%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20row%20%3D%20%28top%20%2B%20bot%29%20//%202%0A%20%20%20%20%20%20%20%20l,%20r%20%3D%200,%20COLS%20-%201%0A%20%20%20%20%20%20%20%20while%20l%20%3C%3D%20r%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20m%20%3D%20%28l%20%2B%20r%29%20//%202%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20target%20%3E%20matrix%5Brow%5D%5Bm%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20l%20%3D%20m%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20target%20%3C%20matrix%5Brow%5D%5Bm%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20r%20%3D%20m%20-%201%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20return%20False%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.searchMatrix%28%5B%5B1,3,5,7%5D,%5B10,11,16,20%5D,%5B23,30,34,60%5D%5D,%2030%29&cumulative=false&curInstr=17&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=2&rawInputLstJSON=%5B%5D&textReferences=false


74. Search a 2D Matrix
Medium
Topics
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 