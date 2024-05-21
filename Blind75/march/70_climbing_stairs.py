class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1, 1
        for n in range(n):
          one, two = two, two + one
        return one
    
# dp but can be done fibonacci way
# set one two variables and loop through n-1 amount of times
# set one to two and two to one plus two simultaneously
# return one


# 70. Climbing Stairs
# Solved
# Easy
# Topics
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 