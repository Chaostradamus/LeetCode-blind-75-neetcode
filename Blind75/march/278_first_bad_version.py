# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 0, n
        mid = n // 2
        while left < right:
           mid = (left + right) // 2
           if isBadVersion(mid):
               right = mid
           else:
               left = mid + 1
        return left
        
# binary search but when readjusting mid we set right to mid instead of the normal mid -1 because i
# we are moving the right pointer that means we found a bad version
# we move left to mid + 1 still
# another difference is we run the loops while l is less than right and not less than or equal too
# if we do equal to included then we are going too far by 1 step and will be return too late
# left will move past r giving us the wrong answer
# we return once left isnt less than r and that will give us the correct index of the first bad version

# 278. First Bad Version
# Solved
# Easy
# Topics
# Companies
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1
 