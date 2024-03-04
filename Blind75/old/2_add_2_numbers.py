# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()

        cur = dummy

        carry = 0

        while l1 or l2 or carry:
          v1 = l1.val if l1 else 0
          v2 = l2.val if l2 else 0

          val = v1 + v2 + carry
          carry = val // 10
          val = val % 10

          cur.next = ListNode(val)

          l1 = l1.next if l1 else 0
          l2 = l2.next if l2 else 0
          cur = cur.next
        return dummy.next
# since its in reverse order the ones is already at the head so makes it easier
    # create dummy node and set cur there
    # create carry variable for carrying over for math
    # while theres l1 l2 or carry(for edge cases)
    # value 1 and 2 is each respective value of the current listnode if not null else its 0
    # val = both numbers added..then floor math to get the carry over...then take val and do modulus division for digit to place down
    # create new listnode as cur.next with val
    # move pointers if not null and move current pointer also
    # return dummy.next

# 2. Add Two Numbers
# Medium
# Topics
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]