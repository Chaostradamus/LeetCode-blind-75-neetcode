# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        return dummy.next    

        
# https://pythontutor.com/render.html#code=class%20ListNode%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20val%3D0,%20next%3DNone%29%3A%0A%20%20%20%20%20%20%20%20self.val%20%3D%20val%0A%20%20%20%20%20%20%20%20self.next%20%3D%20next%0Aclass%20Solution%3A%0A%20%20%20%20def%20removeNthFromEnd%28self,%20head,%20n%29%3A%0A%20%20%20%20%20%20%20%20dummy%20%3D%20ListNode%280,%20head%29%0A%20%20%20%20%20%20%20%20left%20%3D%20dummy%0A%20%20%20%20%20%20%20%20right%20%3D%20head%0A%0A%20%20%20%20%20%20%20%20while%20n%20%3E%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20right%20%3D%20right.next%0A%20%20%20%20%20%20%20%20%20%20%20%20n%20-%3D%201%0A%0A%20%20%20%20%20%20%20%20while%20right%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20left%20%3D%20left.next%0A%20%20%20%20%20%20%20%20%20%20%20%20right%20%3D%20right.next%0A%0A%20%20%20%20%20%20%20%20%23%20delete%0A%20%20%20%20%20%20%20%20left.next%20%3D%20left.next.next%0A%20%20%20%20%20%20%20%20return%20dummy.next%0A%0A%20%20%20%20%20%20%20%20%0Ab%20%3D%20Solution%28%29%0Ab.removeNthFromEnd%28%5B3,2,0,-4%5D,%202%29&cumulative=false&curInstr=14&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# o(n) runtime and o(1) space
# create a dummy node to return from head
# set left pointer to dummy and right to head
# to move right n steps ahead, while loop while n > 0 down to 0 and move right to right.next n times
# while loop with conditions that right is in bounds...move left and right to next...once right is null
# set left to left.next.next to "delete" nth node
# we set left to dummy because if we set left to head, then we will land on nth node from the end without a way to have access to previous
# this way we are at previous of nth node and can just set links to after it and thus deleting it
# return dummy instead of head because of edge case in case list is of size 1 and you need to return null

# 1/16/2023
    # 1/18/2024
    # set left as dummy node and right at head. move right while decrementing n to 0
    # move right and left pointers until right is out of bounds
    # set lefts next as .next.next and return dummy node's.next to start at head of linked list
