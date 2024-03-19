class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        for i in range(n):
          a, b = b, b + a
        return b
        

# easy DP problem
# adding previous two numbers together starting from 0, and 1
# iterate n times and adding previous to current
#  we will do a(prev), b(current) = b, a + b
    # a will become current number and b which will be next will become the current plus last number
    # we repeat this and return the current numberwhich would be b



# 509. Fibonacci Number
# Solved
# Easy
# Topics
# Companies
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
    


    # https://pythontutor.com/render.html#code=class%20Solution%28object%29%3A%0A%20%20%20%20def%20fib%28self,%20n%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%3Atype%20n%3A%20int%0A%20%20%20%20%20%20%20%20%3Artype%3A%20int%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20a%20%3D%200%0A%20%20%20%20%20%20%20%20b%20%3D%201%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28n%29%3A%0A%20%20%20%20%20%20%20%20%20%20a,%20b%20%3D%20b,%20b%20%2B%20a%0A%20%20%20%20%20%20%20%20return%20b%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.fib%286%29&cumulative=false&curInstr=21&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=2&rawInputLstJSON=%5B%5D&textReferences=false