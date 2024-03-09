class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative
        prev , cur = None, head

        while cur:
          temp = cur.next
          cur.next = prev
          prev = cur
          cur = temp
        return prev
    
    # recursive
    if not head:
       return None
    
    nh = head
    if head.next:
       nh = self.reverseList(head.next)
       head.next.next = head
    head.next= None
    
    return nh

    



# 206. Reverse Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]

# iterative
# while there is a current
# set pointers to prev cur and next
# set cur's next to prev to reverse
# set prev to cur and then mov current to next
# repeat
# the last run should put current out of bounds and prev at the end of the list
# return prev since it is the head of the reversed list

# recursive approach
# if theres a next on head that means you can call recursively
# set newhead as recursive call on .next
# inside the call reverse the link by doing head.next.next = head
    # cut off the old link by doing head.next = none
    # return the Nh up the chain

# at the end, return Nh as head of the new reversed list