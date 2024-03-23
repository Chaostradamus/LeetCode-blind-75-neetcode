# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
   
        if not lists or len(lists) == 0:
          return None

        while len(lists) > 1:
          mergedLists = []
          for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(self.mergeList(l1, l2))
          lists = mergedLists
        return lists[0]
    def mergeList(self, l1, l2):
          dummy = ListNode()
          tail = dummy

          while l1 and l2:
            if l1.val < l2.val:
              tail.next = l1
              l1 = l1.next
            else:
              tail.next = l2
              l2 = l2.next
            tail = tail.next
          if l1:
            tail.next = l1
          else:
            tail.next = l2
          return dummy.next
        

# merge function same as all merge functions. create 2 nodes one dummy and one tail
    # iterate through while setting next to lowest value from head of lists and update pointers
    # once one list is empty append the other list
    # for main function while length of lists is more than 1
    # iterate through lists 2 by 2
    # set l1 to lists at i and list 2 to lists at i+1 but check if its in bounds else return one. we can still merge with an empty l2
    # append mergings to new mergedList array and set lists to that at the end
    # once through the iteration set lists to mergedLists tp update it to the merged list pairings..this will pair and merge until 1 
    # list is left


# 23. Merge k Sorted Lists
# Solved
# Hard
# Topics
# Companies
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 