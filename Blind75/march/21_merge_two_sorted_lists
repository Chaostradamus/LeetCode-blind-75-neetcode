# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # create dummy listnode in case of empty list and point to dummy with tail pointer
        # compare head of l1 and l2 values and move pointers
        # if one list is empty point to either or
        # return dummy.next to start off the list 


        node = dummy = ListNode()

        while l1 and l2:
          if l1.val <= l2.val:
            node.next = l1
            l1 = l1.next
          else:
            node.next = l2
            l2 = l2.next
          node = node.next

        node.next = l1 or l2

        return dummy.next
    



# 21. Merge Two Sorted Lists
# Solved
# Easy
# Topics
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

#  iterative appraoch
# set 2 dummy nodes...one will traverse the lists and one will be at the start to keep the list
    # traverse both lists while theyre both active comparing the first values
    # if l1 is the smaller value then point node.next to l1 or l2. 
    # if l1 gets the pointer then move l1 to l1.next to move it's pointer...same for l2
    # at the end there will only be one list left so just set node.next to either active list
# return dummy.next! if you return dummy it will add a 0 to the front of the list and fail the question
