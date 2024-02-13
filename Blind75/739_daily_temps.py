class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return result
    
# you can brute force and check every temp against the rest of the list but that is (o)nsuqared
    # instead we create an array of all 0's to cover edge cases of temp days that dont reach another day that is higher
    # empty stack
    # and enumerate temps and appending that to stack...while there is still a stack and current iteration's temp is higher
    # than the previous day (top of stack) we can take the current index subtracted by the top of stack index to figure out the days inbetween temps rising
    # we keep popping and comparing until top of stack is not lower and continue
    # thought we would use hashmaps but no
    
# https://pythontutor.com/render.html#code=class%20Solution%28object%29%3A%0A%20%20%20%20def%20dailyTemperatures%28self,%20temperatures%29%3A%0A%20%20%20%20%20%20%20%20res%20%3D%20%5B0%5D%20*%20len%28temperatures%29%0A%20%20%20%20%20%20%20%20stack%20%3D%20%5B%5D%20%20%23%20pair%3A%20%5Btemp,%20index%5D%0A%0A%20%20%20%20%20%20%20%20for%20i,%20t%20in%20enumerate%28temperatures%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20stack%20and%20t%20%3E%20stack%5B-1%5D%5B0%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20stackT,%20stackInd%20%3D%20stack.pop%28%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20res%5BstackInd%5D%20%3D%20i%20-%20stackInd%0A%20%20%20%20%20%20%20%20%20%20%20%20stack.append%28%28t,%20i%29%29%0A%20%20%20%20%20%20%20%20return%20res%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.dailyTemperatures%28%5B73,74,75,71,69,72,76,73%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=2&rawInputLstJSON=%5B%5D&textReferences=false


739. Daily Temperatures
Solved
Medium
Topics
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 