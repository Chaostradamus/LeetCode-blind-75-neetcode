class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      minHeap = []
      for x, y in points:
        dist = (x**2) + (y**2)
        minHeap.append([dist, x, y])
      heapq.heapify(minHeap)

      res = []
      while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x,y])
        k -= 1
      return res


# klogn runtime heapify is (n)
# popping from heap is klogn where k is amount of times we pop and n is size of heap
# thats why this is klogn and slightly better than nlogn
# we first populate an array with xy but also distance calculated as x suqare plus y squared
# after we calculate distance and append dist x and y to minHeap we will heapify it creating a minheap
# this gives us a sorted heap and we can return k times which will give us closest points(dist) from the origin
# we pop from minheap k amount of times by decrementing k until 0 
# we pop and have to create placeholder dist x and y but only appending the xy and y to a new results variable
# when k is 0 we pop out of this while loop and return res which will have the K closing x,y points

# 973. K Closest Points to Origin
# Solved
# Medium
# Topics
# Companies
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

# Example 1:


# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.