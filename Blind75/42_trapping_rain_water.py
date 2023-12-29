class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
           return 0
        l,r = 0, len(height) -1
        maxl, maxr = height[l], height[r]
        water = 0

        while l < r:
          if maxl < maxr:
            l += 1
            maxl = max(maxl, height[l])
            water += maxl - height[l]
          else:
            r -= 1
            maxr = max(maxr, height[r])
            water += maxr - height[r]
        return water



# https://pythontutor.com/render.html#code=class%20Solution%28object%29%3A%0A%20%20%20%20def%20trap%28self,%20height%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%3Atype%20height%3A%20List%5Bint%5D%0A%20%20%20%20%20%20%20%20%3Artype%3A%20int%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20if%20not%20height%3A%0A%20%20%20%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20%20%20%20%20l,r%20%3D%200,%20len%28height%29%20-1%0A%20%20%20%20%20%20%20%20maxl,%20maxr%20%3D%20height%5Bl%5D,%20height%5Br%5D%0A%20%20%20%20%20%20%20%20water%20%3D%200%0A%0A%20%20%20%20%20%20%20%20while%20l%20%3C%20r%3A%0A%20%20%20%20%20%20%20%20%20%20if%20maxl%20%3C%20maxr%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20l%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20maxl%20%3D%20max%28maxl,%20height%5Bl%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20water%20%2B%3D%20maxl%20-%20height%5Bl%5D%0A%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20r%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20maxr%20%3D%20max%28maxr,%20height%5Br%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20water%20%2B%3D%20maxr%20-%20height%5Br%5D%0A%20%20%20%20%20%20%20%20return%20water%0A%0A%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.trap%28%5B0,1,0,2,1,0,1,3,2,1,2,1%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
# two pointer solution
# 42. Trapping Rain Water
# Hard
# 30.1K
# 444
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 