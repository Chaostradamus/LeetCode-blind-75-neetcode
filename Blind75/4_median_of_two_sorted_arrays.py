class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

# instead of merging both lists completely, we take half of the shorter list and use that half to partition the second list
# we set list A and B with A-left and b-left as the cutoff and a-right and b-right as the next markers
# the partition will be correct is a-left and bleft are less than the opposite rights
# if that isnt the case then we do binary search on the shorter list
# if it is than we we check if the total length is odd then we take minimum of the rights
# if the total is odd ten we take the max of the lefts and the minimum of the rights and divide by 2

# 4. Median of Two Sorted Arrays
# Hard
# Topics
# Companies
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# https://pythontutor.com/render.html#code=%0Aclass%20Solution%28object%29%3A%0A%20%20%20%20%20def%20findMedianSortedArrays%28self,%20nums1,%20nums2%29%3A%0A%20%20%20%20%20%20%20%20A,%20B%20%3D%20nums1,%20nums2%0A%20%20%20%20%20%20%20%20total%20%3D%20len%28nums1%29%20%2B%20len%28nums2%29%0A%20%20%20%20%20%20%20%20half%20%3D%20total%20//%202%0A%0A%20%20%20%20%20%20%20%20if%20len%28B%29%20%3C%20len%28A%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20A,%20B%20%3D%20B,%20A%0A%0A%20%20%20%20%20%20%20%20l,%20r%20%3D%200,%20len%28A%29%20-%201%0A%20%20%20%20%20%20%20%20while%20True%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20%3D%20%28l%20%2B%20r%29%20//%202%20%20%23%20A%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%3D%20half%20-%20i%20-%202%20%20%23%20B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20Aleft%20%3D%20A%5Bi%5D%20if%20i%20%3E%3D%200%20else%20float%28%22-infinity%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20Aright%20%3D%20A%5Bi%20%2B%201%5D%20if%20%28i%20%2B%201%29%20%3C%20len%28A%29%20else%20float%28%22infinity%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20Bleft%20%3D%20B%5Bj%5D%20if%20j%20%3E%3D%200%20else%20float%28%22-infinity%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20Bright%20%3D%20B%5Bj%20%2B%201%5D%20if%20%28j%20%2B%201%29%20%3C%20len%28B%29%20else%20float%28%22infinity%22%29%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20partition%20is%20correct%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20Aleft%20%3C%3D%20Bright%20and%20Bleft%20%3C%3D%20Aright%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20odd%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20total%20%25%202%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20min%28Aright,%20Bright%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20even%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20%28max%28Aleft,%20Bleft%29%20%2B%20min%28Aright,%20Bright%29%29%20/%202%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20Aleft%20%3E%20Bright%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20r%20%3D%20i%20-%201%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20l%20%3D%20i%20%2B%201%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.findMedianSortedArrays%28%5B1,2,3,4,5,5,6%5D,%5B1,2,3,4,5,6%5D%29&cumulative=false&curInstr=17&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=2&rawInputLstJSON=%5B%5D&textReferences=false