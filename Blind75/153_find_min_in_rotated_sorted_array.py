class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r, = 0 , len(nums) -1
        
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min (res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m -1
        
        return res

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

# o(logn) time and o(1) space
# set l and right pointers
# while nums.left is less than nums.right
# if nums.left is less than nums.right than take min of left and result and return
# this is because itll be the smallest in the sorted split
# set mid pointer
# take min of res and mid.val
# if mid.val is greater thn left.val then reset left to be mid+1...moves pointer to search the other sorted array
# otherwise set right to mid - 1 to search the other sorted array
# binary search on array that is sorted
    
# https://pythontutor.com/render.html#code=import%20math%0Aclass%20Solution%28object%29%3A%0A%20%20%20%20%20def%20findMin%28self,%20nums%29%3A%0A%20%20%20%20%20%20%20%20res%20%3D%20nums%5B0%5D%0A%20%20%20%20%20%20%20%20l,%20r%20%3D%200,%20len%28nums%29%20-1%0A%0A%20%20%20%20%20%20%20%20while%20l%20%3C%3D%20r%3A%0A%20%20%20%20%20%20%20%20%20%20if%20nums%5Bl%5D%20%3C%20nums%5Br%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20res%20%3D%20min%28res,%20nums%5Bl%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20%20%20mid%20%3D%20%28l%20%2B%20r%29%20//%202%0A%20%20%20%20%20%20%20%20%20%20res%20%3D%20min%28res,%20nums%5Bmid%5D%29%0A%20%20%20%20%20%20%20%20%20%20if%20nums%5Bmid%5D%20%3E%3D%20nums%20%5Bl%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20l%20%3D%20mid%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20else%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20r%20%3D%20mid%20-%201%0A%20%20%20%20%20%20%20%20return%20res%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.findMin%28%5B1,2,3,4,5,6%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=2&rawInputLstJSON=%5B%5D&textReferences=false

