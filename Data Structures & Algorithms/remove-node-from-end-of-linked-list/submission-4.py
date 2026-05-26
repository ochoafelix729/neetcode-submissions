# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # find length of linked list
        length = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            length += 1

        i = 0
        goal = length - n

        if goal == 0: return head.next

        prev, curr = None, head
        while i < goal:
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next
        
        return head


