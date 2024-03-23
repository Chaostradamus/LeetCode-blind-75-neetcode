class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l == r:
                return arr
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr
        
        return mergeSort(nums, 0, len(nums) - 1)
    


# for mergeSort we have to define a mergeSorting function
    # sorting function takes the array left middle and right pointers
        # we define left and right by splitting the list in half
        # create 3 pointers for left list right list and main array
        # we then while pointers are in bounds iterate through head of arrays by value and appending them to main array
    # and then moving pointers..if one list is empty we append the rest either listby doing:
    # while j less than length of left:
    # nums[i] = left[j] and then increase both pointers to append rest of array
    # vice versa for right

    # then you call mergesort main function
    # first it wreturn if base case is found
    # defines middle
    # calls mergesort on l to middle
    # then middle to right
    # then merge function called
    # this will work like depth first search to find base case and returning back up and merging at each breath
    


# 912. Sort an Array
# Medium
# Topics
# Companies
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.