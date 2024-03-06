import copy, array
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
    

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = copy.deepcopy(nums)
        for n in nums:
          ans.append(n)
        return ans



# 1929. Concatenation of Array
# Easy
# Topics
# Companies
# Hint
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:

# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
    
    # https://pythontutor.com/render.html#code=class%20Solution%28object%29%3A%0A%20%20%20%20def%20getConcatenation%28self,%20nums%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%3Atype%20nums%3A%20List%5Bint%5D%0A%20%20%20%20%20%20%20%20%3Artype%3A%20List%5Bint%5D%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20ans%20%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%282%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20n%20in%20nums%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ans.append%28n%29%0A%20%20%20%20%20%20%20%20return%20ans%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.getConcatenation%28%5B1,2,1%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=2&rawInputLstJSON=%5B%5D&textReferences=false


# solution 1 neetcode
# create empty array and fill it by iterating through n twice

# my solution
# make copy of nums array called ans
# iterate once through nums and append to ans array