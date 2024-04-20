class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i +1, cur, total)
            
        dfs(0, [], 0)
        return res
    

# another decision tree problem where we iterate along while keeping a current list of choices(cur) a total and the index
# base case is if target is met..we will append to results and then return out of that function call
# another is if i is out of bounds or we go over target with the last addition...we return and break out of that also
# function starts now by adding current candidate choice to choices array and then calling helper function
    # with CURRENT INDEX, current choices, new total with addition
        # we pass in current index without moving index because we can keep taking current index as a choice
        # this is different than the other problems that only let you use the choice once
    # we then pop last choice added
    # then call dfs again on current index+1 to move to next candidate, current choice, and current total without using the current choice
        # this is how we move to next candidate while also not using the current candidate
    # we call dfs on index 0, empty choices array, and a total of 0
    # return res array

# runtime is o(2^t) where t is target value. capped at T which is how large the height will be capped at
    


# 39. Combination Sum
# Solved
# Medium
# Topics
# Companies
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []