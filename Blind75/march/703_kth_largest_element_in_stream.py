class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
# dont understand this one
# in python we can put everything into a minHeap which keeps everything sorted from min to max
# while the length of the minheap is lager than k we pop until it equals k
# for adding we push valu to minheap and if size of minheap is larger than k
# we do the same and pop....this pops the smallest element everytime
# return the minheaps min by indexing 0

# i believe we keep heao size k because the lowest in this heap will always be the kth largest and if we append
# anything smaller it wont matter unless its in the number range we current have the minHeap in

# ACCORDING TO CHATGPT
# Sure, let's break down the problem step by step:

# Initialization:

# The class KthLargest needs to be initialized with two parameters: k and nums.
# k represents the kth largest element we want to find.
# nums is the stream of integers provided to initialize the class.
# Data Structure Choice:

# We need a data structure to efficiently maintain the kth largest elements in the stream.
# A min heap is suitable for this purpose. We'll keep a min heap of size k.
# We'll maintain the kth largest elements in the heap, where the smallest element in the heap is the kth largest element in the stream.
# Algorithm:

# During initialization, we'll iterate over nums and add elements to the heap.
# If the size of the heap exceeds k, we'll remove the smallest element (top of the heap).
# To add a new element to the stream (add method), we'll:
# Add the element to the heap.
# If the size of the heap exceeds k, remove the smallest element from the heap.
# The kth largest element will always be the smallest element in the heap.

# 703. Kth Largest Element in a Stream
# Solved
# Easy
# Topics
# Companies
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

# Example 1:

# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]

# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
