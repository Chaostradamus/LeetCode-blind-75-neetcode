class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

# create a stack and append index and height if heights are in increasing order
    # while current height is lower than the top of the stack
    #  you pop and calculate the maxArea by multiplying the height by (current index - popped index)
    # then reset start last popped index to emulate what the length would be from current iteration to that index
    # after list of heights end
    # you go through reaminging stack with i , h in stack and calculate maxAreas by
    # doing height * (length of list) - i which is the index it started from from the past calculations

# 84. Largest Rectangle in Histogram
# Hard
# Topics
# Companies
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4

# # should be similar to water container algorithm but with stack usage
 

#  https://pythontutor.com/render.html#code=class%20Solution%28object%29%3A%0A%20%20%20%20def%20largestRectangleArea%28self,%20heights%29%3A%0A%20%20%20%20%20%20%20%20maxArea%20%3D%200%0A%20%20%20%20%20%20%20%20stack%20%3D%20%5B%5D%20%20%23%20pair%3A%20%28index,%20height%29%0A%0A%20%20%20%20%20%20%20%20for%20i,%20h%20in%20enumerate%28heights%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20start%20%3D%20i%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20stack%20and%20stack%5B-1%5D%5B1%5D%20%3E%20h%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20index,%20height%20%3D%20stack.pop%28%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20maxArea%20%3D%20max%28maxArea,%20height%20*%20%28i%20-%20index%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20start%20%3D%20index%0A%20%20%20%20%20%20%20%20%20%20%20%20stack.append%28%28start,%20h%29%29%0A%0A%20%20%20%20%20%20%20%20for%20i,%20h%20in%20stack%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20maxArea%20%3D%20max%28maxArea,%20h%20*%20%28len%28heights%29%20-%20i%29%29%0A%20%20%20%20%20%20%20%20return%20maxArea%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.largestRectangleArea%28%5B2,1,5,6,2,3%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=2&rawInputLstJSON=%5B%5D&textReferences=false