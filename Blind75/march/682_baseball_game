class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        ans = [1,2,3]

        for o in operations:
          if o == "+" and len(stack) >= 2:
            stack.append(stack[-2] + stack[-1])
          elif o == "D" and len(stack) > 0:
            stack.append(stack[-1] * 2)
          elif o == "C" and len(stack) > 0:
            stack.pop()
          else:
            stack.append(int(o))
        
        return sum(stack)

# 682. Baseball Game
# Solved
# Easy
# Topics
# Companies
# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

 

# Example 1:

# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.
    


# basically just creating a bootleg stack and iterating through operations
# performing different operations or appending a digit
# remember to append the digit as an int or it will give unicode error
# o(n) time and space because one structure created and running through operations array once