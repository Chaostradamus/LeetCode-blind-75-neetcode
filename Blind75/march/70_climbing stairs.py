class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 1
        two = 1
        for i in range(n):
          one, two = two, one + two
        return one
        


# dynamic programming where we work from the base case
    # if n = 6 we work from the last step with default value of 1
    # at the 5th step we can only take 1 step
    # so far we have 1, 1. at the 4th step we can take 1 step to be on step 5 or 2 to be on step 6. 5 and 6 have 2 possible options
    # so from step 4 there are 2 possible way
    # from step 3 we can do 1 or 2 steps, we will land on step 4 or 5th which are 2 and 1 possibilites respectively
    # we are basically working backwards from the base case(last step) and adding the two previous numbers to move down
    # this is bottom up approach Dynamic programming
    # we run through this N times and return the last step count
    # this is basically fibonacci because of the 1 and 2 steps we are allowed to take
    # if we put both variable declarations on one line it will do it simultaneously as opposed to one after the other

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
    
# https://pythontutor.com/render.html#code=class%20Solution%28object%29%3A%0A%20%20%20%20def%20climbStairs%28self,%20n%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%3Atype%20n%3A%20int%0A%20%20%20%20%20%20%20%20%3Artype%3A%20int%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20one%20%3D%201%0A%20%20%20%20%20%20%20%20two%20%3D%201%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28n%20-1%29%3A%0A%20%20%20%20%20%20%20%20%20%20one,%20two%20%3D%20two,%20one%20%2B%20two%0A%20%20%20%20%20%20%20%20return%20two%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.climbStairs%285%29&cumulative=false&curInstr=15&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=2&rawInputLstJSON=%5B%5D&textReferences=false