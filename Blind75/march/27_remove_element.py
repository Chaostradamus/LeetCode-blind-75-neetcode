class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        r = len(nums)
        l = 0

        while l < r:
          if nums[l] == val:
            nums[l], nums[r-1] = nums[r-1], nums[l]
            r -= 1
          else:
            l += 1
        return r
    


# 27. Remove Element
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.
    
# https://pythontutor.com/render.html#code=class%20Solution%28object%29%3A%0A%20%20%20%20def%20removeElement%28self,%20nums,%20val%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%3Atype%20nums%3A%20List%5Bint%5D%0A%20%20%20%20%20%20%20%20%3Atype%20val%3A%20int%0A%20%20%20%20%20%20%20%20%3Artype%3A%20int%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20n%20%3D%20len%28nums%29%0A%20%20%20%20%20%20%20%20i%20%3D%200%0A%0A%20%20%20%20%20%20%20%20while%20i%20%3C%20n%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20nums%5Bi%5D%20%3D%3D%20val%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20nums%5Bi%5D,%20nums%5Bn%20-%201%5D%20%3D%20nums%5Bn%20-%201%5D,%20nums%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20n%20-%3D%201%20%20%23%20decrement%20the%20length%20of%20the%20array%20by%20discarding%20the%20last%20element%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20i%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20n%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.removeElement%28%5B0,1,2,2,3,0,4,2%5D,%202%29&cumulative=false&curInstr=28&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=2&rawInputLstJSON=%5B%5D&textReferences=false


# hold right pointer out of bounds to the right for indexing
#  left pointer at 0
#  while the pointers arent at the same spot
# if left value equals the remove value then we swap l with r-1
    # then move right one spot left -1
# else we move left counter
# we return r pointer which wil act as a pointer and countdown to how many nums left over...
    # we do full len(nums) because of indexing and countdown 
# (n) time and space because one run through and nothing created