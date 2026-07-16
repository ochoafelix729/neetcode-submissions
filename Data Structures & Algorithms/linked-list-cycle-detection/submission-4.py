# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow = ListNode()
        slow.next = head
        fast = head
        while slow != fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow == fast