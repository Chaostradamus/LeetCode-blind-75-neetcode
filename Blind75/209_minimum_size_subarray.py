class Solution(object):
    class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        total = 0

        res = float("inf")

        for r in range(len(nums)):
          total += nums[r]
          while total >= target:
            res = min(r-l+1, res)
            total = total - nums[l]
            l +=1
        return 0 if res == float("inf") else res

        


# sliding window technique with l and r while holding a live total and minimum between answers
# slide r pointer and add to total
# while checking if total meets or exceeds target
# if it exceeds then take mininum length between current res or current length of window
# subtract nums[l] from total and slide left window over




# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
        
# https://pythontutor.com/render.html#code=class%20Solution%28object%29%3A%0A%20%20%20%20def%20minSubArrayLen%28self,%20target,%20nums%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%3Atype%20target%3A%20int%0A%20%20%20%20%20%20%20%20%3Atype%20nums%3A%20List%5Bint%5D%0A%20%20%20%20%20%20%20%20%3Artype%3A%20int%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20l%20%3D%200%0A%20%20%20%20%20%20%20%20total%20%3D%200%0A%0A%20%20%20%20%20%20%20%20res%20%3D%20float%28%22inf%22%29%0A%0A%20%20%20%20%20%20%20%20for%20r%20in%20range%28len%28nums%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20total%20%2B%3D%20nums%5Br%5D%0A%20%20%20%20%20%20%20%20%20%20while%20total%20%3E%3D%20target%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20res%20%3D%20min%28r-l%2B1,%20res%29%0A%20%20%20%20%20%20%20%20%20%20%20%20total%20%3D%20total%20-%20nums%5Bl%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20l%20%2B%3D1%0A%20%20%20%20%20%20%20%20return%200%20if%20res%20%3D%3D%20float%28%22inf%22%29%20else%20res%20%20%0Ab%20%3D%20Solution%28%29%0Ab.minSubArrayLen%287,%20%5B2,3,1,2,4,3%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false