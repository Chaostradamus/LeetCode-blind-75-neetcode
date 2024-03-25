class Solution:
    def sortArray(self, nums):
        def partition(nums,low,high):
            pivot = (low+high)//2
            nums[pivot],nums[high] = nums[high],nums[pivot]
            
            for j in range(low,high):
                if nums[j] < nums[high]:
                    nums[low],nums[j] = nums[j],nums[low]
                    low += 1
            nums[low],nums[high] = nums[high],nums[low]
            return low
            
        def quicksort(nums,low,high):
            if low >= high:
                return
            pivot = partition(nums,low,high)
            quicksort(nums,low,pivot-1)
            quicksort(nums,pivot+1,high)
            
        quicksort(nums,low=0,high=len(nums)-1)
        return nums
 

class Solution(object):
    def sortArray(self, nums):
        def partition(array, low, high):
          pivot = array[high]
          i = low - 1

          for j in range(low, high):
            if array[j] <= pivot:
              i += 1
              array[i], array[j] = array[j], array[i]

          array[i+1], array[high] = array[high], array[i+1]
          return i+1

        def quicksort(nums, low=0, high=None):
          if high is None:
            high = len(nums) - 1

          if low < high:
            pivot_index = partition(nums, low, high)
            quicksort(nums, low, pivot_index-1)
            quicksort(nums, pivot_index+1, high)
        
        quicksort(nums, low=0, high=None)
        return nums
 

# barely understand
# set a pivot on nums at the beginning and have i, j counters ate low and high(start, end)
# while i is less than J (in bounds)
    # while ith index value is less than or equal to pivot we move i pointer
    # while j is is greater than pivot we move j inwards
    # we swap when both conditions are met until i passes j
    # we swap j and low and return j as next pivot index
# in the main function while low is less than high(in bounds)
    # j (pivot) = partition of (low and high)
    # call quicksort on left and right of pivot


    #use first element as pivot
# set i and j at opposite ends
    # while in bounds and nums[i] is less than pivot value move i...do inverse for j
    # swap when criteria are met and keep going until i moves past j
    # swap low and j values
    # pass in new boundaries for sorting again
    # l and j and j+1 and h
    # return nums
        
# b = Solution()
# b.sortArray([12,11,13,5,6])



# # 912. Sort an Array
# # Attempted
# # Medium
# # Topics
# # Companies
# # Given an array of integers nums, sort the array in ascending order and return it.

# # You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# # Example 1:

# # Input: nums = [5,2,3,1]
# # Output: [1,2,3,5]
# # Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# # Example 2:

# # Input: nums = [5,1,1,2,0,0]
# # Output: [0,0,1,1,2,5]
# # Explanation: Note that the values of nums are not necessairly unique.
 