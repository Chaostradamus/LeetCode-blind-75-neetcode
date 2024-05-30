class Solution:
    def hammingWeight(self, n: int) -> int:
      res = 0

      while n:
        res += n % 2
        n = n >> 1
      return res

# we set res to 0
# we loop while n is still there
# we increase res by remainder division on n then shifting the bit by 1 by doing >> 1
# return res

# 191. Number of 1 Bits
# Solved
# Easy
# Topics
# Companies
# Write a function that takes the binary representation of a positive integer and returns the number of 
# set bits
#  it has (also known as the Hamming weight).

 

# Example 1:

# Input: n = 11

# Output: 3

# Explanation:

# The input binary string 1011 has a total of three set bits.

# Example 2:

# Input: n = 128

# Output: 1

# Explanation:

# The input binary string 10000000 has a total of one set bit.

# Example 3:

# Input: n = 2147483645

# Output: 30

# Explanation:

# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
        