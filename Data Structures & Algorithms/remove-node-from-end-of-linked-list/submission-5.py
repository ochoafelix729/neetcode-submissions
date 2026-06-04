# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        # find size
        size = 0
        ptr = dummy
        while ptr:
            ptr = ptr.next
            size += 1

        # remove n'th node from end
        ptr = dummy
        for _ in range(size-n-1):
            ptr = ptr.next
        
        if not ptr.next:
            return None
        
        if not ptr.next.next:
            ptr.next = None
        else:
            ptr.next = ptr.next.next
        
        return dummy.next
        
        
        # remove node 1 (n=2)
        # dummy -> 1 -> 2 -> 3
        # ptr
        
        
