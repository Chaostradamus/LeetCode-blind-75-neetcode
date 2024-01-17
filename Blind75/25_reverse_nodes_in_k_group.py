# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # solution from leetcode
# Use a dummy head, and

# l, r : define reversing range

# pre, cur : used in reversing, standard reverse linked linked list method

# jump : used to connect last node in previous k-group to first node in following k-group

# def reverseKGroup(self, head, k):
#     dummy = jump = ListNode(0)
#     dummy.next = l = r = head
    
#     while True:
#         count = 0
#         while r and count < k:   # use r to locate the range
#             r = r.next
#             count += 1
#         if count == k:  # if size k satisfied, reverse the inner linked list
#             pre, cur = r, l
#             for _ in range(k):
#                 cur.next, cur, pre = pre, cur.next, cur  # standard reversing
#             jump.next, jump, l = pre, l, r  # connect two k-groups
#         else:
#             return dummy.next


# hard question
# 25. Reverse Nodes in k-Group
# Hard
# Topics
# Companies
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]