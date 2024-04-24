class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      heap = [-s for s in stones]
      heapq.heapify(heap)

      while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        if second > first:
          heapq.heappush(heap, first - second)
      heap.append(0)
      return abs(heap[0])
    

# we can just take a maxheap and pop off first 2 values ad compare them. after that we repush to maxheap
# we do this until 1 value or none remain
# in this algo we reverse the sign for every stone in stones to simulate a maxheap
# while there is more than 1 element we pop as first and second
# since everything is negative...if the second is bigger than the first then we find the difference and push it back to the heap
    # this is because it will emulate a subtraction problem instead of making the value bigger
    # once out of the loop we only have 1 or 0 elements....we append a zero in case its empty 
    # we return the absolute value to reversethe sign of the top of the heap because it will be the last sotne or the recently appended 0
    


# 1046. Last Stone Weight
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

 

# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:

# Input: stones = [1]
# Output: 1